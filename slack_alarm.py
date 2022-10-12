import slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def slack_msg(TOKEN:str, CH:str, MSG:str='Task is completed. :thumbsup:'):
    
    # TOKEN: input the token
    # CH: input the channel id
    # MSG: input the massage, default: 'Task is completed. :thumbsup:'

    slack_token = TOKEN
    client = slack_sdk.WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(
            channel=CH,
            text=MSG
        )
    except SlackApiError as e:
        assert e.response["error"]
