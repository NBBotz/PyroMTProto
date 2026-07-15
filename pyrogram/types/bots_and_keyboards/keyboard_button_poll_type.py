#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import enums
from ..object import Object


class KeyboardButtonPollType(Object):
    """This object represents type of a poll,
    which is allowed to be created and sent when the corresponding button is pressed.

    - :obj:`~pyrogram.types.KeyboardButtonPollTypeRegular`

        If regular is passed, only regular polls will be allowed.

    - :obj:`~pyrogram.types.KeyboardButtonPollTypeQuiz`

        If quiz is passed, the user will be allowed to create only polls in the quiz mode.

    Otherwise, the user will be allowed to create a poll of any type.
    """
    def __init__(
        self,
        type: enums.PollType
    ):
        self.type = type


class KeyboardButtonPollTypeRegular(KeyboardButtonPollType):
    def __init__(
        self
    ):
        super().__init__(type=enums.PollType.REGULAR)


class KeyboardButtonPollTypeQuiz(KeyboardButtonPollType):
    def __init__(
        self
    ):
        super().__init__(type=enums.PollType.QUIZ)
