from dataclasses import dataclass
from datetime import datetime
import requests

from typing import List


@dataclass(init=True, repr=True)
class BannedPlayer:
    order: str
    created: datetime
    expires: datetime
    name: str
    reason: str
    source: str
    uuid: str


class BanList:
    ban_list_url: str | bytes = "https://dreammc.su/banlist/banlist.php"

    def __init__(self) -> None:
        self.ban_list = []
        self.update()

    def update(self) -> None:
        resp = requests.get(self.ban_list_url)
        if resp.status_code != 200:
            return
        self.ban_list.clear()
        raw_data = resp.json()
        last_order = len(raw_data)
        for i, pl in zip(range(last_order), raw_data):
            order = i + 1
            created = datetime.fromisoformat(pl["created"].replace("+0500", "+05:00"))
            expires = datetime.max if pl["expires"] == "forever" \
                else datetime.fromisoformat(pl["expires"].replace("+0500", "+05:00"))
            name, reason, source, uuid = pl["name"], pl["reason"], pl["source"], pl["uuid"]
            self.ban_list.append(BannedPlayer(order, created, expires, name, reason, source, uuid))

    def get_page(self, page: int, page_size: int = 10) -> List[BannedPlayer]:
        self.update()
        page = page - 1
        start_index = page_size * page
        stop_index = start_index + page_size if start_index + page_size <= len(self.ban_list) else len(self.ban_list)
        return self.ban_list[start_index:stop_index]

    def get_by_index(self, index: int):
        self.update()
        return self.ban_list[index - 1]


if __name__ == '__main__':
    from pprint import pprint

    b = BanList()
    pprint(b.get_page(1))
