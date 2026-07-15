#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw
from .auto_name import AutoName


class SentCodeType(AutoName):
    """Sent code type enumeration used in :obj:`~pyrogram.types.SentCode`."""

    APP = raw.types.auth.SentCodeTypeApp
    "The code was sent through the telegram app."

    CALL = raw.types.auth.SentCodeTypeCall
    "The code will be sent via a phone call. A synthesized voice will tell the user which verification code to input."

    FLASH_CALL = raw.types.auth.SentCodeTypeFlashCall
    "The code will be sent via a flash phone call, that will be closed immediately."

    MISSED_CALL = raw.types.auth.SentCodeTypeMissedCall
    "The code will be sent via a Missed call. User manually enters last digits of the calling phone number."

    SMS = raw.types.auth.SentCodeTypeSms
    "The code was sent via SMS."

    FRAGMENT_SMS = raw.types.auth.SentCodeTypeFragmentSms
    "The code was sent via Fragment SMS."

    FIREBASE_SMS = raw.types.auth.SentCodeTypeFirebaseSms
    "The code should be delivered via SMS after Firebase attestation."

    EMAIL_CODE = raw.types.auth.SentCodeTypeEmailCode
    "The code was sent via email."

    SETUP_EMAIL_REQUIRED = raw.types.auth.SentCodeTypeSetUpEmailRequired
    "The user should add and verify an email address in order to login."
