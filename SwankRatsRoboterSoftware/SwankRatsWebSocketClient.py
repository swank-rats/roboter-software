__author__ = 'Johannes'
from ws4py.client.threadedclient import WebSocketClient
from MessageParser import MessageParser


class SwankRatsWebSocketClient(WebSocketClient):


    def opened(self):
        self.parser = MessageParser()

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, m):
        #print m
        self.parser.parse(m)

if __name__ == '__main__':
    try:
        ws = SwankRatsWebSocketClient('ws://echo.websocket.org', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()