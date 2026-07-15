#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import asyncio
import ipaddress
import logging
import socket
from typing import Optional

log = logging.getLogger(__name__)

SEND_BUFFER_SIZE = 1024 * 1024        # 1 MB send buffer
RECV_BUFFER_SIZE = 4 * 1024 * 1024   # 4 MB receive buffer


class TCP:
    def __init__(self, ipv6: bool, proxy: dict):
        self.socket: socket.socket | None = None
        self.reader: asyncio.StreamReader | None = None
        self.writer: asyncio.StreamWriter | None = None
        self.loop = asyncio.get_event_loop()
        self.ipv6 = ipv6
        self.proxy = proxy

    async def connect(self, address: tuple):
        try:
            import socks
        except ImportError:
            raise ImportError(
                'PySocks is missing and Pyrogram can\'t run without. '
                'Please install it using "pip3 install pysocks".'
            )

        if self.proxy:
            hostname = address[0]
            try:
                ipaddress.ip_address(hostname)
                is_ip = True
            except ValueError:
                is_ip = False

            self.socket = socks.socksocket(
                socket.AF_INET6 if self.ipv6 else socket.AF_INET
            )
            self.socket.set_proxy(
                proxy_type=self.proxy.get("scheme"),
                addr=self.proxy.get("hostname"),
                port=self.proxy.get("port"),
                username=self.proxy.get("username"),
                password=self.proxy.get("password"),
                rdns=not is_ip,
            )
        else:
            self.socket = socket.socket(
                socket.AF_INET6 if self.ipv6 else socket.AF_INET
            )

        # Maximize throughput: large socket buffers, disable Nagle
        self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFFER_SIZE)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFFER_SIZE)
        except OSError:
            pass  # Some platforms may restrict this

        self.socket.setblocking(False)

        await self.loop.sock_connect(self.socket, address)

        self.reader, self.writer = await asyncio.open_connection(sock=self.socket)

    def close(self):
        if self.writer:
            try:
                self.writer.close()
            except Exception:
                pass

    async def send(self, data: bytes, *args):
        """Send all bytes, draining the writer."""
        if self.writer is None:
            raise OSError("Not connected")
        self.writer.write(data)
        await self.writer.drain()

    async def recv(self, length: int = 0) -> Optional[bytes]:
        """Receive exactly `length` bytes; returns None on EOF."""
        if self.reader is None:
            return None
        try:
            if length:
                # readexactly raises IncompleteReadError on EOF — convert to None
                data = await self.reader.readexactly(length)
                return data
            else:
                return await self.reader.read(4096)
        except (asyncio.IncompleteReadError, asyncio.LimitOverrunError, ConnectionResetError, OSError):
            return None
