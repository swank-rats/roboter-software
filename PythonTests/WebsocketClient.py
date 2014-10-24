from ws4py.client.threadedclient import WebSocketClient
import Adafruit_BBIO.GPIO as GPIO



class DummyClient(WebSocketClient):
    P = "GPIO8_10"
    def opened(self):
        GPIO.setup(P, GPIO.OUT)
        PIO.output(P, GPIO.LOW)

        for i in range(0, 200, 25):
            self.send("#" * i)

    def closed(self, code, reason=None):
        GPIO.cleanup()
        print "Closed down", code, reason

    def received_message(self, m):
        print m

        if len(m) == 175:
            self.close(reason='Bye bye')

        if len(m) == 100:
            GPIO.output(P, GPIO.HIGH)
            print "should be HIGH"


if __name__ == '__main__':
    try:
        ws = DummyClient('ws://echo.websocket.org', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
