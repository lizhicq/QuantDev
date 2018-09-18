class Solution(object):

    def houseRobber3(self, root):

        def helper(node): # return [without node val, with node val]
            if node is None:
                return [0, 0]

            left, right = helper(node.left), helper(node.right)
            return [max(left) + max(right),
                    left[0] + right[0] + node.val]

        return max(helper(root))
