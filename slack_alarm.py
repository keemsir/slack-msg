import slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def slack_msg(token:str, channel_id:str):

    slack_token = token # input token
    client = slack_sdk.WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(
            channel=channel_id, # channel id
            text='Task is completed. :thumbsup:'
        )
    except SlackApiError as e:
        assert e.response["error"]
