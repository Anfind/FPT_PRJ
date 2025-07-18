class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Cho cân bằng cây
        self.count = 1   # Đếm số lần xuất hiện của giá trị (cho phép trùng lặp)
        self.balance_factor = 0  # Cho AVL Tree
        self.parent = None  # Cho iterator và xử lý cha-con

class BST:
    """
    Binary Search Tree với nhiều tính năng nâng cao:
    - Hỗ trợ cân bằng tự động (AVL)
    - Iterator cho các kiểu duyệt khác nhau
    - Xử lý cây con và so sánh cây
    - Tối ưu hóa bộ nhớ và hiệu năng
    """
    def __init__(self):
        self.root = None
        self.size = 0    # Số node trong cây
        
    def getSize(self):
        """Trả về số node trong cây"""
        return self.size
        
    def isEmpty(self):
        """Kiểm tra cây rỗng"""
        return self.root is None
        
    def height(self):
        """Tính chiều cao của cây"""
        return self._height_recursive(self.root)
        
    def _height_recursive(self, node):
        if not node:
            return 0
        return 1 + max(self._height_recursive(node.left), 
                      self._height_recursive(node.right))
    
    # Thêm node mới vào BST
    def insert(self, data):
        """Chèn một giá trị mới vào BST, hỗ trợ giá trị trùng lặp"""
        if not self.root:
            self.root = TreeNode(data)
            self.size += 1
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data == node.data:
            node.count += 1  # Tăng số lần xuất hiện
            return node
            
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
                self.size += 1
            else:
                node.left = self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
                self.size += 1
            else:
                node.right = self._insert_recursive(node.right, data)
                
        # Cập nhật chiều cao node
        node.height = 1 + max(self._get_height(node.left),
                            self._get_height(node.right))
        return node
        
    def _get_height(self, node):
        """Helper function để lấy chiều cao của node"""
        if not node:
            return 0
        return node.height
    
    # Xóa node khỏi BST
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, root, data):
        if root is None:
            return root
        
        if data < root.data:
            root.left = self._delete_recursive(root.left, data)
        elif data > root.data:
            root.right = self._delete_recursive(root.right, data)
        else:
            # Node với một hoặc không có con
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node với hai con
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete_recursive(root.right, temp.data)
        
        return root
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    # Duyệt cây theo thứ tự giữa (Inorder)
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.data)
            self._inorder_recursive(root.right, result)
    
    # Tìm giá trị nhỏ nhất
    def findMin(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    # Tìm giá trị lớn nhất
    def findMax(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    # Tìm kiếm một giá trị
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, root, data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self._search_recursive(root.left, data)
        return self._search_recursive(root.right, data)
    
    # Các phương thức duyệt cây
    def preorder(self):
        """Duyệt cây theo thứ tự trước (Pre-order: Node -> Left -> Right)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
        
    def _preorder_recursive(self, root, result):
        if root:
            result.append(root.data)
            self._preorder_recursive(root.left, result)
            self._preorder_recursive(root.right, result)
    
    def postorder(self):
        """Duyệt cây theo thứ tự sau (Post-order: Left -> Right -> Node)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
        
    def _postorder_recursive(self, root, result):
        if root:
            self._postorder_recursive(root.left, result)
            self._postorder_recursive(root.right, result)
            result.append(root.data)
    
    def levelOrder(self):
        """Duyệt cây theo từng tầng (Level-order)"""
        if not self.root:
            return []
            
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result
    
    # Các phương thức kiểm tra tính chất của cây
    def isBalanced(self):
        """Kiểm tra cây có cân bằng không (độ chênh lệch chiều cao <= 1)"""
        return self._isBalanced_recursive(self.root)
        
    def _isBalanced_recursive(self, root):
        if not root:
            return True
            
        left_height = self._height_recursive(root.left)
        right_height = self._height_recursive(root.right)
        
        if abs(left_height - right_height) <= 1 and \
           self._isBalanced_recursive(root.left) and \
           self._isBalanced_recursive(root.right):
            return True
            
        return False
    
    def isBST(self):
        """Kiểm tra có phải là cây nhị phân tìm kiếm hợp lệ"""
        return self._isBST_recursive(self.root, float('-inf'), float('inf'))
        
    def _isBST_recursive(self, node, min_val, max_val):
        if not node:
            return True
            
        if node.data <= min_val or node.data >= max_val:
            return False
            
        return self._isBST_recursive(node.left, min_val, node.data) and \
               self._isBST_recursive(node.right, node.data, max_val)
               
    # Các phương thức tìm kiếm nâng cao
    def findKthSmallest(self, k):
        """Tìm phần tử nhỏ thứ k trong BST"""
        result = []
        self._inorder_recursive(self.root, result)
        return result[k-1] if 0 < k <= len(result) else None
        
    def findKthLargest(self, k):
        """Tìm phần tử lớn thứ k trong BST"""
        result = []
        self._inorder_recursive(self.root, result)
        return result[-k] if 0 < k <= len(result) else None
    
    def findLCA(self, n1, n2):
        """Tìm tổ tiên chung gần nhất của hai node"""
        return self._findLCA_recursive(self.root, n1, n2)
        
    def _findLCA_recursive(self, root, n1, n2):
        if not root:
            return None
            
        # Nếu cả hai node đều lớn hơn root, LCA nằm bên phải
        if root.data < n1 and root.data < n2:
            return self._findLCA_recursive(root.right, n1, n2)
            
        # Nếu cả hai node đều nhỏ hơn root, LCA nằm bên trái
        if root.data > n1 and root.data > n2:
            return self._findLCA_recursive(root.left, n1, n2)
            
        return root.data
    
    def findCeiling(self, key):
        """Tìm số nhỏ nhất lớn hơn hoặc bằng key"""
        ceiling = None
        current = self.root
        
        while current:
            if current.data == key:
                return current.data
                
            if current.data < key:
                current = current.right
            else:
                ceiling = current.data
                current = current.left
                
        return ceiling
    
    def findFloor(self, key):
        """Tìm số lớn nhất nhỏ hơn hoặc bằng key"""
        floor = None
        current = self.root
        
        while current:
            if current.data == key:
                return current.data
                
            if current.data > key:
                current = current.left
            else:
                floor = current.data
                current = current.right
                
        return floor

    # Các phương thức cho predecessor và successor
    def findPredecessor(self, data):
        """Tìm node có giá trị lớn nhất nhỏ hơn data"""
        node = self.search(data)
        if not node:
            return None
            
        # Nếu có cây con trái, predecessor là max của cây con trái
        if node.left:
            current = node.left
            while current.right:
                current = current.right
            return current.data
            
        # Nếu không có cây con trái, tìm ancestor đầu tiên mà node nằm ở bên phải
        predecessor = None
        current = self.root
        while current:
            if current.data < data:
                predecessor = current.data
                current = current.right
            elif current.data > data:
                current = current.left
            else:
                break
                
        return predecessor
        
    def findSuccessor(self, data):
        """Tìm node có giá trị nhỏ nhất lớn hơn data"""
        node = self.search(data)
        if not node:
            return None
            
        # Nếu có cây con phải, successor là min của cây con phải
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.data
            
        # Nếu không có cây con phải, tìm ancestor đầu tiên mà node nằm ở bên trái
        successor = None
        current = self.root
        while current:
            if current.data > data:
                successor = current.data
                current = current.left
            elif current.data < data:
                current = current.right
            else:
                break
                
        return successor
        
    # Các phương thức cho khoảng giá trị
    def countInRange(self, low, high):
        """Đếm số node có giá trị trong khoảng [low, high]"""
        return self._countInRange_recursive(self.root, low, high)
        
    def _countInRange_recursive(self, root, low, high):
        if not root:
            return 0
            
        if root.data < low:
            return self._countInRange_recursive(root.right, low, high)
        elif root.data > high:
            return self._countInRange_recursive(root.left, low, high)
        else:
            return (1 * root.count + 
                   self._countInRange_recursive(root.left, low, high) +
                   self._countInRange_recursive(root.right, low, high))
                   
    def printInRange(self, low, high):
        """In tất cả các node có giá trị trong khoảng [low, high]"""
        result = []
        self._printInRange_recursive(self.root, low, high, result)
        return result
        
    def _printInRange_recursive(self, root, low, high, result):
        if not root:
            return
            
        if low < root.data:
            self._printInRange_recursive(root.left, low, high, result)
            
        if low <= root.data <= high:
            result.extend([root.data] * root.count)
            
        if high > root.data:
            self._printInRange_recursive(root.right, low, high, result)

    # Phương thức kiểm tra và xử lý đường đi
    def findPath(self, start, end):
        """Tìm đường đi từ node start đến node end"""
        if not self.search(start) or not self.search(end):
            return None
            
        lca = self.findLCA(start, end)
        if not lca:
            return None
            
        path_to_start = []
        path_to_end = []
        
        # Tìm đường đi từ LCA đến start
        current = self.root
        while current:
            if current.data == lca:
                break
            if start < current.data:
                path_to_start.append(current.data)
                current = current.left
            else:
                path_to_start.append(current.data)
                current = current.right
                
        # Tìm đường đi từ LCA đến end
        current = self.root
        while current:
            if current.data == lca:
                break
            if end < current.data:
                path_to_end.append(current.data)
                current = current.left
            else:
                path_to_end.append(current.data)
                current = current.right
                
        return path_to_start + [lca] + path_to_end

    # Phương thức in cây theo dạng đồ họa
    def display(self):
        """In cây theo dạng đồ họa trực quan"""
        lines = []
        self._display_recursive(self.root, 0, lines)
        return '\n'.join(lines)
        
    def _display_recursive(self, root, level, lines):
        if root:
            self._display_recursive(root.right, level + 1, lines)
            if len(lines) <= level:
                lines.append('')
            lines[level] = ('   ' * level) + str(root.data) + \
                          (f'({root.count})' if root.count > 1 else '')
            self._display_recursive(root.left, level + 1, lines)
            
    # Phương thức serialize/deserialize
    def serialize(self):
        """Chuyển cây thành chuỗi để lưu trữ"""
        if not self.root:
            return "null"
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.data))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
                
        # Cắt bỏ các null ở cuối
        while result[-1] == "null":
            result.pop()
            
        return ",".join(result)
        
    @classmethod
    def deserialize(cls, data):
        """Tạo lại cây từ chuỗi đã serialize"""
        if data == "null":
            return cls()
            
        values = data.split(',')
        bst = cls()
        
        for val in values:
            if val != "null":
                bst.insert(int(val))
                
        return bst
        
    # Phương thức xoay cây
    def rotateLeft(self, node):
        """Xoay trái tại node"""
        if not node or not node.right:
            return node
            
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        # Cập nhật chiều cao
        node.height = 1 + max(self._get_height(node.left),
                            self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left),
                                self._get_height(new_root.right))
                                
        return new_root
        
    def rotateRight(self, node):
        """Xoay phải tại node"""
        if not node or not node.left:
            return node
            
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        # Cập nhật parent pointers
        new_root.parent = node.parent
        node.parent = new_root
        if new_root.right:
            new_root.right.parent = node
        
        # Cập nhật chiều cao và balance factor
        node.height = 1 + max(self._get_height(node.left),
                            self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left),
                                self._get_height(new_root.right))
        
        # Cập nhật balance factor
        node.balance_factor = self._get_height(node.right) - self._get_height(node.left)
        new_root.balance_factor = self._get_height(new_root.right) - self._get_height(new_root.left)
                                
        return new_root
    
    # Các phương thức AVL
    def _update_balance(self, node):
        """Cập nhật balance factor cho node"""
        if not node:
            return
        node.balance_factor = self._get_height(node.right) - self._get_height(node.left)
        
    def _balance(self, node):
        """Cân bằng cây tại node nếu cần"""
        if not node:
            return node
            
        self._update_balance(node)
        
        # Cây lệch trái
        if node.balance_factor < -1:
            # Kiểm tra xem có cần xoay kép không
            if self._get_height(node.left.right) > self._get_height(node.left.left):
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
            
        # Cây lệch phải
        if node.balance_factor > 1:
            # Kiểm tra xem có cần xoay kép không
            if self._get_height(node.right.left) > self._get_height(node.right.right):
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
            
        return node
        
    # Iterator classes cho các kiểu duyệt khác nhau
    class InorderIterator:
        def __init__(self, root):
            self.current = root
            self.stack = []
            # Đi đến node nhỏ nhất
            while self.current:
                self.stack.append(self.current)
                self.current = self.current.left
                
        def hasNext(self):
            return bool(self.stack)
            
        def next(self):
            if not self.hasNext():
                return None
                
            node = self.stack.pop()
            current = node
            
            # Nếu có cây con phải, thêm path đến node nhỏ nhất của cây con phải
            if current.right:
                current = current.right
                while current:
                    self.stack.append(current)
                    current = current.left
                    
            return node.data
    
    # Phương thức cho iterator
    def getIterator(self, traversal_type="inorder"):
        """Trả về iterator cho kiểu duyệt được chọn"""
        if traversal_type == "inorder":
            return self.InorderIterator(self.root)
        # Có thể thêm các loại iterator khác ở đây
        
    # Các phương thức xử lý cây con
    def getSubtree(self, data):
        """Trả về một BST mới chứa cây con gốc tại node có giá trị data"""
        node = self.search(data)
        if not node:
            return None
            
        new_bst = BST()
        new_bst.root = self._copy_subtree(node)
        return new_bst
        
    def _copy_subtree(self, node):
        """Copy một cây con, giữ nguyên cấu trúc"""
        if not node:
            return None
            
        new_node = TreeNode(node.data)
        new_node.count = node.count
        new_node.height = node.height
        new_node.balance_factor = node.balance_factor
        
        new_node.left = self._copy_subtree(node.left)
        if new_node.left:
            new_node.left.parent = new_node
            
        new_node.right = self._copy_subtree(node.right)
        if new_node.right:
            new_node.right.parent = new_node
            
        return new_node
        
    def compareWith(self, other_bst):
        """So sánh hai cây BST"""
        return self._compare_subtrees(self.root, other_bst.root)
        
    def _compare_subtrees(self, root1, root2):
        """So sánh hai cây con"""
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
            
        return (root1.data == root2.data and
                root1.count == root2.count and
                self._compare_subtrees(root1.left, root2.left) and
                self._compare_subtrees(root1.right, root2.right))
                
    # Các phương thức tối ưu hóa
    def optimize(self):
        """Tối ưu hóa cấu trúc cây"""
        # Cân bằng toàn bộ cây
        values = []
        self._inorder_recursive(self.root, values)
        self.root = None
        self.size = 0
        
        # Xây dựng lại cây cân bằng
        self._build_balanced_tree(values, 0, len(values)-1)
        
    def _build_balanced_tree(self, values, start, end):
        """Xây dựng cây cân bằng từ danh sách đã sắp xếp"""
        if start > end:
            return
            
        mid = (start + end) // 2
        self.insert(values[mid])
        
        self._build_balanced_tree(values, start, mid-1)
        self._build_balanced_tree(values, mid+1, end)
        
    # Phương thức kiểm tra tính đối xứng
    def isSymmetric(self):
        """Kiểm tra cây có đối xứng không"""
        if not self.root:
            return True
        return self._isSymmetric_recursive(self.root.left, self.root.right)
        
    def _isSymmetric_recursive(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
            
        return (left.data == right.data and
                self._isSymmetric_recursive(left.left, right.right) and
                self._isSymmetric_recursive(left.right, right.left))

# Ví dụ sử dụng
if __name__ == "__main__":
    # 1. Tạo và thêm dữ liệu vào BST
    bst = BST()
    nums = [5, 3, 7, 1, 4, 6, 8, 3]  # Note: có số 3 trùng lặp
    for num in nums:
        bst.insert(num)
        
    # Hiển thị cấu trúc cây ban đầu
    print("Cây ban đầu:")
    print(bst.display())
    
    # 2. Thử nghiệm iterator
    print("\nDuyệt cây sử dụng iterator:")
    iterator = bst.getIterator()
    while iterator.hasNext():
        print(iterator.next(), end=' ')
    print()
    
    # 3. Thử nghiệm cây con
    print("\nLấy và hiển thị cây con gốc tại node 3:")
    subtree = bst.getSubtree(3)
    if subtree:
        print(subtree.display())
    
    # 4. So sánh cây
    print("\nTạo một cây khác để so sánh:")
    bst2 = BST()
    for num in [5, 3, 7, 1, 4, 6, 8, 3]:  # Cấu trúc giống bst1
        bst2.insert(num)
    print("Hai cây có giống nhau?", bst.compareWith(bst2))
    
    # 5. Tối ưu hóa cây
    print("\nTối ưu hóa cấu trúc cây:")
    print("Trước khi tối ưu:")
    print(bst.display())
    bst.optimize()
    print("\nSau khi tối ưu (cân bằng hoàn hảo):")
    print(bst.display())
    
    # 6. Kiểm tra cân bằng AVL
    print("\nKiểm tra các thông số cân bằng:")
    def print_balance_info(node, prefix=""):
        if node:
            print(f"{prefix}Node {node.data}: height={node.height}, balance_factor={node.balance_factor}")
            print_balance_info(node.left, prefix + "  ")
            print_balance_info(node.right, prefix + "  ")

    print("1. Thông tin cơ bản của cây:")
    print("Cấu trúc cây:")
    print(bst.display())  # In cây theo dạng đồ họa
    print("\nKích thước:", bst.getSize())
    print("Chiều cao:", bst.height())
    
    print("\n2. Các cách duyệt cây:")
    print("Inorder (LNR):", bst.inorder())
    print("Preorder (NLR):", bst.preorder())
    print("Postorder (LRN):", bst.postorder())
    print("Level-order:", bst.levelOrder())
    
    print("\n3. Tìm kiếm giá trị đặc biệt:")
    print("Min:", bst.findMin())
    print("Max:", bst.findMax())
    print("Phần tử nhỏ thứ 3:", bst.findKthSmallest(3))
    print("Phần tử lớn thứ 2:", bst.findKthLargest(2))
    
    print("\n4. Predecessor và Successor:")
    print("Predecessor của 5:", bst.findPredecessor(5))
    print("Successor của 5:", bst.findSuccessor(5))
    
    print("\n5. Tìm kiếm trong khoảng:")
    print("Số node trong khoảng [3, 6]:", bst.countInRange(3, 6))
    print("Các node trong khoảng [3, 6]:", bst.printInRange(3, 6))
    
    print("\n6. Đường đi giữa các node:")
    print("Đường đi từ 1 đến 8:", bst.findPath(1, 8))
    
    print("\n7. Kiểm tra tính chất:")
    print("Cây có cân bằng?", bst.isBalanced())
    print("Cây có phải BST hợp lệ?", bst.isBST())
    print("Cây có đối xứng?", bst.isSymmetric())
    
    print("\n8. Lưu trữ và khôi phục:")
    serialized = bst.serialize()
    print("Chuỗi serialize:", serialized)
    new_bst = BST.deserialize(serialized)
    print("\nCây sau khi deserialize:")
    print(new_bst.display())
    
    print("\n9. Tìm kiếm nâng cao:")
    print("LCA của 1 và 4:", bst.findLCA(1, 4))
    print("Ceiling của 2:", bst.findCeiling(2))
    print("Floor của 2:", bst.findFloor(2))
    
    print("\n10. Thử nghiệm xóa node:")
    print("Trước khi xóa 3:")
    print(bst.display())
    bst.delete(3)
    print("\nSau khi xóa một node có giá trị 3:")
    print(bst.display())
