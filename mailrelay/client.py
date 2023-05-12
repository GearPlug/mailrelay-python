from mailrelay import exceptions
from urllib import response
import requests


class Client(object):
    def __init__(self, api_key, domain):
        self.api_key = api_key
        if domain.startswith("http://") or domain.startswith("https://"):
            if domain.endswith("/"):
                self.base_url = f"{domain}api/v1/"
            else:
                self.base_url = f"{domain}/api/v1/"

        else:
            self.base_url = f"https://{domain}/api/v1/"

    def _compose_endpoint(self, endpoint, id=None):
        if id:
            url = self.base_url + endpoint + "/{id}".format(id=id)
        else:
            url = self.base_url + endpoint
        return url

    def get_groups(self) -> list:
        """Lists groups.

        Returns:
            list: [
            {
                "id": 1,
                "name": "grupo test 1",
                "description": "",
                "subscribers_count": 3,
                "created_at": "2022-05-11T22:48:18.000Z",
                "updated_at": "2022-05-11T22:48:18.000Z",
            },
            {
                "id": 2,
                "name": "grupo 2",
                "description": "",
                "subscribers_count": 1,
                "created_at": "2022-05-20T15:38:13.000Z",
                "updated_at": "2022-05-20T15:38:13.000Z",
            },
        ]
        """        
        url = self._compose_endpoint("groups")
        return self._get(url=url)
    
    def get_campaigns(self) -> list:
        """Lists campaigns.

        Returns:
            [
                {
                    "id": 0,
                    "subject": "string",
                    "sender_id": 0,
                    "campaign_folder_id": 0,
                    "target": "groups",
                    "segment_id": 0,
                    "group_ids": "string",
                    "preview_text": "string",
                    "html": "string",
                    "editor_type": "html",
                    "url_token": false,
                    "analytics_utm_campaign": "string",
                    "use_premailer": false
                }
            ]
        """
        url = self._compose_endpoint("campaigns")
        return self._get(url=url)

    def send_campaigns(self, id, data:dict) -> dict:
        """This method is used to send a campaign to groups or a specific segment. It will return some attributes, including the ID of the sent campaign which can be used to check the progress and results of the campaign

        Args:
            id (_type_): _description_
            data (dict): {
                            "target": "groups",
                            "group_ids": [
                                0
                            ],
                            "segment_id": 0,
                            "scheduled_at": "1970-01-01T00:00:00.000Z",
                            "callback_url": "string"
                        }
        Returns:
            dict: _description_
        """
        url = self.base_url + "campaigns/{id}/send_all".format(id=id)
        return self._post(url=url, json=data)

    def get_subscribers(self) -> list:
        """Lists all subscribers.

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

    def get_subscriber_by_id(self, id: int) -> dict:
        """Get a subscriber by id

        Args:
            id (int): _description_

        Returns:
            dict: {
                "id": 0,
                "email": "user@example.com",
                "name": "string",
                "score": 0,
                "status": "string",
                "subscribed_at": "1970-01-01T00:00:00.000Z",
                "subscribed_with_acceptance": false,
                "subscribe_ip": "198.51.100.42",
                "unsubscribed": false,
                "unsubscribed_at": "1970-01-01T00:00:00.000Z",
                "unsubscribe_ip": "198.51.100.42",
                "unsubscribe_sent_email_id": 0,
                "address": "string",
                "city": "string",
                "state": "string",
                "country": "string",
                "birthday": "1970-01-01",
                "website": "string",
                "time_zone": "Africa/Abidjan",
                "locale": "en",
                "bounced": false,
                "reported_spam": false,
                "local_ban": false,
                "global_ban": false,
                "created_at": "1970-01-01T00:00:00.000Z",
                "updated_at": "1970-01-01T00:00:00.000Z",
                "groups": [
                    {
                    "group_id": 0,
                    "assigned_at": "1970-01-01T00:00:00.000Z"
                    }
                ],
                "custom_fields": {}
                }
        """
        url = self._compose_endpoint(endpoint="subscribers", id=id)
        return self._get(url=url)

    def create_subscriber(self, data:dict) -> dict:
        """Add a new subscriber

        Note that you should provide the default subscriber status.

        active: use this status if the subscriber has already gone through your opt in process and confirmed that he wants to receive your newsletters.
        inactive: if you use this option, you must use the resend_confirmation_email method to send the confirmation email to the subscriber. Only after clicking at link in the confirmation email, he will be changed to active status and will receive your newsletters.

        Args:
            data (dict): {
                "status": "active",
                "email": "user@example.com",
                "name": "string",
                "address": "string",
                "city": "string",
                "state": "string",
                "country": "string",
                "birthday": "1970-01-01",
                "website": "string",
                "locale": "en",
                "time_zone": "Africa/Abidjan",
                "group_ids": [
                    0
                ]
            }

        Returns:
            dict: {
                    "id": 0,
                    "email": "user@example.com",
                    "name": "string",
                    "score": 0,
                    "status": "string",
                    "subscribed_at": "1970-01-01T00:00:00.000Z",
                    "subscribed_with_acceptance": false,
                    "subscribe_ip": "198.51.100.42",
                    "unsubscribed": false,
                    "unsubscribed_at": "1970-01-01T00:00:00.000Z",
                    "unsubscribe_ip": "198.51.100.42",
                    "unsubscribe_sent_email_id": 0,
                    "address": "string",
                    "city": "string",
                    "state": "string",
                    "country": "string",
                    "birthday": "1970-01-01",
                    "website": "string",
                    "time_zone": "Africa/Abidjan",
                    "locale": "en",
                    "bounced": false,
                    "reported_spam": false,
                    "local_ban": false,
                    "global_ban": false,
                    "created_at": "1970-01-01T00:00:00.000Z",
                    "updated_at": "1970-01-01T00:00:00.000Z",
                    "groups": [
                        {
                        "group_id": 0,
                        "assigned_at": "1970-01-01T00:00:00.000Z"
                        }
                    ],
                    "custom_fields": {}
                }
        """
        url = self._compose_endpoint("subscribers")
        return self._post(url=url, json=data)

    def delete_subscriber(self, id=id) -> response:
        url = self._compose_endpoint("subscribers", id=id)
        return self._delete(url=url)

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

