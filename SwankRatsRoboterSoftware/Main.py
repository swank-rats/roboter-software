__author__ = 'Johannes'
from SwankRatsWebSocketClient import SwankRatsWebSocketClient
import ConfigParser

if __name__ == '__main__':
    try:
        global Config
        Config = ConfigParser.ConfigParser()
        Config.read("./config.ini")

        address = Config.get("server", "address")
        print address
        ws = SwankRatsWebSocketClient(address)
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
