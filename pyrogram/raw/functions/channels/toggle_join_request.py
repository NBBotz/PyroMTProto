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


class ToggleJoinRequest(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``ECC2618``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        enabled (``bool``):
            N/A

        apply_to_invites (``bool``, *optional*):
            N/A

        guard_bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = ["channel", "enabled", "apply_to_invites", "guard_bot"]

    ID = 0xecc2618
    QUALNAME = "functions.channels.ToggleJoinRequest"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool, apply_to_invites: Optional[bool] = None, guard_bot: "raw.base.InputUser" = None) -> None:
        self.channel = channel  # InputChannel
        self.enabled = enabled  # Bool
        self.apply_to_invites = apply_to_invites  # flags.1?true
        self.guard_bot = guard_bot  # flags.0?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleJoinRequest":
        
        flags = Int.read(b)
        
        apply_to_invites = True if flags & (1 << 1) else False
        channel = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        guard_bot = TLObject.read(b) if flags & (1 << 0) else None
        
        return ToggleJoinRequest(channel=channel, enabled=enabled, apply_to_invites=apply_to_invites, guard_bot=guard_bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.apply_to_invites else 0
        flags |= (1 << 0) if self.guard_bot is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        if self.guard_bot is not None:
            b.write(self.guard_bot.write())
        
        return b.getvalue()
