import os
import json
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models import Tutorial, Category
from .services import get_all, get_by_category, get_all_categories


TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = os.environ.get('TELEGRAM_TOKE', None)


# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/
class TutorialBotView(View):
    def parsing_to_msg(self, data_list):
        if data_list:
            parsed_item = ['\n'.join(t) for t in data_list if t]
            parsed_obj = '\n\n'.join(parsed_item)
            return parsed_obj
        else:
            return ''

    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]

        try:
            text = t_message["text"].strip().lower()
        except Exception as e:
            return JsonResponse({"ok": "POST request processed"})

        text = text.lstrip("/")
        if text == 'get_all':
            tutorial_list = get_all()
            msg = self.parsing_to_msg(tutorial_list)
        elif text.startswith('get_by_category'):
            category = text.split('get_by_category ')[1]
            tutorial_list = get_by_category(category)
            msg = self.parsing_to_msg(tutorial_list)
        elif text == 'categories':
            category_list = get_all_categories()
            msg = '\n'.join(category_list)
        else:
            msg = "Unknown command"
        self.send_message(msg, t_chat["id"])

        return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage", data=data
        )
