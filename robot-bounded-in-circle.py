class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        endpos = [0, 0]
        enddir = 0

        direction = [[0,1],[-1,0],[0,-1],[1,0]]
        dirv = 0
        for instruction in instructions:
            if instruction == "G":
                if dirv < 0:
                    endpos[0] += direction[3 - ((abs(dirv) - 1) % 4)][0]
                    endpos[1] += direction[3 - ((abs(dirv) - 1) % 4)][1]
                else:
                    endpos[0] += direction[dirv % 4][0]
                    endpos[1] += direction[dirv % 4][1]                 
            elif instruction == "L":
                dirv += 1
            elif instruction == "R":
                dirv -= 1
        # print(endpos. dirv)
        if endpos == [0, 0]:
            return True
        
        if dirv < 0:
            if 3 - ((abs(dirv) - 1) % 4) != 0:
                return True
        else:
            if dirv % 4 != 0:
                return True
        return False