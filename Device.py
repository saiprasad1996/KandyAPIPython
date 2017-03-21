import json as JSON

import requests

import Constants


class Device:
    device_id = None
    user_access_token = None

    def __init__(self, user_access_token, device_id):
        self.user_access_token = user_access_token
        self.device_id = device_id

    def upload_a_device_addressbook(self, contacts, give_json=False):
        """
        Upload a device address book
        :param contacts: Array of contacts information in json format
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + 'devices/addressbooks'
        requestbody = JSON.dumps({
            "device_id": self.device_id,
            "contacts": []
        })

        data = JSON.loads(requestbody)
        data["contacts"].append(contacts)
        requestbody = JSON.dumps(data)
        response = requests.post(url=url,
                                 params={'key': self.user_access_token, 'device_id': self.device_id}, json=requestbody)
        # print(respone)
        if give_json:
            return response.json()
        else:
            return response.text

    def get_device_addressbook(self, give_json=False):
        """
        Get address book of device with hints
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'devices/addressbooks'
        response = requests.get(url=url,
                                params={'key': self.user_access_token, 'device_id': self.device_id})

        if give_json:
            return response.json()
        else:
            return response.text

    def delete_device_addressbook(self, give_json=False):
        """
        Delete an address book of device
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'devices/addressbooks'
        response = requests.delete(url=url,
                                   params={'key': self.user_access_token, 'device_id': self.device_id})

        if give_json:
            return response.json()
        else:
            return response.text

    def get_hints_for_device_addressbook(self, give_json=False):
        """
        Get only hints from an address book of a device
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'devices/addressbooks/hints'
        response = requests.get(url=url,
                                params={'key': self.user_access_token, 'device_id': self.device_id})

        if give_json:
            return response.json()
        else:
            return response.text

    def send_message(self, device_id, destination, UUID, message_text, give_json=False):
        """
        Send a single message to a single destination
        :param device_id: 
        :param destination: 
        :param UUID: 
        :param message_text: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + 'devices/messages'
        request_body = {
            "message": {
                "content_type": "text",
                "destination": destination,
                "UUID": UUID,
                "message": {
                    "mimeType": "text/plain",
                    "text": message_text
                }
            }
        }
        response = requests.post(url=url, params={"key": self.user_access_token,
                                                  "device_id": device_id},
                                 json=request_body)
        if give_json:
            return response.json()
        else:
            return response.text

    def get_pending_messages(self, device_id, client_timestamp=None, give_json=False):

        url = Constants.BASE_URL + "devices/messages"
        response = requests.get(url=url, params={"device_id": device_id,
                                                 "client_timestamp": client_timestamp})
        if give_json:
            return response.json()
        else:
            return response.text

    def delete_handled_message(self, device_id, messages, give_json=False):
        """
        
        :param device_id: Device ID
        :param messages: JSON array of message IDs to delete
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "devices/messages"
        response = requests.delete(url=url, params={"key": self.user_access_token,
                                                    "device_id": device_id,
                                                    "messages": messages})
        if give_json:
            return response.json()
        else:
            return response.text
