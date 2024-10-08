'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def main(nums, target):
    hash_map = {}
    counter = 0
    for i in nums:
        if target - i in hash_map:
            print([hash_map[target - i], counter])
        else:
            hash_map[i] = counter
            counter = counter + 1

if __name__ == "__main__":
    #main([2,7,11,15], 9)
    main([3,2,4], 6)