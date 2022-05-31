# python-mailrelay
python-mailrelay is an API wrapper for Mailrelay written in Python.

## Installing
```
pip install mailrelay-python
```
## Before start
To use Mailrelay Python, go user dashboard anf get the API KEY

## Usage
### Client instantiation
```
from mailrelay.client import Client as Client
client = Client((api_key=api_key, url=url))
```

### Mailrelay Workflow
#### Get Groups
```
response = client.get_groups()
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
```

#### Get Campaigns
```
response = client.get_campaigns()

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


```

#### Send Campaigns
```
response = client.send_campaigns(id, data)
```

#### Get Subscribers
```
response = client.get_subscribers()

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
```

#### Get Subscriber by id
```
response = client.get_subscriber_by_id(id)

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
```

#### Create Subscriber
```
response = client.create_subscriber(data)
```
#### Delete Subscriber
```
response = client.delete_subscriber(id)
```

## Requirements
- requests

## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.

#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/mailrelay-python/issues).

#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/mailrelay-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')   
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request