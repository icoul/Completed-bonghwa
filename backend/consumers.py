from channels.generic.websocket import WebsocketConsumer
import json

class UserConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass
