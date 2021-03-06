from mailjet_rest import Client
from config import MJ_APIKEY_PUBLIC,MJ_APIKEY_PRIVATE 

api_key = MJ_APIKEY_PUBLIC
api_secret = MJ_APIKEY_PRIVATE



def send_email_mj(email,link,location):

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
                    {
                            "From": {
                                    "Email": "openedme@gmail.com",
                                    "Name": "Opened Me"
                            },
                            "To": [
                                    {
                                            "Email": email,
                                            "Name": ""
                                    }
                            ],
                            "Subject": "Your link was opened by someone in %s." % location,
                            "TextPart": """
                                        Your link %s was opened by someone in %s.
                                        Please support Opened Me via Patreon: https://patreon.com/openedme
                                        """ % (link,location),
                            "HTMLPart": ""
                    }
            ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

    return True
