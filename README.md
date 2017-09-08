# Plurk API

This provides a simple OAuth wrapper for [Plurk 2.0 API](https://www.plurk.com/API#/APP/Timeline/getUnreadPlurks). Note that this is **NOT** a full wrapper of the API.

## Getting Started
### Register your app
1. Register your app [here](https://www.plurk.com/PlurkApp/register) or manage your apps [here](https://www.plurk.com/PlurkApp/).
2. Copy your app key and app secret.

### Install library
```
pip install plurk-api
```

### Get user access token
```python
from plurk-api import PlurkOAuthApi


api = PlurkOAuthApi("<App Key>", "<App Sercet>")
request_token = api.request_token()
authorization_url = api.authorization_url(request_token)

# Let the user give you back the verifier

access_token = api.access_token(request_token, "<verifier>")
```

### Access API
```python
from plurk-api import PlurkApi


api = PlurkApi("<App Key>", "<App Sercet>", access_token["oauth_token"], access_token["oauth_token_secret"])
response = api.request("/APP/Profile/getPublicProfile", {"user_id": 12345})
```

## API Documentation
Documentation is avaiable [here](https://www.plurk.com/API).