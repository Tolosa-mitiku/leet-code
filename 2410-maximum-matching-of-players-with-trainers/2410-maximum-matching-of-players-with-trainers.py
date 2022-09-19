class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        playercount = 0
        trainercount = 0
        ans = 0
        while playercount < len(players) and trainercount < len(trainers):
            if players[playercount] <= trainers[trainercount]:
                ans +=1
                playercount +=1
                trainercount +=1
            else:
                while trainercount < len(trainers) and trainers[trainercount] < players[playercount]:
                    trainercount += 1
        return ans