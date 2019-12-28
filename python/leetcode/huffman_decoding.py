"""https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies. More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords. All edges along the path to a character contain a code digit. If they are on the left side of the tree, they will be a 0 (zero). If on the right, they'll be a 1 (one). Only the leaves will contain a letter and its frequency count. All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its descendant characters.
"""

def decodeHuff(root, s):
    """just follow the instructions... 
    1 -> right, 0 -> left, if node is leaf return to root
    """
    # set-up...
    is_leaf = lambda node: not node.left and not node.right
    # string builder...
    message = []
    current_node = root
    for i,e in enumerate(s):
        if e: current_node = current_node.right
        else: current_node = current_node.left
        if is_leaf(current_node):
            message.append(current_node.data)
            current_node = root
    return print(''.join(message))
