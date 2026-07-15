#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw, utils
from ..object import Object
from typing import Optional


class LinkPreviewOptions(Object):
    """Describes the options used for link preview generation.

    Parameters:
        is_disabled (``bool``, *optional*):
            True, if the link preview is disabled

        url (``str``, *optional*):
            URL to use for the link preview.
            If empty, then the first URL found in the message text will be used

        prefer_small_media (``bool``, *optional*):
            True, if the media in the link preview is suppposed to be shrunk;
            ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
        
        prefer_large_media (``bool``, *optional*):
            True, if the media in the link preview is suppposed to be enlarged;
            ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
        
        show_above_text (``bool``, *optional*):
            True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text
        
        manual (``bool``, *optional*):

        safe (``bool``, *optional*):
    """

    def __init__(
        self,
        *,
        is_disabled: bool = None,
        url: str = None,
        prefer_small_media: bool = None,
        prefer_large_media: bool = None,
        show_above_text: bool = None,
        manual: bool = None,
        safe: bool = None
    ):
        super().__init__()

        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text
        self.manual = manual
        self.safe = safe

    @staticmethod
    def _parse(
        client,
        media_webpage: "raw.types.MessageMediaWebPage",
        media_first_url: str = None,
        invert_media: bool = False
    ) -> Optional["LinkPreviewOptions"]:
        if (
            media_webpage and
            isinstance(media_webpage, raw.types.MessageMediaWebPage)
        ):
            if media_webpage.webpage:
                media_first_url = media_webpage.webpage.url
            return LinkPreviewOptions(
                is_disabled=False,
                url=media_first_url,
                prefer_small_media=getattr(media_webpage, "force_small_media"),
                prefer_large_media=getattr(media_webpage, "force_large_media"),
                show_above_text=invert_media,
                manual=getattr(media_webpage, "manual"),
                safe=getattr(media_webpage, "safe")
            )
        if media_first_url:
            return LinkPreviewOptions(
                is_disabled=True,
                url=media_first_url,
                show_above_text=invert_media,
            )
