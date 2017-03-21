import json as JSON
import requests

import Constants


class User:
    api_key = ''
    api_secret = ''
    user_access_token = ''

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_user_access_token(self, user_id, give_json=False):
        """
        Get user Access Token
        :param user_id: user id of the user
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + 'domains/users/accesstokens'
        response = requests.get(url=url,
                                params={'key': self.api_key, 'domain_api_secret': self.api_secret, 'user_id': user_id})
        json_obj = response.json()
        self.user_access_token = json_obj["result"]["user_access_token"]
        if give_json:
            return json_obj
        else:
            return response.text

    def get_user_access_token_alt(self, user_id, user_password, give_json=False):
        """
        Get access token for user
        :param user_id: user id of the user
        :param user_password: password of the user
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'domains/users/accesstokens'
        response = requests.get(url=url,
                                params={'key': self.api_key, 'user_id': user_id, 'user_password': user_password})
        if give_json:
            return response.json()
        else:
            return response.text

    def delete_user_access_token(self, user_id, user_password, user_access_token, give_json=False):
        """
        Revoke user access token
        :param user_id: user id of the user
        :param user_password: password of the user
        :param user_access_token: Access token of user
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'domains/users/accesstokens'
        response = requests.delete(url=url,
                                   params={'key': self.api_key, 'user_id': user_id, 'user_password': user_password})
        if give_json:
            return response.json()
        else:
            return response.text

    def create_device(self, device_native_id, device_family, device_name, client_sw_version, device_os_version,
                      give_json=False):  # please check this one over API docc
        """
        Create a Device
        :param user_access_token:
        :param device_native_id: Native device ID (UDID/IMEI/MAC) in the JSON body
        :param device_family: Device family
        :param device_name: Device name
        :param client_sw_version: Client software version
        :param device_os_version: Client os version
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'users/devices'
        requestbody = JSON.dumps({
            'device_native_id': device_native_id,
            'device_family': device_family,
            'device_name': device_name,
            'client_sw_version': client_sw_version,
            'device_os_version': device_os_version
        })
        response = requests.post(url=url, params={'key': self.user_access_token}, json=requestbody)

        if give_json:
            return response.json()
        else:
            return response.text

    def delete_device(self, device_id, give_json=False):
        """
        Delete an existing domain user
        :param device_id: Device ID of the device
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'users/devices'
        response = requests.delete(url=url, params={'key': self.user_access_token, 'device_id': device_id})

        if give_json:
            return response.json()
        else:
            return response.text

    def get_list_of_devices(self, give_json=False):
        """
        Retrieve list of all user Device
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'users/devices'
        response = requests.get(url=url, params={'key': self.user_access_token})

        if give_json:
            return response.json()
        else:
            return response.text

    def get_user_personal_addressbook(self, give_json=False):
        """
        Retrieve list of all contacts in user personal address book
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'users/addressbooks/personal'
        response = requests.get(url=url, params={'key': self.user_access_token})

        if give_json:
            return response.json()
        else:
            return response.text

    def add_contact_to_personal_addressbook(self, name, nickname, first_name, last_name, home_phone, mobile_number,
                                            business_number, fax, email, image_id, give_json=False):
        """
        Add Contact to user personal address book
        :param name: Contact user name
        :param nickname: Contact nick name
        :param first_name: Contact First name
        :param last_name: Contact Last name
        :param home_phone: Contact home phone number
        :param mobile_number: Contact mobile number
        :param business_number: Contact business number
        :param fax: Contact Fax number
        :param email: Contact email address
        :param image_id: Contact image id
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'users/addressbooks/personal'
        requestbody = JSON.dumps({
            "contact": {
                "name": name,
                "nickname": nickname,
                "first_name": first_name,
                "last_name": last_name,
                "home_phone": home_phone,
                "mobile_number": mobile_number,
                "business_number": business_number,
                "fax": fax,
                "email": email,
                "image_id": image_id
            }
        })
        response = requests.post(url=url, params={'key': self.user_access_token}, json=requestbody)

        if give_json:
            return response.json()
        else:
            return response.text

    def delete_contact_from_personal_addressbook(self, contact_id, give_json=False):
        """
        Delete a contact from user personal address book
        :param contact_id: Contact ID
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'users/addressbooks/personal'
        response = requests.delete(url=url, params={'key': self.user_access_token, 'contact_id': contact_id})

        if give_json:
            return response.json()
        else:
            return response.text

    def get_user_device_addressbooks(self, device_id, give_json=False):
        """
        Returns listing of known Kandy users for domainRetrieve list of all contacts in user device addressbooks
        (combined of all devices, including hints)
        :param device_id: Device ID
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'users/addressbooks/device'
        response = requests.post(url=url, params={'key': self.user_access_token, 'device_id': device_id})

        if give_json:
            return response.json()
        else:
            return response.text
