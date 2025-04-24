class UniqueSubsets:
    def __init__(self, input_set_param):
        self.input_set = input_set_param
    def get_subsets(self):
        return self._subsets_recursive(sorted(self.input_set))
    def _subsets_recursive(self, nums):
        if not nums:
            return [[]]
        subsets = self._subsets_recursive(nums[1:])
        return subsets + [[nums[0]] + subset for subset in subsets]
if __name__ == "__main__":
    user_input = input("Enter a set of distinct integers separated by spaces: ")
    input_set = set(map(int, user_input.split()))
    unique_subsets = UniqueSubsets(input_set)
    result = unique_subsets.get_subsets()
    print("All possible unique subsets are:")
    for subset in result:
        print(subset)
        
# Enter a set of distinct integers separated by spaces: 2 3 4
# All possible unique subsets are:
# []
# [4]
# [3]
# [3, 4]
# [2]
# [2, 4]
# [2, 3]
# [2, 3, 4]
