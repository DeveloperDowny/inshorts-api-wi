from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_ApiKeyAuth(api_key, required_scopes):
    return {'test_key': 'test_value'}

def check_BearerAuth(token):
    return {'test_key': 'test_value'}


