"""https://www.hackerrank.com/challenges/tree-top-view/problem
You are given a pointer to the root of a binary tree. Print the top view of the binary tree.
Top view means when you look the tree from the top the nodes, what you will see will be called the top view of the tree. See the example below.
"""
def topView(root):
    """we keep track of the index in a hashmap
    keep an index of how the horizontal
    position in the tree and a level for the vertical one
    """
    index = dict()
    def traverse(node, p=0, level=0):
        if not node: return
        if p not in index:
            index[p] = (node.info, level)
        else:
            old_node, old_level = index[p]
            if level < old_level: index[p] = (node.info, level)
        traverse(node.left, p-1, level+1)
        traverse(node.right, p+1, level+1)
    traverse(root)
    res = list(sorted(index.items()))
    res = [str(v[0]) for k, v in res]
    print(' '.join(res))
