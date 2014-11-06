__author__ = 'Johannes'
from SwankRatsWebSocketClient import SwankRatsWebSocketClient

if __name__ == '__main__':
    try:
        ws = SwankRatsWebSocketClient('wss://172.16.50.41:3001', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()