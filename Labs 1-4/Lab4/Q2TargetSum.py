class TargetSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def find_pair(self):
        num_dict = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_dict:
                return (num_dict[complement], i)
            num_dict[num] = i
        return None
if __name__ == "__main__":
    nums = list(map(int, input("Enter the numbers in the array separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))
    ts = TargetSum(nums, target)
    result = ts.find_pair()
    if result:
        print(f"Pair found at indices: {result}")
    else:
        print("No pair found")
# Enter the numbers in the array separated by spaces: 4 5 6 7 1 2 3 4 5 6 7 7 2 5 7
# Enter the target sum: 5
# Pair found at indices: (0, 4)
