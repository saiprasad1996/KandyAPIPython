class User:
    api_key = ''
    api_secrect = ''

    def __init__(self, api_key, api_secrect):
        self.api_key = api_key
        self.api_secrect = api_secrect

    def get_user_access_token(self, user_id, give_json=False):
        pass

    def get_user_access_token_alt(self, user_id, user_password, give_json=False):
        pass

    def delete_user_access_token(self, user_id, user_password, user_access_token, give_json=False):
        pass

    def create_device(self, device_native_id, device_family, device_name, client_sw_version, device_os_version,
                      give_json=False):  # please check this one over API docc
        pass

    def delete_device(self, device_id, give_json=False):
        pass

    def get_list_of_devices(self, give_json=False):
        pass

    def get_user_personal_addressbook(self, give_json=False):
        pass

    def add_contact_to_personal_addressbook(self, name, image_id, give_json=False):
        pass

    def delete_contact_from_personal_addressbook(self, contact_id, give_json=False):
        pass

    def get_user_device_addressbooks(self, device_id, give_json=False):
        pass
