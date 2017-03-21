import json as JSON

import requests

import Constants


class Account:
    api_key = ''
    api_secret = ''

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_access_token(self, give_json=False):
        """
        :param give_json: A boolean type which determines the return type.
         If give_json is true the method returns a json object in python in-built dictionary and List form
         If give_json is false the method return a json string
        :return: json string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + 'accounts/accesstokens'
        response = requests.get(url=url, params={'key': self.api_key, 'account_api_secret': self.api_secret})
        if give_json:
            return response.json()
        else:
            return response.text

    def delete_access_token(self, account_access_token, give_json=False):
        """
        
        :param account_access_token: Account accesstoken to be deleted
        :param give_json: Returns json object as in-built if true else Returns Json object as string
        :return: json string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + 'accounts/accesstokens'
        response = requests.delete(url, params={'key': self.api_key, 'account_api_secret': self.api_secret,
                                                'account_access_token': account_access_token})
        if give_json:
            return response.json()
        else:
            return response.text

    def create_domain(self, account_access_token, domain_name, project_name, give_json=False):
        """
        
        :param domain_name: Name of the domain which is to be created
        :param project_name: Name of the project associated with the domain
        :param give_json: Returns json object as in-built if true else Returns Json object as string
        :return: json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'accounts/domains'
        requestbody = JSON.dumps({'domain_name': domain_name, 'project_name': project_name})
        response = requests.post(url=url, data={'key': self.api_secret}, json=requestbody)

        if give_json:
            return response.json()
        else:
            return response.text

    def delete_domain(self, account_access_token, domain_api_key, give_json=False):
        '''
        :param account_access_token: Account access token (Hint : Use get_access_token() method to get all the relevant data)
        :param domain_api_key: API key of the domain to delete
        :param give_json: Returns json object as in-built if true else Returns Json object as string
        :return: json response string or Object determined by give_json parameter to the method

        '''
        url = Constants.BASE_URL + 'accounts/domains'
        response = requests.delete(url=url, params={'key': account_access_token})

        if give_json:
            return response.json()
        else:
            return response.text

    def get_domain_list(self, account_access_token, give_json=False):
        """
        
        :param account_access_token: Account access token (Hint : Use get_access_token() method on the object to get all the relevant data )
        :param give_json: Returns json object as in-built if true else Returns Json object as string
        :return: json response string or Object determined by give_json parameter to the method

        """
        url = Constants.BASE_URL + 'accounts/domains'
        response = requests.get(url=url, params={'key': account_access_token})

        if give_json:
            return response.json()
        else:
            return response.text
