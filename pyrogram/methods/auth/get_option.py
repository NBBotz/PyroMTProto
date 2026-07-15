#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw


class GetOption:
    @staticmethod
    def _parse_tggob_json(obj):
        """Recursively parses Telegram's raw JSON types into native Python types."""
        if isinstance(obj, raw.types.JsonString):
            return obj.value
        elif isinstance(obj, raw.types.JsonNumber):
            return obj.value
        elif isinstance(obj, raw.types.JsonBool):
            return obj.value
        elif isinstance(obj, raw.types.JsonNull):
            return None
        elif isinstance(obj, raw.types.JsonArray):
            # Recursively parse every item in the array to a Python list
            return [GetOption._parse_tggob_json(item) for item in obj.value]
        elif isinstance(obj, raw.types.JsonObject):
            # Recursively parse every key-value pair to a Python dict
            return {item.key: GetOption._parse_tggob_json(item.value) for item in obj.value}
        # Fallback for base values
        return obj

    async def get_option(
        self: "pyrogram.Client",
        name: str,
    ) -> Optional[Union[bool, int, str, list, dict]]:
        """Returns the value of an option by its name.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            name (``str``):
                The name of the option.

        Returns:
            ``bool`` | ``int`` | ``str`` | ``list`` | ``dict``: On success, the value of the option is returned.

        """
        app_config = await self.invoke(
            raw.functions.help.GetAppConfig(
                hash=0
            )
        )
        option = next(
            (x for x in app_config.config.value if x.key == name), 
            None
        )
        if not option:
            return option
        return self._parse_tggob_json(option.value)
