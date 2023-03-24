from mcstatus import JavaServer
from mcstatus.pinger import PingResponse
from typing import Union


class ServerStatus:
    favicon_url = "https://eu.mc-api.net/v3/server/favicon/dreammc.su"

    @staticmethod
    def get_status(ip: str = "dreammc.su") -> Union[PingResponse, None]:
        try:
            server = JavaServer.lookup(ip)
            return server.status()
        except TimeoutError:
            return None


if __name__ == '__main__':
    from pprint import pprint
    ss = ServerStatus()
    a = ss.get_status("dreammc.su")
    pprint(a)
