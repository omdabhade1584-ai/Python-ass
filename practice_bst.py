
class Node:
    def __init__(self, value):
        self.left = None
        self.bid = value
        self.right = None


class BST:
    def __init__(self):
        self.rt = None

    def insert(self, rt, value):
        if rt is None:
            return Node(value)

        if value < rt.bid:
            rt.left = self.insert(rt.left, value)
        elif value > rt.bid:
            rt.right = self.insert(rt.right, value)

        return rt

    # Inorder
    def inorder(self, rt):
        if rt:
            self.inorder(rt.left)
            print(rt.bid, end=" ")
            self.inorder(rt.right)

    # Search
    def search(self, rt, value):
        if rt is None:
            return False

        if rt.bid == value:
            return True
        elif value < rt.bid:
            return self.search(rt.left, value)
        else:
            return self.search(rt.right, value)

    # Minimum
    def find_min(self, rt):
        while rt.left:
            rt = rt.left
        return rt.bid

    # Maximum
    def find_max(self, rt):
        while rt.right:
            rt = rt.right
        return rt.bid

    # Delete
    def delete(self, rt, value):
        if rt is None:
            return rt

        if value < rt.bid:
            rt.left = self.delete(rt.left, value)

        elif value > rt.bid:
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

            rt.bid = temp.bid
            rt.right = self.delete(rt.right, temp.bid)

        return rt

    # Preorder
    def preorder(self, rt):
        if rt:
            print(rt.bid, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder
    def postorder(self, rt):
        if rt:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.bid, end=" ")


# Create BST object
bst = BST()

# Book IDs
ids = [50, 30, 70, 20, 40, 60, 80, 10, 35, 65]

# Create BST
for id in ids:
    bst.rt = bst.insert(bst.rt, id)

# Display ascending order
print("Ascending Order:")
bst.inorder(bst.rt)

# Search book ID 60
print("\n\nSearching Book ID 60:")
if bst.search(bst.rt, 60):
    print("Book ID 60 exists.")
else:
    print("Book ID 60 does not exist.")

# Delete book ID 30
bst.rt = bst.delete(bst.rt, 30)

print("\nAfter deleting Book ID 30:")

# Inorder traversal
print("\nInorder Traversal:")
bst.inorder(bst.rt)

# Preorder traversal
print("\nPreorder Traversal:")
bst.preorder(bst.rt)

# Postorder traversal
print("\nPostorder Traversal:")
bst.postorder(bst.rt)

# Minimum and Maximum
print("\n\nMinimum Book ID:", bst.find_min(bst.rt))
print("Maximum Book ID:", bst.find_max(bst.rt))
