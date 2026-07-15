#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class WebAppInfo(Object):
    """Contains information about a `Web App <https://core.telegram.org/bots/webapps>`_.

    Parameters:
        url (``str``):
            An HTTPS URL of a Web App to be opened with additional data as specified in
            `Initializing Web Apps <https://core.telegram.org/bots/webapps#initializing-web-apps>`_.
    """

    def __init__(
        self, *,
        url: str,
    ):
        super().__init__()

        self.url = url
