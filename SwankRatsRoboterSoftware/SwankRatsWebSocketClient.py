__author__ = 'Johannes'
from ws4py.client.threadedclient import WebSocketClient
from MessageParser import MessageParser
import RobotConfig
import os

class SwankRatsWebSocketClient(WebSocketClient):
    def opened(self):
        self.form = RobotConfig.Config.get("robot", "form")
        print("opened " + self.form)
        self.parser = MessageParser()
        data = '{"to":"robot", "cmd":"init", "params":{"form":"' + self.form + '"} }'
        self.send(data)

    def closed(self, code, reason=None):
        print "Closed down", code, reason
        os.system("shutdown /r")

    def received_message(self, m):
        print m
        self.parser.parse(m.data)
