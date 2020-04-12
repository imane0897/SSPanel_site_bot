""" 
Definitions of command handlers
"""
import re
import json
import requests
import session
from info import base_url
from bs4 import BeautifulSoup


def start(update, context):
    """Send a welcome message when start command used"""

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def checkin(update, context):
    """Check in for current user and send check in result when checkin command used"""

    try:
        checkin_url = base_url + "user/checkin"
        checkin = session.login().post(checkin_url)
    except requests.exceptions.RequestException:
        error(update, context)

    result = json.loads(checkin.text)
    message = re.sub("<br/>", '\n', result["msg"])

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def usage(update, context):
    """Query data usage for current use and send usage info when usage command used"""

    try:
        usage_url = base_url
        usage = session.login().get(usage_url)
    except requests.exceptions.RequestException:
        error(update, context)

    result = BeautifulSoup(usage.text).body.findAll('code')
    usage_info = tuple(i.text for i in result)
    message = "用户：%s\n等级：%s\n过期时间：%s\n总流量：%s\n已用流量：%s\n剩余流量：%s" % usage_info

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def error(update, context):
    """Send an error message when requests fails"""

    message = "A network error happend, please try again later"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
