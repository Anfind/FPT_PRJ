class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Thêm tail để tối ưu thao tác với cuối danh sách
        self.size = 0  # Thêm biến size để theo dõi kích thước
    
    # Thêm node vào đầu danh sách
    def addFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    # Thêm node vào cuối danh sách
    def addLast(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    # Thêm node vào vị trí bất kỳ (0-based index)
    def addAtIndex(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        
        if index == 0:
            self.addFirst(data)
            return
            
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    # Thêm node sau một node có giá trị cụ thể
    def addAfter(self, target_data, data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return True
            current = current.next
        return False  # Không tìm thấy target_data
    
    # Thêm node trước một node có giá trị cụ thể
    def addBefore(self, target_data, data):
        if not self.head:
            return False
            
        if self.head.data == target_data:
            self.addFirst(data)
            return True
            
        current = self.head
        while current.next:
            if current.next.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return True
            current = current.next
        return False  # Không tìm thấy target_data
    
    # Xóa node đầu tiên
    def removeFirst(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return removed_data
        
    # Xóa node tại vị trí bất kỳ (0-based index)
    def removeAtIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
            
        if index == 0:
            return self.removeFirst()
            
        current = self.head
        for i in range(index - 1):
            current = current.next
            
        removed_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return removed_data
    
    # Xóa node có giá trị cụ thể (xóa node đầu tiên tìm thấy)
    def removeByValue(self, data):
        if not self.head:
            return False
            
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
            
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False  # Không tìm thấy giá trị cần xóa
    
    # Xóa tất cả các node có giá trị cụ thể
    def removeAllByValue(self, data):
        count = 0
        while self.head and self.head.data == data:
            self.head = self.head.next
            count += 1
            self.size -= 1
            
        if self.head:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    count += 1
                    self.size -= 1
                else:
                    current = current.next
        return count  # Trả về số node đã xóa
    
    # Xóa node cuối cùng
    def removeLast(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data
    
    # Duyệt danh sách
    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
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
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    # Kiểm tra xem danh sách có phải là palindrome
    def isPalindrome(self):
        if not self.head or not self.head.next:
            return True
            
        # Tìm điểm giữa
        slow = fast = self.head
        stack = []
        
        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next
        
        # Nếu số phần tử lẻ, bỏ qua phần tử giữa
        if fast:
            slow = slow.next
        
        # So sánh nửa sau với nửa trước (trong stack)
        while slow:
            if stack.pop() != slow.data:
                return False
            slow = slow.next
        
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
                self.size -= 1
            else:
                values.add(current.next.data)
                current = current.next
                
    # Tìm phần tử ở vị trí thứ k từ cuối
    def findKthFromEnd(self, k):
        if not self.head or k <= 0:
            return None
            
        # Sử dụng hai con trỏ cách nhau k node
        slow = fast = self.head
        
        # Di chuyển fast đi trước k node
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
            
        # Di chuyển cả hai con trỏ cho đến khi fast đến cuối
        while fast:
            slow = slow.next
            fast = fast.next
            
        return slow.data

    # Tách danh sách thành hai nửa
    def split(self):
        if not self.head or not self.head.next:
            return self, None
            
        # Tìm điểm giữa
        slow = fast = self.head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        # Tạo danh sách mới từ nửa sau
        second_half = LinkedList()
        second_half.head = slow
        second_half.size = self.size // 2
        
        # Cắt nửa đầu
        prev.next = None
        self.size = (self.size + 1) // 2
        
        return self, second_half

    # Ghép hai danh sách có thứ tự thành một danh sách có thứ tự
    def merge(self, other):
        if not other.head:
            return self
        if not self.head:
            self.head = other.head
            self.size = other.size
            return self
            
        # Tạo node giả để dễ xử lý
        dummy = Node(0)
        current = dummy
        
        # Con trỏ cho hai danh sách
        l1 = self.head
        l2 = other.head
        
        # Ghép hai danh sách
        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        # Nối phần còn lại
        current.next = l1 if l1 else l2
        
        self.head = dummy.next
        self.size += other.size
        return self

    # Sắp xếp merge sort (hiệu quả hơn bubble sort)
    def mergeSort(self):
        if not self.head or not self.head.next:
            return self
            
        # Tách danh sách làm đôi
        left, right = self.split()
        
        # Đệ quy sắp xếp hai nửa
        left.mergeSort()
        right.mergeSort()
        
        # Ghép hai nửa đã sắp xếp
        return left.merge(right)

    # Phát hiện và xóa chu trình (nếu có)
    def detectAndRemoveLoop(self):
        if not self.head or not self.head.next:
            return False
            
        # Sử dụng Floyd's Cycle-Finding Algorithm
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        # Không có chu trình
        if not fast or not fast.next:
            return False
            
        # Tìm điểm bắt đầu của chu trình
        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
            
        # Xóa chu trình
        fast.next = None
        return True

    # Hoán đổi các cặp node liền kề
    def swapPairs(self):
        if not self.head or not self.head.next:
            return
            
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes cần hoán đổi
            first = prev.next
            second = first.next
            
            # Thực hiện hoán đổi
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Di chuyển đến cặp tiếp theo
            prev = first
            
        self.head = dummy.next

    # Xoay danh sách sang phải k vị trí
    # Hoán đổi giá trị của hai node bất kỳ
    def swapValues(self, x, y):
        if x == y:
            return
            
        # Tìm node chứa giá trị x
        currX = self.head
        while currX and currX.data != x:
            currX = currX.next
            
        # Tìm node chứa giá trị y
        currY = self.head
        while currY and currY.data != y:
            currY = currY.next
            
        # Nếu một trong hai giá trị không tồn tại
        if not currX or not currY:
            return
            
        # Hoán đổi giá trị
        currX.data, currY.data = currY.data, currX.data
    
    # Hoán đổi hai node liền kề theo giá trị
    def swapAdjacent(self, x):
        if not self.head or not self.head.next:
            return False
            
        # Nếu x là head
        if self.head.data == x:
            if self.head.next:  # Đảm bảo có node kế tiếp
                self.head.data, self.head.next.data = self.head.next.data, self.head.data
                return True
            return False
            
        # Tìm node trước node chứa x
        prev = self.head
        while prev.next and prev.next.data != x:
            prev = prev.next
            
        if not prev.next or not prev.next.next:  # Không tìm thấy x hoặc x là node cuối
            return False
            
        # Hoán đổi giá trị của node chứa x và node kế tiếp
        prev.next.data, prev.next.next.data = prev.next.next.data, prev.next.data
        return True
    
    # Hoán đổi hai node bất kỳ (không chỉ giá trị mà là cả node)
    def swapNodes(self, x, y):
        if x == y:
            return
            
        # Tìm x
        prevX = None
        currX = self.head
        while currX and currX.data != x:
            prevX = currX
            currX = currX.next
            
        # Tìm y
        prevY = None
        currY = self.head
        while currY and currY.data != y:
            prevY = currY
            currY = currY.next
            
        # Nếu một trong hai node không tồn tại
        if not currX or not currY:
            return
            
        # Nếu x không phải head
        if prevX:
            prevX.next = currY
        else:
            self.head = currY
            
        # Nếu y không phải head
        if prevY:
            prevY.next = currX
        else:
            self.head = currX
            
        # Hoán đổi next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
    
    # Hoán đổi cặp node thứ i và j (0-based index)
    def swapNodesByIndex(self, i, j):
        if i == j or i < 0 or j < 0 or i >= self.size or j >= self.size:
            return
            
        # Đảm bảo i < j
        if i > j:
            i, j = j, i
            
        if i == 0:  # Xử lý trường hợp đặc biệt khi i là head
            currI = self.head
            prevJ = self.head
            for _ in range(j-1):
                prevJ = prevJ.next
            currJ = prevJ.next
            
            # Cập nhật head
            self.head = currJ
            temp = currJ.next
            currJ.next = currI.next
            prevJ.next = currI
            currI.next = temp
        else:
            # Tìm node thứ i và node trước nó
            prevI = self.head
            for _ in range(i-1):
                prevI = prevI.next
            currI = prevI.next
            
            # Tìm node thứ j và node trước nó
            prevJ = currI
            for _ in range(j-i-1):
                prevJ = prevJ.next
            currJ = prevJ.next
            
            # Thực hiện hoán đổi
            prevI.next = currJ
            temp = currJ.next
            currJ.next = currI.next
            prevJ.next = currI
            currI.next = temp
    
    def rotateRight(self, k):
        if not self.head or not self.head.next or k == 0:
            return
            
        # Chuẩn hóa k
        k = k % self.size
        if k == 0:
            return
            
        # Tìm node mới sẽ là tail
        slow = fast = self.head
        for _ in range(k):
            fast = fast.next
            
        # Di chuyển đến vị trí cần cắt
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # Thực hiện xoay
        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

    # Nhóm các node theo k phần tử và đảo ngược từng nhóm
    def reverseKGroup(self, k):
        if k <= 1 or not self.head:
            return
            
        def reverseGroup(start, k):
            # Kiểm tra xem có đủ k node không
            current = start
            for _ in range(k):
                if not current:
                    return None, None, False
                current = current.next
                
            # Đảo ngược k node
            prev = None
            current = start
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                
            return prev, start, True  # new_first, new_last, success
            
        dummy = Node(0)
        dummy.next = self.head
        prev_group = dummy
        
        while prev_group:
            new_first, new_last, success = reverseGroup(prev_group.next, k)
            if not success:
                break
                
            # Kết nối với phần còn lại
            next_group = new_last.next
            prev_group.next = new_first
            new_last.next = next_group
            prev_group = new_last
            
        self.head = dummy.next

# Ví dụ sử dụng
if __name__ == "__main__":
    ll = LinkedList()
    ll.addFirst(3)
    ll.addLast(7)
    ll.addFirst(1)
    ll.addLast(9)
    print("Danh sách:", ll.traverse())
    print("Giá trị lớn nhất:", ll.findMax())
    print("Giá trị nhỏ nhất:", ll.findMin())
    print("Xóa đầu:", ll.removeFirst())
    print("Xóa cuối:", ll.removeLast())
    print("Danh sách sau khi xóa:", ll.traverse())
