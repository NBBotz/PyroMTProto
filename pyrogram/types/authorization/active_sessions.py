#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class ActiveSessions(Object):
    """Contains a list of sessions

    Parameters:
        inactive_session_ttl_days (``int``):
            Number of days of inactivity before sessions will automatically be terminated; 1-366 days.

        active_sessions (List of :obj:`~pyrogram.types.ActiveSession`):
            List of sessions.

    """

    def __init__(
        self,
        *,
        inactive_session_ttl_days: int = None,
        active_sessions: list["types.ActiveSession"] = None
    ):
        super().__init__()

        self.inactive_session_ttl_days = inactive_session_ttl_days
        self.active_sessions = active_sessions

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        authorizations: "raw.types.account.Authorizations"
    ) -> "ActiveSessions":        
        return ActiveSessions(
            inactive_session_ttl_days=authorizations.authorization_ttl_days,
            active_sessions=types.List([
                types.ActiveSession._parse(client, active)
                for active in authorizations.authorizations
            ])
        )
