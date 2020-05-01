import json
import dice


def CreateNPC():
    """Returns a tuple representing NPC (class, level, alignment)"""

    strJson = ""

    with open("data/npc.json", "r") as inFile:
        strJson = inFile.read()
    # The way the JSON is formatted, it creates a dictionary w/key of 'xxxtables'
    # which will have a list of the tables (which are dictionaries themselves). I just want that list.
    tables = json.loads(strJson)['npctables']
    
    # NPC Class
    table = [tbl for tbl in tables if tbl['name'] == 'Class'][0]
    d = table['dtype']
    npcClass = table['entries'][str(sum(dice.roll('1d' + str(d))))]

    # NPC Level
    table = [tbl for tbl in tables if tbl['name'] == 'Level'][0]
    d = table['dtype']
    npcLevel = table['entries'][str(sum(dice.roll('1d' + str(d))))]

    # NPC Alignment
    table = [tbl for tbl in tables if tbl['name'] == 'Alignment'][0]
    d = table['dtype']
    npcAlign = table['entries'][str(sum(dice.roll('1d' + str(d))))]

    return (npcClass, npcLevel, npcAlign)

