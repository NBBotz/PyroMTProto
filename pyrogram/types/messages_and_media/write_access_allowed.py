#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw
from ..object import Object


class WriteAccessAllowed(Object):
    """This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method `requestWriteAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`__.

    Parameters:
        from_request (``bool``, *optional*):
            True, if the access was granted after the user accepted an explicit request from a Web App sent by the method `requestWriteAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`__

        web_app_name (``str``, *optional*):
            Name of the Web App, if the access was granted when the Web App was launched from a link
        
        from_attachment_menu (``bool``, *optional*):
            True, if the access was granted when the bot was added to the attachment or side menu

    """

    def __init__(
        self,
        *,
        from_request: bool = None,
        web_app_name: str = None,
        from_attachment_menu: bool = None,
    ):
        super().__init__()

        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu

    @staticmethod
    def _parse(action: "raw.types.MessageActionBotAllowed"):
        return WriteAccessAllowed(
            from_request=action.from_request if action.from_request else None,
            web_app_name=action.app.short_name if action.app is not None else None,
            from_attachment_menu=action.attach_menu if action.attach_menu else None,
        )
