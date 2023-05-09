class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
class BST(object):
    def __init__(self, root):
        self.root=Node(root)
    def insert(self,new_val):
        self.insert_help(self.root, new_val)
    def insert_help(self, cur, new_val):
        if cur.data< new_val:
            if cur.right:
                self.insert_help(cur.right, new_val)
            else:
                cur.right = Node(new_val)
        else:
            if cur.left:
                self.insert_help(cur.left, new_val)
            else:
                cur.left = Node(new_val)

    def search(self,find_val):
        return self.search_help(self.root, find_val)
    def search_help(self,cur,find_val):
        if cur:
            if cur.data == find_val:
                return True
            elif cur.data < find_val:
                return self.search_help(cur.right, find_val)
            else:
                return self.search_help(cur.left, find_val)
        else:
            return False
bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))