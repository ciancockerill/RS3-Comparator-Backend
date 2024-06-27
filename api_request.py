import requests


def requestPlayerData(name):
    response = requests.get(
        "https://apps.runescape.com/runemetrics/profile/profile?user=" + name + "&activities=20"
    )

    response = response.json()

    if "error" in response:
        return None

    return response


class RequestAPI:
    def __init__(self, name):
        self.playerData = requestPlayerData(name)

    def getPlayerData(self):
        return self.playerData
