class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {"N":(0,1), "S": (0,-1), "E": (1, 0), "W": (-1, 0)}
        coordinates = (0, 0)
        coordinate_set = set([coordinates])
        for i in path:
            x, y = coordinates
            new_x, new_y = direction[i]
            coordinates = (x + new_x, y + new_y)
            if coordinates in coordinate_set:
                return True
            coordinate_set.add(coordinates)
        return False