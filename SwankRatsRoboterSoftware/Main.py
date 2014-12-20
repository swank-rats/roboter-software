__author__ = 'Johannes'
from SwankRatsWebSocketClient import SwankRatsWebSocketClient

if __name__ == '__main__':
    try:
        ws = SwankRatsWebSocketClient('ws://echo.websocket.org', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()