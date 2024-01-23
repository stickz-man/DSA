from TreePrint import pretty_tree


class BinarySearchTree:
    # Constructor just assigns an empty root.
    def __init__(self):
        self.root = None

    # Search for a node containing a matching key. Returns the
    # Node object that has the matching key if found, None if
    # not found.
    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node

            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left

            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_node = current_node.right

        # The key was not found in the tree.
        return None

    # Inserts the new node into the tree.
    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

                        # Removes the node with the matching key from the tree.

     
    def remove(self, key):
        # add your code here
        node = self.root
        parent = None
        while node:
            if key == node.key:
                break
            parent = node
            if key<node.key:
                node = node.left
            else:
                node=node.right
            
        if node == None:
            return False
        if node.left is not None and node.right is not None:
            successorNode = node.right
            successorparent = node
            while successorNode.left is not None:
                successorparent = successorNode
                successorNode = successorNode.left
            node.key = successorNode.key
            node = successorNode
            parent = successorparent
        if node.left or node.right:
            child = node.left or node.right
            if not parent:
                self.root = child  # The node is the root
            else:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child

    # Case 3: Node is a leaf (no children)
        if not node.left and not node.right:
            if not parent:
                self.root = None  # The node is the root
            else:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

        return True  # Node not found

    # Build a string representation of the tree by
    # getting the string representation of the root.
    def __str__(self):
        return pretty_tree(self)
