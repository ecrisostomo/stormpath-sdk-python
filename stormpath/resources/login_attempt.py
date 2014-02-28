"""Stormpath LoginAttempt resource mappings."""


from base64 import b64encode

from .base import (
    CollectionResource,
    Resource,
)


class AuthenticationResult(Resource):
    """Handles Base64-encoded login data.

    More info in documentation:
    http://docs.stormpath.com/rest/product-guide/#authenticate-an-account
    """

    writable_attrs = ('type', 'value', 'account_store', 'ip_address', 'challenge',)

    def get_resource_attributes(self):
        from .account import Account

        return {
            'account': Account,
        }

    def __repr__(self):
        return '<%s attributes=%s>' % (self.__class__.__name__,
            str(self._get_property_names()))


class LoginAttemptList(CollectionResource):
    """List of login data."""
    resource_class = AuthenticationResult

    def basic_auth(self, login, password, expand, account_store=None, ip_address=None):
        value = login + ':' + password
        value = b64encode(value.encode('utf-8')).decode('ascii')
        properties = {
            'type': 'basic',
            'value': value
        }

        if account_store:
            properties['account_store'] = account_store

        if ip_address:
            properties['ip_address'] = ip_address

        return self.create(properties, expand=expand)
