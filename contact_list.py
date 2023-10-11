import re


class ContactList:
    def __init__(self, name: str, contacts: list[dict]):
        self._name = name
        self._contacts = contacts
        self._contacts.sort(key=lambda contact: contact["name"].lower())

    @property
    def get_name(self):
        return self._name

    @property
    def get_contacts(self):
        return self._contacts

    @get_name.setter
    def set_name(self, name: str):
        if type(name) == str:
            self._name = name

    @get_contacts.setter
    def set_contacts(self, contacts):
        self._contacts = contacts

    @staticmethod
    def validate_number(phone_number):
        pattern = "^([0-9]{3})?(-|.| )?[0-9]{3}(-|.| )?[0-9]{4}$"
        if re.match(pattern, phone_number):
            return True
        else:
            return False

    def add_contact(self, contact: dict):
        if type(contact["name"]) == str and ContactList.validate_number(
            contact["number"]
        ):
            self._contacts.append(contact)
            self._contacts.sort(key=lambda contact: contact["name"].lower())

    def remove_contact(self, name: str):
        for contact in self._contacts:
            if contact["name"] == name:
                to_remove = contact
        if to_remove:
            self._contacts.remove(to_remove)

    def find_shared_contacts(self, contact_list: "ContactList") -> list:
        matched_contacts = []
        for contact in self._contacts:
            if contact in contact_list.get_contacts:
                matched_contacts.append(contact)

        return matched_contacts


friends = [
    {"name": "Alice", "number": "867-5309"},
    {"name": "Bob", "number": "555-5555"},
]
work_buddies = [
    {"name": "Alice", "number": "867-5309"},
    {"name": "Carlos", "number": "555-5555"},
]

my_friends_list = ContactList("My Friends", friends)
my_work_buddies = ContactList("Work Buddies", work_buddies)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)

print(friends_i_work_with)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]
