import requests

import Constants


class Domain:
    api_key = None
    domain_api_secret = None
    domain_access_token = None

    def __init__(self, api_key, api_secret):
        """
        
        :param api_key: API key from the kandy accounts section for a project
        :param api_secret: API secret from the kandy accounts section for a project
        """
        self.api_key = api_key
        self.domain_api_secret = api_secret

    def get_access_token(self, give_json=False):
        """
        
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        """
        url = Constants.BASE_URL + "domains/accesstokens"
        response = requests.get(url=url, params={'key': self.api_key, 'domain_api_secret': self.domain_api_secret})
        json_obj = response.json()
        self.domain_access_token = json_obj["result"]["domain_access_token"]
        if give_json:
            return json_obj
        else:
            return response.text

    def delete_access_token(self, give_json=False):
        """
        
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """

        url = Constants.BASE_URL + "domains/accesstokens"
        response = requests.delete(url=url, params={"key": self.api_key, "domain_api_secret": self.domain_api_secret,
                                                    "domain_access_token": self.domain_access_token})

        if give_json:
            return response.json()
        else:
            return response.text

    def get_limited_domain_detail(self, give_json=False):
        """
        
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """

        url = Constants.BASE_URL + "accounts/domains/details"
        response = requests.get(url=url, params={'key': self.api_key, 'domain_access_token': self.domain_access_token,
                                                 'domain_api_secret': self.domain_api_secret})
        if give_json:
            return response.json()
        else:
            return response.text

    def create_user_by_phno(self, user_phno, user_country_code, user_first_name=None, user_last_name=None,
                            user_email=None, user_password=None, give_json=False):
        """
        
        :param user_phno: Local phone number of the user in the JSON body.
        :param user_country_code: 2 letter user country code .
        :param user_first_name: First Name of the user 
        :param user_last_name: Last Name of the user
        :param user_email: Email address of the User
        :param user_password: User password. (8-20 characters, at least 1 letter, at least 2 digits, and characters ! @ ( ) & ' - . , ? ^ _ are allowed, if not provided the platform will generate it)
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/users/phone_number"
        json_body = {"user_phone_number": user_phno,
                     "user_country_code": user_country_code,
                     "user_first_name": user_first_name,
                     "user_last_name": user_last_name,
                     "user_password": user_password}

        response = requests.post(url=url, params={"key": self.domain_access_token}, json=json_body)

        if give_json:
            return response.json()
        else:
            return response.text

    def create_user_by_userid(self, user_id, user_country_code, user_first_name=None, user_last_name=None,
                              user_email=None, user_password=None, give_json=False):

        """
        
        :param user_id: 
        :param user_country_code: 
        :param user_first_name: 
        :param user_last_name: 
        :param user_email: 
        :param user_password: 
         :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/users/user_id"
        response = requests.post(url=url, params={"key": self.domain_access_token},
                                 json={"user_id": user_id,
                                       "user_country_code": user_country_code,
                                       "user_first_name": user_first_name,
                                       "user_last_name": user_last_name,
                                       "user_email": user_email,
                                       "user_password": user_password
                                       })
        if give_json:
            return response.json()
        else:
            return response.text

    def delete_user(self, user_api_key=None, user_id=None, user_password=None, give_json=False):
        """
        
        :param user_api_key: 
        :param user_id: 
        :param user_password: 
         :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
         
        """
        url = Constants.BASE_URL + "domains/users"
        response = requests.delete(url=url, params={"key": self.domain_access_token,
                                                    "user_api_key": user_api_key,
                                                    "user_id": user_id,
                                                    "user_password": user_password})
        if give_json:
            return response.json()
        else:
            return response.text

    def get_list_of_users(self, give_json=False):
        """
        
         :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object of list of users depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/users"
        response = requests.get(url=url, params={"key": self.domain_access_token})
        if give_json:
            return response.json()
        else:
            return response.text

    def get_user_details(self, user_access_token=None, user_api_key=None, give_json=False):
        """
        
        :param user_access_token: 
        :param user_api_key: 
         :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object of user details depending upon give_json parameter
        
        """

        url = Constants.BASE_URL + "domains/users/details"
        response = requests.get(url=url, params={"key": self.domain_access_token,
                                                 "user_access_token": user_access_token,
                                                 "user_api_key": user_api_key})
        if give_json:
            return response.json()
        else:
            return response.text

    def get_country_code(self, MCC=None, give_json=False):
        """
        
        :param MCC: 
         :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
         
        """
        url = Constants.BASE_URL + "domains/countrycodes"
        response = requests.get(url=url, params={"key": self.domain_access_token,
                                                 "MCC": MCC})
        if give_json:
            return response.json()
        else:
            return response.text

    def send_validation_code_sms(self, user_phone_number, user_country_code, give_json=False):
        """
        
        :param user_phone_number: 
        :param user_country_code: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
         
        """
        url = Constants.BASE_URL + "domains/verifications/smss"
        response = requests.post(url=url, params={"key": self.domain_access_token,
                                                  }, data={"user_phone_number": user_phone_number,
                                                           "user_country_code": user_country_code})
        if give_json:
            return response.json()
        else:
            return response.text

    def verify_validation_code(self, validation_code, give_json=False):
        """
        
        :param validation_code: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/verifications/codes"
        response = requests.get(url=url, params={"key": self.domain_access_token,
                                                 "validation_code": validation_code})
        if give_json:
            return response.json()
        else:
            return response.text

    def create_hunt_group(self, huntgroup_name, huntgroup_type, pilot_uri_address, overflow_dest, anonymous_uri,
                          give_json=False):
        """
        
        :param huntgroup_name: 
        :param huntgroup_type: 
        :param pilot_uri_address: 
        :param overflow_dest: 
        :param anonymous_uri: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/huntgroups"
        response = requests.post(url=url, params={"key": self.domain_access_token},
                                 json={"huntgroup_name": huntgroup_name,
                                       "huntgroup_type": huntgroup_type,
                                       "pilot_uri_address": pilot_uri_address,
                                       "overflow_dest": overflow_dest,
                                       "anonymous_uri": anonymous_uri})
        if give_json:
            return response.json()
        else:
            return response.text

    def delete_hunt_group(self, huntgroup_name, give_json=False):
        """
        
        :param huntgroup_name: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/huntgroups"
        response = requests.delete(url=url, params={"key": self.domain_access_token, "huntgroup_name": huntgroup_name})
        if give_json:
            return response.json()
        else:
            return response.text

    def list_hunt_groups(self, give_json=False):
        """
        
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
         
        """
        url = Constants.BASE_URL + "domains/huntgroups"
        response = requests.get(url=url, params={"key": self.domain_access_token})
        if give_json:
            return response.json()
        else:
            return response.text

    def add_huntgroup_user(self, huntgroup_name, user_name, give_json=False):
        """
        
        :param huntgroup_name: 
        :param user_name: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/huntgroups/users"
        response = requests.post(url=url, params={"key": self.domain_access_token},
                                 json={"huntgroup_name": huntgroup_name,
                                       "user_name": user_name})
        if give_json:
            return response.json()
        else:
            return response.text

    def delete_huntgroup_user(self, huntgroup_name, user_name, give_json=False):
        """
        
        :param huntgroup_name: 
        :param user_name: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
         
        """
        url = Constants.BASE_URL + "/domains/huntgroups/users"
        response = requests.delete(url=url, params={"key": self.domain_access_token,
                                                    "huntgroup_name": huntgroup_name,
                                                    "user_name": user_name})
        if give_json:
            return response.json()
        else:
            return response.text

    def list_huntgroup_user(self, huntgroup_name, give_json=False):
        """
        
        :param huntgroup_name: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
         
        """
        url = Constants.BASE_URL + "domains/huntgroups/users"
        response = requests.delete(url=url, params={"key": self.domain_access_token,
                                                    "huntgroup_name": huntgroup_name})
        if give_json:
            return response.json()
        else:
            return response.text

    def add_admin_to_huntgroup_users(self, huntgroup_name, admin_name, give_json=False):
        """
        
        :param huntgroup_name: 
        :param admin_name: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "/domains/huntgroups/admins"
        response = requests.post(url=url, params={"key": self.domain_access_token},
                                 json={"huntgroup_name": huntgroup_name,
                                       "admin_name": admin_name})
        if give_json:
            return response.json()
        else:
            return response.text

    def delete_huntgroup_admin(self, huntgroup_name, admin_name, give_json=False):
        """
        
        :param huntgroup_name: 
        :param admin_name: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
        
        """
        url = Constants.BASE_URL + "domains/huntgroups/admin"
        response = requests.delete(url=url, params={"key": self.domain_access_token,
                                                    "huntgroup_name": huntgroup_name,
                                                    "admin_name": admin_name})
        if give_json:
            return response.json()
        else:
            return response.text

    def get_huntgroup_admins(self, huntgroup_name, give_json=False):
        """
        
        :param huntgroup_name: 
        :param give_json: Returns Json object as python in-built List/Dictionary if true else returns Json as text
        :return: Json text or Json Object depending upon give_json parameter
         
        """
        url = Constants.BASE_URL + "domains/huntgroups/admins"
        response = requests.get(url=url, params={"key": self.domain_access_token,
                                                 "huntgroup_name": huntgroup_name})
        if give_json:
            return response.json()
        else:
            return response.text
