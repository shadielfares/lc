class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines) == 0:
#Must be a legal number as it would have already been ruled out otherwise.
            running_imbalance, moves = 0, 0
            target = sum(machines) // len(machines)
            for dresses in machines:
                delta = dresses - target
                running_imbalance += delta
                moves = max(moves, abs(running_imbalance), delta)
            return moves
        else:
            return -1