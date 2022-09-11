"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#TC - O(N)
#SC - O(N)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        q = deque()
        res = []
        q.append(root)
        while q and root:
            size = len(q)
            t = []
            while size!=0:
                node = q.popleft()
                t.append(node.val)
                for child in node.children:
                    q.append(child)
                
                size-=1
            res.append(t)
        return res