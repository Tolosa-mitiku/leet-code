class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue, seen = deque([(start, 0)]), {start}      # Ex: start = "AACCGGTT" ;    end = "AAACGGTA"
                                                        #     bank  = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
        while queue:
            s, n = queue.popleft()                      #   n    queue             seen
                                                        #  –––  ––––––––––––––––  –––––––––––––– 
            if s == end: return n                       #   0   [('AACCGGTA', 1)]  {'AACCGGTA', 'AACCGGTT'}
                                                        #
            for i in range(8):                          #   1   [('AAACGGTA', 2),  {'AACCGGTA', 'AACCGGTT',
                for ch in 'ACGT':                       #        ('AACCGCTA', 2)]   'AACCGCTA', 'AAACGGTA'}
                                                        #                           
                    m = s[:i]+ch+s[i+1:]                #   2                       'AACCGCTA', 'AAACGGTA'}
                                                        #   |
                    if m in bank and m not in seen:     # answer    
                        seen.add(m)
                        queue.append((m, n+1))
        return -1