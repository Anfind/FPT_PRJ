class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, k): #key < 100
        # =========================================
        # === BEGIN YOUR CODE HERE
        if k >= 100:
            return  
        new_node = Node(k)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if k < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
        # === END YOUR CODE

        # === END YOUR CODE
    
    def print_tree(self, node):
        if node is not None:
            self.print_tree(node.left)
            print(node.key, end=' ')
            self.print_tree(node.right)

    def f1(self, k):
    # =========================================
        # === BEGIN YOUR CODE HERE
        current = self.root
        while current:
            if current.key == k:
                return True
            elif k < current.key:
                current = current.left
            else:
                current = current.right
        return False
        # === END YOUR CODE

    def f2(self):
    # =========================================
        # === BEGIN YOUR CODE HERE
        def height(node):
            if node is None:
                return -1  
            return 1 + max(height(node.left), height(node.right))
        return height(self.root)
        # === END YOUR CODE

    def f3(self): # Count leaves with key > 10
    # =========================================
        # === BEGIN YOUR CODE HERE
        def count_leaves_gt_10(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1 if node.key > 10 else 0
            return count_leaves_gt_10(node.left) + count_leaves_gt_10(node.right)
        return count_leaves_gt_10(self.root)
        # === END YOUR CODE

    def f4(self):
    # =========================================
        # === BEGIN YOUR CODE HERE
        def sum_leaves(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.key
            return sum_leaves(node.left) + sum_leaves(node.right)
        return sum_leaves(self.root)
        # === END YOUR CODE

    def f5(self, k):
    # =========================================
        # === BEGIN YOUR CODE HERE
        if k % 2 == 0:
            self.insert(k)
        return self.f2()
        # === END YOUR CODE
    
    def f6(self):
    # =========================================
        # === BEGIN YOUR CODE HERE
        def height(node):
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))
        if self.root is None:
            return 0
        left_height = height(self.root.left)
        right_height = height(self.root.right)
        return left_height - right_height
        # === END YOUR CODE

        # === END YOUR CODE
        
    def f7(self):
    # =========================================
        # === BEGIN YOUR CODE HERE
        def height(node):
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))
        
        def count_imbalanced(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            imbalanced = 1 if abs(left_height - right_height) > 1 else 0
            return imbalanced + count_imbalanced(node.left) + count_imbalanced(node.right)
        
        return count_imbalanced(self.root)
        # === END YOUR CODE
    def f8(self):
    # =========================================
        # === BEGIN YOUR CODE HERE
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key
        # === END YOUR CODE
        
    def f9(self):
    # =========================================
        # === BEGIN YOUR CODE HERE
        if self.root is None:
            return -1
            
        if self.root.left is None:
            self.root = self.root.right
        else:
            current = self.root
            while current.left.left is not None:
                current = current.left
            current.left = current.left.right
        
        def height(node):
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))
        return height(self.root)
        # === END YOUR CODE

# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    t = BSTree()
    t.insert(5)
    t.insert(3)
    t.insert(10)
    t.insert(20)
    t.insert(14)
    t.insert(7)
    t.insert(2)
    t.insert(40)
    t.insert(6)
    t.insert(8)
    t.insert(100)
    t.insert(200)
    t.insert(300)
    # t.print_tree(t.root)
    print("Do you want to run?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")
    print("6. Run f6()")
    print("7. Run f7()")
    print("8. Run f8()")
    print("9. Run f9()")

    n = int(input("Enter a number : "))

    if n == 1:
        result = t.f1(10)
        print("OUTPUT:")
        print(str(result))

    if n == 2:
        result = t.f2()
        print("OUTPUT:")
        print(result)

    if n == 3:
        result = t.f3()
        print("OUTPUT:")
        print(result)

    if n == 4:
        result = t.f4()
        print("OUTPUT:")
        print(result)

    if n == 5:
        result = t.f5(42)
        print("OUTPUT:")
        print(result)
    if n == 6:
        result = t.f6()
        print("OUTPUT:")
        print(result)

    if n == 7:
        result = t.f7()
        print("OUTPUT:")
        print(result)
    if n == 8:
        result = t.f8()
        print("OUTPUT:")
        print(result)

    if n == 9:
        result = t.f9()
        print("OUTPUT:")
        print(result)

# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================

