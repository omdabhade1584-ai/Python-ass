
class Node:
    def __init__(self, value):
        self.left = None
        self.pid = value
        self.right = None


class BST:
    def __init__(self):
        self.rt = None

    def insert(self, rt, value):
        if rt is None:
            return Node(value)
        if value < rt.pid:
            rt.left = self.insert(rt.left, value)
        elif value > rt.pid:
            rt.right = self.insert(rt.right, value)

        return rt

    # inorder
    def inorder(self, rt):
        if rt:
            self.inorder(rt.left)
            print(rt.pid, end=" ")
            self.inorder(rt.right)

    # Search
    def search(self, rt, value):
        if rt is None:
            return False

        if rt.pid == value:
            return True
        elif value < rt.pid:
            return self.search(rt.left, value)
        else:
            return self.search(rt.right, value)

    # min
    def find_min(self, rt):
        while rt.left:
            rt = rt.left
        return rt.pid

    # max
    def find_max(self, rt):
        while rt.right:
            rt = rt.right
        return rt.pid

    # delete
    def delete(self, rt, value):
        if rt is None:
            return rt

        if value < rt.pid:
            rt.left = self.delete(rt.left, value)

        elif value > rt.pid:
            rt.right = self.delete(rt.right, value)

        else:
            if rt.left is None:
                return rt.right

            elif rt.right is None:
                return rt.left

            # Find inorder successor
            temp = rt.right
            while temp.left:
                temp = temp.left

            rt.pid = temp.pid
            rt.right = self.delete(rt.right, temp.pid)

        return rt

    # Preorder Traversal
    def preorder(self, rt):
        if rt:
            print(rt.pid, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder Traversal
    def postorder(self, rt):
        if rt:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.pid, end=" ")


# create an BST object
bst = BST()

# Product ids
ids = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110]

# Create BST
for id in ids:
    bst.rt = bst.insert(bst.rt, id)

# 2. Display ascending order
print("Ascending Order:")
bst.inorder(bst.rt)

# 3. Search product ID 175
print("\n\nSearching Product ID 175:")
if bst.search(bst.rt, 175):
    print("Product ID 175 exists.")
else:
    print("Product ID 175 does not exist.")

# 4. Delete product ID 100
bst.rt = bst.delete(bst.rt, 100)
print("\nAfter deleting Product ID 100:")

# 5. Display all traversals
print("\nInorder Traversal:")
bst.inorder(bst.rt)

print("\nPreorder Traversal:")
bst.preorder(bst.rt)

print("\nPostorder Traversal:")
bst.postorder(bst.rt)

# 6. Find minimum and maximum
print("\n\nMinimum Product ID:", bst.find_min(bst.rt))
print("Maximum Product ID:", bst.find_max(bst.rt))
