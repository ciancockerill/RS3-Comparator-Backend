import api_request

skillDictionary = {
    0: "Attack",
    1: "Defence",
    2: "Strength",
    3: "Constitution",
    4: "Ranged",
    5: "Prayer",
    6: "Magic",
    7: "Cooking",
    8: "Woodcutting",
    9: "Fletching",
    10: "Fishing",
    11: "Firemaking",
    12: "Crafting",
    13: "Smithing",
    14: "Mining",
    15: "Herblore",
    16: "Agility",
    17: "Thieving",
    18: "Slayer",
    19: "Farming",
    20: "Runecrafting",
    21: "Hunter",
    22: "Construction",
    23: "Summoning",
    24: "Dungeoneering",
    25: "Divination",
    26: "Invention",
    27: "Archaeology",
    28: "Necromancy",
}


class DataProcessor:
    def __init__(self, data):
        self.originalData = data
        self.formattedData = None

        if self.originalData is None:
            self.constructErrorTable()
        else:
            self.constructPlayerTable()

    def constructErrorTable(self):
        self.formattedData = {
            "status": "error",
            "message": "Player Not Found or Player is Private"
        }

    def constructPlayerTable(self):
        self.formattedData = {
            "name": self.originalData["name"],
            "totalskill": self.originalData["totalskill"],
            "totalxp": self.originalData["totalxp"],
            "completedquests": self.originalData["questscomplete"],
            "skills": self.getOrganizedSkills()
        }

    def getOrganizedSkills(self):
        skillsList = {}

        for skill in self.originalData["skillvalues"]:
            skillName = str(skillDictionary[skill["id"]])
            skillLevel = skill["level"]
            skillXP = int(skill["xp"]) / 10.0

            skillsList[skillName] = {
                "level": skillLevel,
                "xp": skillXP
            }

        return skillsList

    def getFormattedData(self):
        return self.formattedData
