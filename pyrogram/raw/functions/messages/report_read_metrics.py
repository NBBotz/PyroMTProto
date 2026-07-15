#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from io import BytesIO
from typing import TYPE_CHECKING, Optional, Any

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject

if TYPE_CHECKING:
    from pyrogram import raw

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ReportReadMetrics(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``4067C5E6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        metrics (List of :obj:`InputMessageReadMetric <pyrogram.raw.base.InputMessageReadMetric>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["peer", "metrics"]

    ID = 0x4067c5e6
    QUALNAME = "functions.messages.ReportReadMetrics"

    def __init__(self, *, peer: "raw.base.InputPeer", metrics: list["raw.base.InputMessageReadMetric"]) -> None:
        self.peer = peer  # InputPeer
        self.metrics = metrics  # Vector<InputMessageReadMetric>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportReadMetrics":
        # No flags
        
        peer = TLObject.read(b)
        
        metrics = TLObject.read(b)
        
        return ReportReadMetrics(peer=peer, metrics=metrics)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.metrics))
        
        return b.getvalue()
