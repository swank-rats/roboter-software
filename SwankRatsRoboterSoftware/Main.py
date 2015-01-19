__author__ = 'Johannes'
from SwankRatsWebSocketClient import SwankRatsWebSocketClient

import RobotConfig


def getAddress():
    ssl = RobotConfig.Config.getboolean("server", "ssl")
    ip = RobotConfig.Config.get("server", "ip")
    port = RobotConfig.Config.get("server", "port")

    schema = "ws"
    if ssl:
        schema = "wss://"

    if RobotConfig.Config.getboolean("authentication", "enabled"):
        username = RobotConfig.Config.get("authentication", "username")
        password = RobotConfig.Config.get("authentication", "password")

        return schema + "://" + username + ":" + password + "@" + ip + ":" + port

    return schema + "://" + ip + ":" + port


if __name__ == '__main__':
    try:
        address = getAddress()
        print address
        ws = SwankRatsWebSocketClient(address)
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
