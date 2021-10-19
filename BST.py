class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node({self.value})>'

    def has_children(self):
        return self.left or self.right

    def minimum(self, parent_ref=None):
        if not self.left:
            return self, parent_ref
        else:
            return self.left.minimum(parent_ref=self)

    def maximum(self):
        if not self.right:
            return self
        else:
            return self.right.maximum()

    def successor(self):
        if self.right:
            return self.right.minimum()
        elif self.left:
            return self.left, None
        else:
            return None, None

    def insert(self, new_val):
        if new_val < self.value:
            if not self.left:
                self.left = Node(new_val)
            else:
                self.left.insert(new_val)
        elif new_val > self.value:
            if not self.right:
                self.right = Node(new_val)
            else:
                self.right.insert(new_val)
        else:
            print(f"Duplicate Found: {new_val}")

    def delete(self, del_val, parent_ref=None):
        if del_val < self.value:
            self.left.delete(del_val, parent_ref=(self, 'left'))
        elif del_val > self.value:
            self.right.delete(del_val, parent_ref=(self, 'right'))
        else:
            self.rearrange(parent_ref)

    def rearrange(self, parent_ref):
        succ, succ_parent = self.successor()
        parent, direction = parent_ref

        setattr(parent, direction, succ)

        if succ_parent:
            succ_parent.left = succ.right


class BinaryTree:
    def __init__(self):
        self.root = None

    def print_tree(self, order_type):
        if order_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif order_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif order_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print(f"Traversal type {str(order_type)}  is not supported.")
            return False

    def preorder_print(self, start, order):
        # root - left - right
        if start:
            order += (str(start.value) + "-")
            order = self.preorder_print(start.left, order)
            order = self.preorder_print(start.right, order)
        return order

    def inorder_print(self, start, order):
        # Left-Root-Right
        if start:
            order = self.inorder_print(start.left, order)
            order += (str(start.value) + "-")
            order = self.inorder_print(start.right, order)
        return order

    def postorder_print(self, start, order):
        # Left-Right-Root
        if start:
            order = self.postorder_print(start.left, order)
            order = self.postorder_print(start.right, order)
            order += (str(start.value) + "-")
        return order

    def maximum(self):
        return self.root.maximum().value

    def minimum(self):
        return self.root.minimum()[0].value

    def insert(self, new_val):
        if self.root is None:
            self.root = Node(new_val)
        else:
            self.root.insert(new_val)

    def delete(self, del_val):
        self.root.delete(del_val)


test_nums = [2, 4, 8, 5, 6, 10, 1, 7, 3, 9, 21, 19, 18, 20]
tree = BinaryTree()

for i in test_nums:
    tree.insert(i)

print("\n\n\t\tBinary Search Tree Simulator")
print(f"\nNumbers pre-loaded: {', '.join([str(i) for i in test_nums])} In that order.\n\n")

while True:

    print("Choose what you would like to do.\n1) Insert a number\n2) Delete a number\n3) Find the post order"
          "\n4) Find the pre-order\n5) Find the in-order\n6) Find the max number\n7) Quit")
    choice = input("Type the number of the option you would like: ")

    if choice == "1":
        num = int(input("Enter the number you would like to insert: "))
        tree.insert(num)
        print("In Order of this tree after inserting is as follows: ", tree.print_tree("inorder"))
    if choice == "2":
        num = int(input("Enter the number you would like to delete: "))
        tree.delete(num)
        print("In Order of this tree after deleting is as follows: ", tree.print_tree("inorder"))
    if choice == "3":
        print("Post Order of this tree is as follows: ", tree.print_tree("postorder"))
    if choice == "4":
        print("Pre-Order of this tree is as follows: ", tree.print_tree("preorder"))
    if choice == "5":
        print("In Order of this tree is as follows: ", tree.print_tree("inorder"))
    if choice == "6":
        print("The maximum number in this tree is:", tree.maximum())
    if choice == "7":
        exit()

    more = input("Would you like to do anything else? Y or N\n")
    more = more.upper()

    if more == "N" or more == "NO":
        break
