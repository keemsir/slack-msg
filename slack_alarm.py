import slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def slack_msg(token:str, channel_id:str):
    
    # token: input token id
    # channel_id: input channel id

    slack_token = token
    client = slack_sdk.WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text='Task is completed. :thumbsup:'
        )
    except SlackApiError as e:
        assert e.response["error"]
