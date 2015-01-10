__author__ = 'Johannes'
from SwankRatsWebSocketClient import SwankRatsWebSocketClient
import ConfigParser

if __name__ == '__main__':
    try:
        Config = ConfigParser.ConfigParser()
        Config.read("./config.ini")
        ws = SwankRatsWebSocketClient(Config.get("server", "address"))
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
