__author__ = 'Johannes'
from ws4py.client.threadedclient import WebSocketClient
from MessageParser import MessageParser
import RobotConfig

class SwankRatsWebSocketClient(WebSocketClient):
    def opened(self):
        self.form = RobotConfig.Config.get("robot", "form")
        print("opened " + self.form)
        self.parser = MessageParser()
        data = '{"to":"robot", "cmd":"init", "params":{"form":"' + self.form + '"} }'
        self.send(data)

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, m):
        print m
        # data = '{"to":"robot", "cmd":"left"}'
        self.parser.parse(m.data)


if __name__ == '__main__':
    try:
        ws = SwankRatsWebSocketClient('ws://192.168.43.177:2000')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()