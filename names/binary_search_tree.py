import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #  < go left
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # >= go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: self.right.insert(value)



    def contains(self, target):
        if self.value == target:
            return self.value

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can go right no further
        current = self

        while current.right:
        # Keep going right
            if current.right == None:
                return current.value
            else:
                current = current.right
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore, then
        # go back and go right
        # in here somewhere, you want to call cb(node)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if node is None:
            return

        self.in_order_print(node.left)
        # if self.value == node.left.value or self.value == node.right.value:
        print(node.value)
        self.in_order_print(node.right)

"""
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()

        queue.enqueue(node)

        while queue.size != 0:
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()

        stack.push(node)

        while stack.size != 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(2)
# bst.insert(3)
# bst.insert(7)
# # bst.insert(6)
# print(bst.in_order_print(bst))
"""