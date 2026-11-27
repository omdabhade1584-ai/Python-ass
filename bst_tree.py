class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def get_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        # Case 1 & 2: Node with 0 or 1 child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Node with 2 children (find inorder successor)
        temp = get_min_value_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# --- Example Usage ---
if __name__ == "__main__":
    root = None
    values = [50, 30, 20, 40, 70, 60, 80]
    
    for val in values:
        root = insert(root, val)

    print("Inorder traversal (sorted):")
    inorder_traversal(root)  # Output: 20 30 40 50 60 70 80
    print()

    # Search test
    found = search(root, 40)
    print("Search 40:", "Found" if found else "Not Found")

    # Delete test (node with 2 children)
    root = delete(root, 50)
    print("After deleting 50:")
    inorder_traversal(root)  # Output: 20 30 40 60 70 80
