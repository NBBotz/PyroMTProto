#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..rpc_error import RPCError


class Unauthorized(RPCError):
    """Unauthorized"""
    CODE = 401
    """``int``: RPC Error Code"""
    NAME = __doc__


class ActiveUserRequired(Unauthorized):
    """The method is only available to already activated users"""
    ID = "ACTIVE_USER_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthKeyInvalid(Unauthorized):
    """The specified auth key is invalid."""
    ID = "AUTH_KEY_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthKeyPermEmpty(Unauthorized):
    """The method is unavailable for temporary authorization keys, not bound to a permanent authorization key."""
    ID = "AUTH_KEY_PERM_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthKeyUnregistered(Unauthorized):
    """The specified authorization key is not registered in the system (for example, a PFS temporary key has expired)."""
    ID = "AUTH_KEY_UNREGISTERED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SessionExpired(Unauthorized):
    """The session has expired."""
    ID = "SESSION_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SessionPasswordNeeded(Unauthorized):
    """2FA is enabled, use a password to login."""
    ID = "SESSION_PASSWORD_NEEDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SessionRevoked(Unauthorized):
    """The session was revoked by the user."""
    ID = "SESSION_REVOKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserDeactivated(Unauthorized):
    """The current account was deleted by the user."""
    ID = "USER_DEACTIVATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserDeactivatedBan(Unauthorized):
    """The current account was deleted and banned by Telegram's antispam system."""
    ID = "USER_DEACTIVATED_BAN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


