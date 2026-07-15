#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    PageBlock = Union[raw.types.InputPageBlockMap, raw.types.PageBlockAnchor, raw.types.PageBlockAudio, raw.types.PageBlockAuthorDate, raw.types.PageBlockBlockquote, raw.types.PageBlockBlockquoteBlocks, raw.types.PageBlockChannel, raw.types.PageBlockCollage, raw.types.PageBlockCover, raw.types.PageBlockDetails, raw.types.PageBlockDivider, raw.types.PageBlockEmbed, raw.types.PageBlockEmbedPost, raw.types.PageBlockFooter, raw.types.PageBlockHeader, raw.types.PageBlockHeading1, raw.types.PageBlockHeading2, raw.types.PageBlockHeading3, raw.types.PageBlockHeading4, raw.types.PageBlockHeading5, raw.types.PageBlockHeading6, raw.types.PageBlockKicker, raw.types.PageBlockList, raw.types.PageBlockMap, raw.types.PageBlockMath, raw.types.PageBlockOrderedList, raw.types.PageBlockParagraph, raw.types.PageBlockPhoto, raw.types.PageBlockPreformatted, raw.types.PageBlockPullquote, raw.types.PageBlockRelatedArticles, raw.types.PageBlockSlideshow, raw.types.PageBlockSubheader, raw.types.PageBlockSubtitle, raw.types.PageBlockTable, raw.types.PageBlockThinking, raw.types.PageBlockTitle, raw.types.PageBlockUnsupported, raw.types.PageBlockVideo]
else:
    # noinspection PyRedeclaration
    class PageBlock(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 39 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPageBlockMap
            PageBlockAnchor
            PageBlockAudio
            PageBlockAuthorDate
            PageBlockBlockquote
            PageBlockBlockquoteBlocks
            PageBlockChannel
            PageBlockCollage
            PageBlockCover
            PageBlockDetails
            PageBlockDivider
            PageBlockEmbed
            PageBlockEmbedPost
            PageBlockFooter
            PageBlockHeader
            PageBlockHeading1
            PageBlockHeading2
            PageBlockHeading3
            PageBlockHeading4
            PageBlockHeading5
            PageBlockHeading6
            PageBlockKicker
            PageBlockList
            PageBlockMap
            PageBlockMath
            PageBlockOrderedList
            PageBlockParagraph
            PageBlockPhoto
            PageBlockPreformatted
            PageBlockPullquote
            PageBlockRelatedArticles
            PageBlockSlideshow
            PageBlockSubheader
            PageBlockSubtitle
            PageBlockTable
            PageBlockThinking
            PageBlockTitle
            PageBlockUnsupported
            PageBlockVideo
        """

        QUALNAME = "pyrogram.raw.base.PageBlock"
        __union_types__ = Union[raw.types.InputPageBlockMap, raw.types.PageBlockAnchor, raw.types.PageBlockAudio, raw.types.PageBlockAuthorDate, raw.types.PageBlockBlockquote, raw.types.PageBlockBlockquoteBlocks, raw.types.PageBlockChannel, raw.types.PageBlockCollage, raw.types.PageBlockCover, raw.types.PageBlockDetails, raw.types.PageBlockDivider, raw.types.PageBlockEmbed, raw.types.PageBlockEmbedPost, raw.types.PageBlockFooter, raw.types.PageBlockHeader, raw.types.PageBlockHeading1, raw.types.PageBlockHeading2, raw.types.PageBlockHeading3, raw.types.PageBlockHeading4, raw.types.PageBlockHeading5, raw.types.PageBlockHeading6, raw.types.PageBlockKicker, raw.types.PageBlockList, raw.types.PageBlockMap, raw.types.PageBlockMath, raw.types.PageBlockOrderedList, raw.types.PageBlockParagraph, raw.types.PageBlockPhoto, raw.types.PageBlockPreformatted, raw.types.PageBlockPullquote, raw.types.PageBlockRelatedArticles, raw.types.PageBlockSlideshow, raw.types.PageBlockSubheader, raw.types.PageBlockSubtitle, raw.types.PageBlockTable, raw.types.PageBlockThinking, raw.types.PageBlockTitle, raw.types.PageBlockUnsupported, raw.types.PageBlockVideo]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/page-block"
            )
