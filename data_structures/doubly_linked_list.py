class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Con trỏ đến node trước đó

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Con trỏ đến node cuối
        self.size = 0
    
    # Thêm node vào đầu danh sách
    def addFirst(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    # Thêm node vào cuối danh sách
    def addLast(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    # Thêm node vào vị trí bất kỳ (0-based index)
    def addAtIndex(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        
        if index == 0:
            self.addFirst(data)
            return
            
        if index == self.size:
            self.addLast(data)
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(index):
            current = current.next
            
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1
    
    # Thêm node sau một node có giá trị cụ thể
    def addAfter(self, target_data, data):
        current = self.head
        while current:
            if current.data == target_data:
                if current == self.tail:
                    self.addLast(data)
                else:
                    new_node = Node(data)
                    new_node.next = current.next
                    new_node.prev = current
                    current.next.prev = new_node
                    current.next = new_node
                    self.size += 1
                return True
            current = current.next
        return False
    
    # Thêm node trước một node có giá trị cụ thể
    def addBefore(self, target_data, data):
        if not self.head:
            return False
            
        if self.head.data == target_data:
            self.addFirst(data)
            return True
            
        current = self.head.next
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node
                self.size += 1
                return True
            current = current.next
        return False
    
    # Xóa node đầu tiên
    def removeFirst(self):
        if not self.head:
            return None
            
        removed_data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return removed_data
    
    # Xóa node cuối cùng
    def removeLast(self):
        if not self.head:
            return None
            
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return removed_data
    
    # Xóa node tại vị trí bất kỳ (0-based index)
    def removeAtIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
            
        if index == 0:
            return self.removeFirst()
            
        if index == self.size - 1:
            return self.removeLast()
            
        current = self.head
        for i in range(index):
            current = current.next
            
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return current.data
    
    # Xóa node có giá trị cụ thể (xóa node đầu tiên tìm thấy)
    def removeByValue(self, data):
        if not self.head:
            return False
            
        if self.head.data == data:
            self.removeFirst()
            return True
            
        if self.tail.data == data:
            self.removeLast()
            return True
            
        current = self.head.next
        while current != self.tail:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        return False
    
    # Xóa tất cả các node có giá trị cụ thể
    def removeAllByValue(self, data):
        count = 0
        while self.head and self.head.data == data:
            self.removeFirst()
            count += 1
            
        if self.head:
            current = self.head
            while current:
                if current.data == data:
                    # Nếu là node cuối
                    if current == self.tail:
                        self.removeLast()
                        count += 1
                        break
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        count += 1
                        self.size -= 1
                current = current.next
        return count
    
    # Duyệt danh sách từ đầu đến cuối
    def traverseForward(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    # Duyệt danh sách từ cuối về đầu
    def traverseBackward(self):
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
    
    # Tìm giá trị lớn nhất
    def findMax(self):
        if not self.head:
            return None
        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val
    
    # Tìm giá trị nhỏ nhất
    def findMin(self):
        if not self.head:
            return None
        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val
    
    # Lấy kích thước danh sách
    def getSize(self):
        return self.size
    
    # Đếm số lượng node có giá trị cụ thể
    def countValue(self, data):
        count = 0
        current = self.head
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count
    
    # Đảo ngược danh sách
    def reverse(self):
        if not self.head or not self.head.next:
            return
            
        current = self.head
        self.tail = self.head
        
        while current:
            # Lưu next node
            next_node = current.next
            # Đảo ngược các con trỏ
            current.next = current.prev
            current.prev = next_node
            # Di chuyển đến node tiếp theo
            if not next_node:
                self.head = current
            current = next_node
    
    # Kiểm tra xem danh sách có phải là palindrome
    def isPalindrome(self):
        if not self.head or not self.head.next:
            return True
            
        # So sánh từ hai đầu vào giữa
        left = self.head
        right = self.tail
        
        while left != right and left.prev != right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.prev
            
        return True
    
    # Sắp xếp danh sách (sử dụng bubble sort)
    def sort(self):
        if not self.head or not self.head.next:
            return
            
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    # Swap data
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
    
    # Xóa các node trùng lặp (giữ lại một)
    def removeDuplicates(self):
        if not self.head or not self.head.next:
            return
            
        values = set([self.head.data])
        current = self.head
        while current.next:
            if current.next.data in values:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                else:
                    self.tail = current
                self.size -= 1
            else:
                values.add(current.next.data)
                current = current.next
                
    # Tìm phần tử ở vị trí thứ k từ cuối
    def findKthFromEnd(self, k):
        if not self.head or k <= 0 or k > self.size:
            return None
            
        current = self.tail
        for i in range(k-1):
            current = current.prev
            
        return current.data
        
    # Hoán đổi giá trị của hai node bất kỳ
    def swapValues(self, x, y):
        if x == y:
            return
            
        # Tìm node chứa giá trị x và y
        currX = self.head
        while currX and currX.data != x:
            currX = currX.next
            
        currY = self.head
        while currY and currY.data != y:
            currY = currY.next
            
        # Nếu một trong hai giá trị không tồn tại
        if not currX or not currY:
            return
            
        # Hoán đổi giá trị
        currX.data, currY.data = currY.data, currX.data

    # Hoán đổi hai node liền kề (node1 đứng trước node2)
    def swapAdjacentNodes(self, node1, node2):
        if not node1 or not node2 or node1.next != node2:
            return
            
        # Cập nhật prev của node1
        if node1 == self.head:
            self.head = node2
        else:
            node1.prev.next = node2
            
        # Cập nhật next của node2
        if node2 == self.tail:
            self.tail = node1
        else:
            node2.next.prev = node1
            
        # Hoán đổi các con trỏ
        node1.next = node2.next
        node2.prev = node1.prev
        node2.next = node1
        node1.prev = node2

    # Hoán đổi hai node bất kỳ
    def swapNodes(self, x, y):
        if x == y:
            return
            
        # Tìm node chứa x và y
        nodeX = self.head
        while nodeX and nodeX.data != x:
            nodeX = nodeX.next
            
        nodeY = self.head
        while nodeY and nodeY.data != y:
            nodeY = nodeY.next
            
        # Nếu một trong hai node không tồn tại
        if not nodeX or not nodeY:
            return
            
        # Nếu hai node liền kề
        if nodeX.next == nodeY:
            self.swapAdjacentNodes(nodeX, nodeY)
            return
        if nodeY.next == nodeX:
            self.swapAdjacentNodes(nodeY, nodeX)
            return
            
        # Cập nhật head và tail nếu cần
        if nodeX == self.head:
            self.head = nodeY
        elif nodeY == self.head:
            self.head = nodeX
        if nodeX == self.tail:
            self.tail = nodeY
        elif nodeY == self.tail:
            self.tail = nodeX
            
        # Lưu các con trỏ
        xPrev, xNext = nodeX.prev, nodeX.next
        yPrev, yNext = nodeY.prev, nodeY.next
        
        # Cập nhật các con trỏ của node trước và sau
        if xPrev:
            xPrev.next = nodeY
        nodeY.prev = xPrev
        
        if xNext:
            xNext.prev = nodeY
        nodeY.next = xNext
        
        if yPrev:
            yPrev.next = nodeX
        nodeX.prev = yPrev
        
        if yNext:
            yNext.prev = nodeX
        nodeX.next = yNext

    # Hoán đổi cặp node kề nhau
    def swapPairs(self):
        if not self.head or not self.head.next:
            return
            
        current = self.head
        while current and current.next:
            # Hoán đổi giá trị của hai node kề nhau
            current.data, current.next.data = current.next.data, current.data
            # Di chuyển đến cặp tiếp theo
            current = current.next.next

    # Hoán đổi node theo index
    def swapNodesByIndex(self, i, j):
        if i == j or i < 0 or j < 0 or i >= self.size or j >= self.size:
            return
            
        # Tìm node thứ i
        nodeI = self.head
        for _ in range(i):
            nodeI = nodeI.next
            
        # Tìm node thứ j
        nodeJ = self.head
        for _ in range(j):
            nodeJ = nodeJ.next
            
        # Hoán đổi hai node
        self.swapNodes(nodeI.data, nodeJ.data)

# Ví dụ sử dụng
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Thêm các phần tử
    dll.addFirst(3)
    dll.addLast(7)
    dll.addFirst(1)
    dll.addLast(9)
    
    print("Duyệt từ đầu đến cuối:", dll.traverseForward())
    print("Duyệt từ cuối về đầu:", dll.traverseBackward())
    print("Giá trị lớn nhất:", dll.findMax())
    print("Giá trị nhỏ nhất:", dll.findMin())
    
    # Thêm vào vị trí cụ thể
    dll.addAtIndex(2, 5)
    print("Sau khi thêm 5 vào index 2:", dll.traverseForward())
    
    # Xóa phần tử
    print("Xóa đầu:", dll.removeFirst())
    print("Xóa cuối:", dll.removeLast())
    print("Sau khi xóa:", dll.traverseForward())
    
    # Kiểm tra palindrome
    dll.addLast(5)
    dll.addLast(3)
    print("Danh sách hiện tại:", dll.traverseForward())
    print("Là palindrome?", dll.isPalindrome())
    
    # Đảo ngược danh sách
    dll.reverse()
    print("Sau khi đảo ngược:", dll.traverseForward())
