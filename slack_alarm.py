import slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def slack_msg(TOKEN:str, CH:str, MSG:str='Task is completed. :thumbsup:'):

    slack_token = TOKEN # input token
    client = slack_sdk.WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(
            channel=CH, # channel id
            text=MSG
        )
    except SlackApiError as e:
        assert e.response["error"]
