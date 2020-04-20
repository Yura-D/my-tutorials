
import json
import requests
import yaml

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models import Tutorial, Category


with open('conf.yaml', 'r') as yamlfile:
    config = yaml.load(yamlfile)


TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = config['telegram_bot_token']


# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/
class TutorialBotView(View):
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
            tutorial_list = Tutorial.objects.values_list(
                'name',
                'link',
                'category__name',
                'comment'
            ).order_by('category')

            tutorial_list = ['\n'.join(t) for t in tutorial_list if t]
            msg = '\n\n'.join(tutorial_list)
            
            self.send_message(msg, t_chat["id"])
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
