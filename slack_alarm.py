
import slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = '' # input token
client = slack_sdk.WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel='', # channel id
        text='Task is completed. :thumbsup:'
    )
except SlackApiError as e:
    assert e.response["error"]
