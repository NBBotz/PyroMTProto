#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional
import pyrogram
from pyrogram import raw


class UpdateBusinessGreetingMessage:
    async def update_business_greeting_message(
        self: "pyrogram.Client",
        shortcut_id: Optional[int] = None,
        no_activity_days: int = 7,
        recipients_type: str = "all",
        recipients: Optional[list] = None,
        exclude_recipients: Optional[list] = None,
    ) -> bool:
        """Set or clear your Business greeting message.

        The greeting message is sent automatically to users who message
        you for the first time (or after a period of inactivity).

        Parameters:
            shortcut_id (``int``, *optional*):
                ID of the quick-reply shortcut to use. Pass None to disable.

            no_activity_days (``int``, *optional*):
                Re-send the greeting if no activity for this many days.
                Defaults to 7.

            recipients_type (``str``, *optional*):
                ``"all"``, ``"contacts"``, ``"non_contacts"``, or ``"selected"``.

            recipients (``list`` of ``int``, *optional*):
                User IDs when ``recipients_type="selected"``.

            exclude_recipients (``list`` of ``int``, *optional*):
                User IDs to exclude when ``recipients_type="all"``.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.update_business_greeting_message(
                    shortcut_id=2,
                    no_activity_days=14,
                    recipients_type="non_contacts"
                )

                # Disable greeting
                await app.update_business_greeting_message()
        """
        greeting = None
        if shortcut_id is not None:
            if recipients_type == "contacts":
                rcpts = raw.types.BusinessRecipients(contacts=True)
            elif recipients_type == "non_contacts":
                rcpts = raw.types.BusinessRecipients(non_contacts=True)
            elif recipients_type == "selected" and recipients:
                rcpts = raw.types.BusinessRecipients(
                    users=[raw.types.InputUser(user_id=uid, access_hash=0) for uid in recipients],
                )
            else:
                rcpts = raw.types.BusinessRecipients(
                    all_users=True,
                    exclude_users=[
                        raw.types.InputUser(user_id=uid, access_hash=0)
                        for uid in (exclude_recipients or [])
                    ] or None,
                )

            greeting = raw.types.BusinessGreetingMessage(
                shortcut_id=shortcut_id,
                recipients=rcpts,
                no_activity_days=no_activity_days,
            )

        await self.invoke(
            raw.functions.account.UpdateBusinessGreetingMessage(message=greeting)
        )
        return True
