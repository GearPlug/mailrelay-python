from typing import Optional
from urllib import response
from urllib.parse import urlencode
import exceptions
import json
import requests


class Client(object):
    def __init__(self, api_key, domain):
        self.api_key = api_key
        self.base_url = f"https://{domain}/api/v1/"        

    def _compose_endpoint(self, endpoint, id=None):
        if id:
            url = self.base_url+endpoint+"/{id}".format(id=id)
        else:
            url = self.base_url+endpoint
        return url

    def get_subscribers(self)-> list:
        """Return Subscribers data

        Returns:
            list: 
            [
                {
                    "id": 1,
                    "email": "juantest@gmail.com",
                    "name": "juan",
                    "score": None,
                    "status": "active",
                    "subscribed_at": None,
                    "subscribed_with_acceptance": False,
                    "subscribe_ip": None,
                    "unsubscribed": False,
                    "unsubscribed_at": None,
                    "unsubscribe_ip": None,
                    "unsubscribe_sent_email_id": None,
                    "address": "",
                    "city": "",
                    "state": "",
                    "country": "",
                    "birthday": None,
                    "website": "",
                    "time_zone": "",
                    "locale": "",
                    "bounced": False,
                    "reported_spam": False,
                    "local_ban": False,
                    "global_ban": False,
                    "created_at": "2022-05-11T22:15:02.000Z",
                    "updated_at": "2022-05-11T22:15:02.000Z",
                    "custom_fields": {},
                },
            ]
        """        
        url = self._compose_endpoint("subscribers")
        return self._get(url=url)

    def get_subscriber_by_id(self, id:int)-> dict:
        """Get subscriber by id

        Args:
            id (int): _description_

        Returns:
            dict: _description_
        """
        url = self._compose_endpoint(endpoint="subscribers", id=id)    
        return self._get(url=url)

    def create_subscriber(self, data)-> response:
        url = self._compose_endpoint("subscribers")
        return self._post(url=url, json=data)

    def _get(self, url, **kwargs):
        return self._request("GET", url, **kwargs)

    def _post(self, url, **kwargs):
        return self._request("POST", url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request("PUT", url, **kwargs)

    def _patch(self, url, **kwargs):
        return self._request("PATCH", url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request("DELETE", url, **kwargs)

    def _request(self, method, url, headers=None, **kwargs):
        _headers = {
            "X-AUTH-TOKEN": "{}".format(self.api_key),
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if headers:
            _headers.update(headers)
        return self._parse(requests.request(method, url, headers=_headers, **kwargs))

    def _parse(self, response):

        status_code = response.status_code

        if "Content-Type" in response.headers and "application/json" in response.headers["Content-Type"]:
            r = response.json()
        else:
            r = response.content

        if status_code in (200, 201, 202, 204, 206):
            return r
        elif status_code == 400:
            raise exceptions.BadRequest(r)
        elif status_code == 401:
            raise exceptions.Unauthorized(r)
        elif status_code == 403:
            raise exceptions.Forbidden(r)
        elif status_code == 404:
            raise exceptions.NotFound(r)
        elif status_code == 405:
            raise exceptions.MethodNotAllowed(r)
        elif status_code == 406:
            raise exceptions.NotAcceptable(r)
        elif status_code == 409:
            raise exceptions.Conflict(r)
        elif status_code == 410:
            raise exceptions.Gone(r)
        elif status_code == 411:
            raise exceptions.LengthRequired(r)
        elif status_code == 412:
            raise exceptions.PreconditionFailed(r)
        elif status_code == 413:
            raise exceptions.RequestEntityTooLarge(r)
        elif status_code == 415:
            raise exceptions.UnsupportedMediaType(r)
        elif status_code == 416:
            raise exceptions.RequestedRangeNotSatisfiable(r)
        elif status_code == 422:
            raise exceptions.UnprocessableEntity(r)
        elif status_code == 429:
            raise exceptions.TooManyRequests(r)
        elif status_code == 500:
            raise exceptions.InternalServerError(r)
        elif status_code == 501:
            raise exceptions.NotImplemented(r)
        elif status_code == 503:
            raise exceptions.ServiceUnavailable(r)
        elif status_code == 504:
            raise exceptions.GatewayTimeout(r)
        elif status_code == 507:
            raise exceptions.InsufficientStorage(r)
        elif status_code == 509:
            raise exceptions.BandwidthLimitExceeded(r)
        else:
            if r["error"]["innerError"]["code"] == "lockMismatch":
                # File is currently locked due to being open in the web browser
                # while attempting to reupload a new version to the drive.
                # Thus temporarily unavailable.
                raise exceptions.ServiceUnavailable(r)
            raise exceptions.UnknownError(r)


if __name__ == "__main__":
    API_KEY = ""
    DOMAIN = ""
    client = Client(API_KEY, DOMAIN)
    # campaigns = client.get_sent_campaigns(sender_id_eq=2)
    # campaign = client.get_campaigns()
    d = {
        "status": "active",
        "email": "johanntest@example.com",
        "name": "johann",
        "address": "calle",
        "city": "buga",
        "state": "valle",
        "country": "CO",
        "birthday": "1970-01-01",
        
        "locale": "en",
        "time_zone": "",
        "group_ids": [1],
    }
    
    print(d)
    campaign = client.create_subscriber(d)
    #campaign = client.get_subscribers()
    #campaign = client.get_subscriber_by_id(id=1)
    print(campaign)
