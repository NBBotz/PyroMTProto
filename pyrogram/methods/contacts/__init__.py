#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .add_contact import AddContact
from .delete_contacts import DeleteContacts
from .get_contacts import GetContacts
from .get_contacts_count import GetContactsCount
from .import_contacts import ImportContacts


class Contacts(
    AddContact,
    DeleteContacts,
    GetContacts,
    GetContactsCount,
    ImportContacts,
):
    pass
