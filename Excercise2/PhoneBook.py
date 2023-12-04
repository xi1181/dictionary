class PhoneBook:
    def __init__(self):
        self.contactDictionary = {}

    def add_contact(self, name, phone):
        if name in self.contactDictionary:
            print("Contact already exists.")
        else:
            self.contactDictionary[name] = phone

    def lookup_contact(self, name):
        if name not in self.contactDictionary:
            print("Contact does not exists.")
        else:
            print(f"{name} -> {self.contactDictionary[name]}")

    def delete_contact(self, name):
        if name not in self.contactDictionary:
            print("Contact does not exists.")
        else:
            del self.contactDictionary[name]

    def display_contacts(self):
        print("List of Contacts")
        print("------------------------")
        for name in self.contactDictionary:
            print(f"{name} -> {self.contactDictionary[name]}")