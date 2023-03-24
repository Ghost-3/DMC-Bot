class Cravatar:
    base_url: str = "http://cravatar.eu/{endpoint}/{nickname}/{size}"

    def avatar(self, nickname: str, size: int = 512):
        return self.base_url.format(endpoint="avatar", nickname=nickname, size=size)

    def helm_avatar(self, nickname: str, size: int = 512):
        return self.base_url.format(endpoint="helmavatar", nickname=nickname, size=size)

    def head(self, nickname: str, size: int = 512):
        return self.base_url.format(endpoint="head", nickname=nickname, size=size)

    def helm_head(self, nickname: str, size: int = 512):
        return self.base_url.format(endpoint="helmhead", nickname=nickname, size=size)



