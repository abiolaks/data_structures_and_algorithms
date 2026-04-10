"""
Intuition
My first thought is to have a for loop and a nested for loop, that will loop through the arrays and sum up the values,
then check if the result result equal to the target, is yes i return this two index as a list.

Approach
doning the above will take a take time complexity of O(n2) since i am looping each element twice one by one.

The approach i took is to create a hash map that will help store the value and index.
Then look over the nums array using an enumerate function which allows us to the index and the value of the array.
Then have a variable that substract the target from the value of the current index in the for loop.
Then check if the variable (which will serve as key for the hash map) is in the hash map already.
if yes, we return a list containing the key of the variable in the hashmap and
the loop index but not we just assign the add a key value pair of the value and the couter to the hash map

Complexity
Time complexity:
O(1)

Space complexity:
O(n)

"""

from typing import List


# code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Example 1: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(
        f"Explanation: nums[{result1[0]}] + nums[{result1[1]}] = {nums1[result1[0]]} + {nums1[result1[1]]} = {target1}\n"
    )

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Example 2: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(
        f"Explanation: nums[{result2[0]}] + nums[{result2[1]}] = {nums2[result2[0]]} + {nums2[result2[1]]} = {target2}\n"
    )

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Example 3: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(
        f"Explanation: nums[{result3[0]}] + nums[{result3[1]}] = {nums3[result3[0]]} + {nums3[result3[1]]} = {target3}"
    )
