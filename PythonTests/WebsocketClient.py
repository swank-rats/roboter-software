from ws4py.client.threadedclient import WebSocketClient
import Adafruit_BBIO.GPIO as GPIO



class DummyClient(WebSocketClient):
    def opened(self):
        GPIO.setup("USR3", GPIO.OUT)


        for i in range(0, 200, 25):
            self.send("#" * i)

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, m):
        print m
        if len(m) == 175:
            self.close(reason='Bye bye')

        if len(m) == 100:
             GPIO.output("USR3", GPIO.HIGH)


if __name__ == '__main__':
    try:
        ws = DummyClient('ws://echo.websocket.org', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()