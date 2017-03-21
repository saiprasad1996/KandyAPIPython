import requests

import Constants


class Groups:
    api_key = None
    group_id = None
    user_access_token = None

    def __init__(self, api_key, group_id, user_access_token):
        """
        
        :param api_key: 
        :param group_id: 
        :param user_access_token: 
        """
        self.api_key = api_key
        self.group_id = group_id
        self.user_access_token = user_access_token

    def get_all_groups(self, give_json=False):
        """
        
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "users/chatgroups"
        response = requests.get(url=url, params={"key": self.user_access_token})
        if give_json:
            return response.json()
        else:
            return response.text

    def create_group(self, group_name=None, group_image=None, give_json=False):
        """
        
        :param group_name: 
        :param group_image: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + "users/chatgroups"
        response = requests.post(url=url, params={"key": self.user_access_token},
                                 json={"group_name": group_name,
                                       "group_image": group_image})
        if give_json:
            return response.json()
        else:
            return response.text

    def get_group_by_id(self, group_id, give_json=False):
        """
        
        :param group_id: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "users/chatgroups/chatgroup"
        response = requests.get(url=url, params={"key": self.user_access_token,
                                                 "group_id": group_id})
        if give_json:
            return response.json()
        else:
            return response.text

    def destory_group(self, group_id, give_json=False):
        """
        
        :param group_id: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "users/chatgroups/chatgroup"
        response = requests.delete(url=url, params={"key": self.user_access_token,
                                                    "group_id": group_id})
        if give_json:
            return response.json()
        else:
            return response.text

    def update_group(self, group_id, group_name, group_image, give_json=False):
        """
        
        :param group_id: 
        :param group_name: 
        :param group_image: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "users/chatgroups/chatgroup"
        response = requests.put(url=url, params={"key": self.user_access_token,
                                                 "group_id": group_id},
                                json={"group_id": group_id, "group_name": group_name,
                                      "group_image": group_image})
        if give_json:
            return response.json()
        else:
            return response.text

    def add_members_to_group(self, group_id, members, give_json=False):
        """
        
        :param group_id: 
        :param members: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "users/chatgroups/chatgroup/members"
        response = requests.post(url=url, params={"group_id": group_id,
                                                  "members": members},
                                 json={"group_id": group_id,
                                       "members": members})
        if give_json:
            return response.json()
        else:
            return response.text

    def remove_members_from_group(self, group_id, members, give_json=False):
        """
        
        :param group_id: 
        :param members: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "users/chatgroups/chatgroup/members"
        response = requests.delete(url=url, params={"key": self.user_access_token,
                                                    "group_id": group_id,
                                                    "members": members})
        if give_json:
            return response.json()
        else:
            return response.text

    def leave_group(self, group_id, give_json=False):

        """
        
        :param group_id: 
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + "users/chatgroups/chatgroup/members/membership"
        response = requests.delete(url=url, params={"key": self.user_access_token,
                                                    "group_id": group_id})
        if give_json:
            return response.json()
        else:
            return response.text


def mute_unmute_group(self, group_id, mute, give_json=False):
    """
    
    :param self: 
    :param group_id: 
    :param mute: 
    :param give_json:Returns json object as in-built if true else Returns Json object as string
    :return:json response string or Object determined by give_json parameter to the method
    """
    url = Constants.BASE_URL + "users/chatgroups/chatgroup/mute"
    response = requests.put(url=url, params={"key": self.user_access_token,
                                             "mute": mute}, json={"group_id": group_id,
                                                                  "mute": mute})
    if give_json:
        return response.json()
    else:
        return response.text


def mute_unmute_members(self, mute, members, group_id, give_json=False):
    """
    
    :param self: 
    :param mute: 
    :param members: 
    :param group_id: 
    :param give_json:Returns json object as in-built if true else Returns Json object as string
    :return:json response string or Object determined by give_json parameter to the method
    """
    url = Constants.BASE_URL + "users/chatgroups/chatgroup/members/mute"
    response = requests.put(url=url, params={"key": self.user_access_token,
                                             "mute": mute,
                                             "members": members},
                            json={"group_id": group_id,
                                  "members": members,
                                  "mute": mute})
    if give_json:
        return response.json()
    else:
        return response.text


def send_message(self, dest_groupid, UUID, text_message, give_json=False):
    """
    
    :param self: 
    :param dest_groupid: 
    :param UUID: 
    :param text_message: 
    :param give_json:Returns json object as in-built if true else Returns Json object as string
    :return:json response string or Object determined by give_json parameter to the method
        
    """
    url = Constants.BASE_URL + 'users/chatgroups/chatgroup/messages'
    message = {
        "message": {
            "contentType": "text",
            "group_id": dest_groupid,
            "UUID": UUID,
            "message": {
                "mimeType": "text/plain",
                "text": text_message
            }
        }
    }
    response = requests.post(url=url, params={"key": self.user_access_token},
                             json=message)
