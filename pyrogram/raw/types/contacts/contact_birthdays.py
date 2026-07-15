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


class ContactBirthdays(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.ContactBirthdays`.

    Details:
        - Layer: ``227``
        - ID: ``114FF30D``

    Parameters:
        contacts (List of :obj:`ContactBirthday <pyrogram.raw.base.ContactBirthday>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetBirthdays
    """

    __slots__: list[str] = ["contacts", "users"]

    ID = 0x114ff30d
    QUALNAME = "types.contacts.ContactBirthdays"

    def __init__(self, *, contacts: list["raw.base.ContactBirthday"], users: list["raw.base.User"]) -> None:
        self.contacts = contacts  # Vector<ContactBirthday>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContactBirthdays":
        # No flags
        
        contacts = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ContactBirthdays(contacts=contacts, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.contacts))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
