__author__ = 'Johannes'
from SwankRatsWebSocketClient import SwankRatsWebSocketClient

import RobotConfig

if __name__ == '__main__':
    try:

        address = RobotConfig.Config.get("server", "address")
        print address
        ws = SwankRatsWebSocketClient(address)
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
