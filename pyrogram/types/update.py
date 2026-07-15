#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram


class Update:
    def stop_propagation(self):
        raise pyrogram.StopPropagation

    def continue_propagation(self):
        raise pyrogram.ContinuePropagation
