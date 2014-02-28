"""Stormpath ChallengeToken resource."""

from .base import (
CollectionResource,
Resource,
)

class ChallengeToken(Resource):
    """Handles reset tokens used in password reset workflow.

     Attributes:

    :py:attr:`token` - Token with which to prove the challenge.
    """
    writable_attrs = ('type',)

    def get_resource_attributes(self):
        from .account import Account

        return {
            'account': Account
        }

    @property
    def token(self):
        return self.href.split('/')[-1]

class ChallengeTokenList(CollectionResource):
    """List of challenge tokens."""
    resource_class = ChallengeToken
