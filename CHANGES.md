Version 1.0.0
-------------

Released on February 11th, 2014.

- Library no longer in BETA!
- PEP-8 fixes.
- Error object now has a `user_message` attribute, which contains the
  user-friendly error message from the API service.
- Error object's `message` attribute now contains the developer friendly
  message.
- Adding HTTP proxy support to Clients.
- Renaming PyPI package from stormpath-sdk -> stormpath.
- Updating copyright notices.
- Updating PyPI contact information.
- `authenticate_account` no longer returns an account object directly.
- Added support for accountStore specification when authenticating an account.
- Added custom data fields for groups and accounts.
- Added support for login attempt expansion.


Version 1.0.0.beta
------------------

Released on September 26, 2013

- Complete rewrite of codebase
- Support for Python 2.7
- Added self-contained tests
- Account store resources added
- Implemented caching
- Added ability to autocreate directory
- Added entity expansion to create method and tenant resource


Version 0.2.1
-------------

Released on June 27, 2013

- Fixed current tenant redirection handling by adding general redirection support of the Stormpath REST API.


Version 0.2.0
-------------

Released on March 22, 2013

- Implementing Stormpath Digest Authentication (SAuthc1).
- Fixing implementation when no 'base_url' is specified when creating a DataStore.


Version 0.1.1
-------------

Released on March 14, 2013

- Making the 'base_url' an optional argument in the Client class constructor.


Version 0.1.0
-------------

Released on March 14, 2013

- First release of the Stormpath Python SDK where all of the features available on the REST API, before the ones released on February 19th 2013, were implemented.
