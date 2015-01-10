__author__ = 'Johannes'
from SwankRatsWebSocketClient import SwankRatsWebSocketClient

if __name__ == '__main__':
    try:
        ws = SwankRatsWebSocketClient('ws://192.168.43.177:2000')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()  