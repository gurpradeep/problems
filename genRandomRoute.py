import random
class Uber:
    def __init__(self, metrics):

        self.cum_sums = []
        cum_sum = 0
        for metric in metrics:
            cum_sum += metric
            self.cum_sums.append(cum_sum)
        self.total_sum = cum_sum

    def pick_route(self):
        target = self.cum_sums[-1] * random.random()
        
        # Binary search to find the target
        low, high = 0, len(self.cum_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.cum_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Driver code
uber = Uber([1, 2, 3])

for i in range(10):
    print("Randomly choose route", uber.pick_route())