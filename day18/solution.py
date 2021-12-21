test = [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]

class BinaryTreeNode:
    def __init__(self, data, level, parent=None):
        if isinstance(data, int):
            self.data = data
        else:
            self.data = None
        self.left = None
        self.right = None
        self.level = level
        self.parent = parent

def create_tree(left, right, node, depth):
    if node == None:
        node = BinaryTreeNode([], depth)
    
    node.left = BinaryTreeNode(left, depth+1, node)
    node.right = BinaryTreeNode(right, depth+1, node)
        
    if left != None and not isinstance(left, int):
        create_tree(left[0], left[1], node.left, depth+1)
    if right != None and not isinstance(right, int):
        create_tree(right[0], right[1], node.right, depth+1)
    return node

def increment_levels(node):
    node.level += 1
    if isinstance(node.data, int):
        return
    increment_levels(node.left)
    increment_levels(node.right)

def snail_addition(number1, number2):
    addition_node = BinaryTreeNode(None, 0)
    increment_levels(number1)
    increment_levels(number2)
    addition_node.left = number1
    addition_node.right = number2
    return addition_node

test = [[[[1,2],[3,4]],[[5,6],[7,8]]],9]
node = create_tree(test[0], test[1], None, 0)

s1 = [[[[[9,8],1],2],3],4]
s2 = [[1,9],[8,5]]
node1 = create_tree(s1[0], s1[1], None, 0)
node2 = create_tree(s2[0], s2[1], None, 0)
nodeA = snail_addition(node1, node2)