"""
`nums = [1, 2, 3, 4, 5]`
The first time you choose you can either choose 1 or 2 or 3 or 4 or 5. Lets say you choose 2. So the path so far is `[2]`.
The second time you choose you can only choose 1 or 3 or 4 or 5. Lets say you choose 3. So the path so far is `[2, 3]`.
The third time you choose you can only choose 1 or 4 or 5. Lets say you choose 1. So the path so far is `[2, 3, 1]`.
The third time you choose you can only choose 4 or 5...
.
.
.

We put the numbers we can choose in the `options` parameter. And the path so far in the `path` parameter.
In each `dfs()` we check if the path has used up all the numbers in the `nums`. If true. Append it in the output.
If not, we explore all the posible path in the `options` by `dfs()`.

The time complexity is O(N!). Since in this example our choices is 5 at the beginning, then 4, then 3, then 2, then 1.
The space complexity is O(N!), too. And the recursion takes N level of recursion.
"""


class Solution(object):
    def permute(self, nums):
        def dfs(path, options):
            if len(nums) == len(path):
                opt.append(path)
                return
            for i, nums in enumerate(options):
                dfs(path + [nums], options[:i] + options[i + 1:])

        opt = []
        dfs([], nums)
        return opt
