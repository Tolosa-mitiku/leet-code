class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        A = [0] * (n+1)
        for first, last, seats in bookings:
            A[first-1] += seats
            A[last] -= seats
        ans = [0] * n
        curr = 0
        for i in range(len(A)-1):
            curr += A[i]
            ans[i] = curr
        return ans