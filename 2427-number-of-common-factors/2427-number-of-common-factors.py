class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        afactors = set()
        bfactors = set()
        for potentialfactor in range(1, a+1):
            if a % potentialfactor == 0:
                afactors.add(potentialfactor)
        for potentialfactor in range(1, b+1):
            if b % potentialfactor == 0:
                bfactors.add(potentialfactor)
        return len(afactors.intersection(bfactors))