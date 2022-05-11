from typing import Optional
from urllib.parse import urlencode
import exceptions

import requests


class Client(object):
    def __init__(self, api_key, domain):
        self.headers = {
            "x-auth-token": api_key,
            "cache-control": "max-age=0, private, must-revalidate",
            "content-type": "application/json; charset=utf-8",
        }
        self.base_url = f"https://{domain}/api/v1/"

    def __compose_endpoint(self, endpoint, *endpoints):
        url = self.base_url + endpoint + "/"
        for endpoint in endpoints:
            url += str(endpoint) + "/"
        return url[:-1]

    def __compose_get_query(self, **kwargs):
        """Compose the paramateres for the get payload.
        For queriable parameters
        """
        params = {}
        no_query = ["page", "unique", "include"]
        for key, value in kwargs.items():
            if value:
                is_query = True
                for keyword in no_query:
                    if key in keyword:
                        is_query = False
                if is_query:
                    params[f"q[{key}]"] = value
                else:
                    params[key] = kwargs[key]
        return params

    def __compose_request(self, endpoint, *endpoints, **kwargs):
        """Create a request dictionary to pass to the request function."""
        url = self.__compose_endpoint(endpoint, *endpoints)
        params = self.__compose_get_query(**kwargs)
        req_dict = dict(url=url, params=params, headers=self.headers)
        return req_dict

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
        return self._parse(requests.request(method, url, headers=headers, **kwargs))

    def get_campaigns(self, **kwargs):
        params = locals()
        params.pop("self")
        req_dict = self.__compose_request("campaigns", **kwargs)
        print(req_dict)
        return self._get(**req_dict)

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
    campaign = client.get_campaigns()
    print(campaign)
