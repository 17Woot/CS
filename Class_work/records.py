class PlayerRecord(object):
    def __init__(self):
        self.player_number = None
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.position = None
        self.injured = None

if __name__ == "__main__":
    first_team = []
    for i in range(1,12):
        player = PlayerRecord()
        player.player_number = i
        player.first_name = "first_name" + str(i)
        player.last_name = "last_name" + str(i)
        player.date_of_birth = "date_of_birth" + str(i)
        player.position = "position" + str(i)
        player.injured = "injured" + str(i)
        first_team.append(player)

    for player in first_team:
        print(player.player_number)
        print(player.first_name)
        print(player.last_name)
        print(player.date_of_birth)
        print(player.position)
        print(player.injured)
        print()


    

