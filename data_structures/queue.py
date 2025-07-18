from linked_list import Node

class Queue:
    def __init__(self, max_size=None):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size  # None means unlimited
    
    # Kiểm tra queue rỗng
    def isEmpty(self):
        return self.front is None
        
    # Kiểm tra queue đầy (nếu có giới hạn)
    def isFull(self):
        if self.max_size is None:
            return False
        return self.size >= self.max_size
        
    # Lấy kích thước hiện tại
    def getSize(self):
        return self.size
    
    # Thêm phần tử vào cuối queue
    def enQueue(self, data):
        if self.isFull():
            raise Exception("Queue is full")
            
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    # Lấy phần tử từ đầu queue
    def deQueue(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.data
        
    # Xóa tất cả phần tử khỏi queue
    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    # Tìm kiếm phần tử trong queue
    def search(self, key):
        if self.isEmpty():
            return False
        current = self.front
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
        
    # Đếm số lần xuất hiện của một giá trị
    def count(self, value):
        count = 0
        current = self.front
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count
    
    # Xem phần tử đầu queue mà không xóa
    def peek(self):
        if self.isEmpty():
            return None
        return self.front.data
    
    # Duyệt queue
    def traverse(self):
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    # Đảo ngược queue
    def reverse(self):
        if self.isEmpty():
            return
            
        # Sử dụng stack để đảo ngược
        stack = []
        while not self.isEmpty():
            stack.append(self.deQueue())
            
        # Đưa lại vào queue theo thứ tự ngược lại
        for item in reversed(stack):
            self.enQueue(item)
    
    # Sao chép queue
    def copy(self):
        new_queue = Queue(self.max_size)
        if self.isEmpty():
            return new_queue
            
        # Sử dụng mảng tạm để lưu giá trị
        temp_array = []
        current = self.front
        while current:
            temp_array.append(current.data)
            current = current.next
            
        # Thêm lại vào cả hai queue
        for item in temp_array:
            new_queue.enQueue(item)
            
        return new_queue
    
    # Kiểm tra queue có phải palindrome
    def isPalindrome(self):
        if self.isEmpty():
            return True
            
        # Sử dụng stack để so sánh
        stack = []
        temp_queue = self.copy()
        
        # Copy tất cả phần tử vào stack
        while not temp_queue.isEmpty():
            current = temp_queue.deQueue()
            stack.append(current)
        
        # So sánh từng phần tử
        temp_queue = self.copy()
        while not temp_queue.isEmpty():
            if temp_queue.deQueue() != stack.pop():
                return False
                
        return True
    
    # Sắp xếp queue
    def sort(self):
        if self.isEmpty():
            return
            
        # Chuyển sang list để sắp xếp
        arr = []
        while not self.isEmpty():
            arr.append(self.deQueue())
            
        # Sắp xếp
        arr.sort()
        
        # Đưa lại vào queue
        for item in arr:
            self.enQueue(item)
    
    # Trộn hai queue
    def merge(self, other_queue):
        if other_queue.isEmpty():
            return
            
        other_copy = other_queue.copy()
        while not other_copy.isEmpty():
            self.enQueue(other_copy.deQueue())
            
    # Trộn hai queue đã sắp xếp thành một queue được sắp xếp
    def mergeSorted(self, other_queue):
        """Trộn hai queue đã sắp xếp thành một queue được sắp xếp"""
        if other_queue.isEmpty():
            return
            
        result = Queue()
        temp1 = self.copy()
        temp2 = other_queue.copy()
        
        while not temp1.isEmpty() and not temp2.isEmpty():
            if temp1.peek() <= temp2.peek():
                result.enQueue(temp1.deQueue())
            else:
                result.enQueue(temp2.deQueue())
                
        # Thêm các phần tử còn lại từ queue 1
        while not temp1.isEmpty():
            result.enQueue(temp1.deQueue())
            
        # Thêm các phần tử còn lại từ queue 2
        while not temp2.isEmpty():
            result.enQueue(temp2.deQueue())
            
        # Cập nhật queue hiện tại
        self.front = result.front
        self.rear = result.rear
        self.size = result.size
            
    # Xóa các phần tử trùng lặp, giữ lại lần xuất hiện đầu tiên
    def removeDuplicates(self):
        if self.isEmpty():
            return
            
        seen = set()
        temp_queue = Queue()
        
        while not self.isEmpty():
            current = self.deQueue()
            if current not in seen:
                seen.add(current)
                temp_queue.enQueue(current)
                
        # Gán lại queue gốc
        self.front = temp_queue.front
        self.rear = temp_queue.rear
        self.size = temp_queue.size

    # Trả về phần tử lớn nhất trong queue
    def getMax(self):
        if self.isEmpty():
            return None
        current = self.front
        max_val = current.data
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val
    
    # Trả về phần tử nhỏ nhất trong queue
    def getMin(self):
        if self.isEmpty():
            return None
        current = self.front
        min_val = current.data
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val
    
    # Chia queue thành hai queue dựa trên điều kiện
    def split(self, condition):
        """
        Chia queue thành hai queue dựa trên điều kiện
        condition: một hàm nhận vào một giá trị và trả về True/False
        """
        queue1 = Queue()
        queue2 = Queue()
        temp = self.copy()
        
        while not temp.isEmpty():
            current = temp.deQueue()
            if condition(current):
                queue1.enQueue(current)
            else:
                queue2.enQueue(current)
                
        return queue1, queue2
    
    # Xoay queue sang phải k lần
    def rotateRight(self, k):
        if self.isEmpty() or k <= 0:
            return
        k = k % self.size  # Chuẩn hóa k
        for _ in range(k):
            # Lấy phần tử cuối cùng và thêm vào đầu
            temp = []
            for _ in range(self.size - 1):
                temp.append(self.deQueue())
            last = self.deQueue()
            self.enQueue(last)
            for item in temp:
                self.enQueue(item)
                
    # Xoay queue sang trái k lần
    def rotateLeft(self, k):
        if self.isEmpty() or k <= 0:
            return
        k = k % self.size  # Chuẩn hóa k
        self.rotateRight(self.size - k)
    
    # Kiểm tra xem queue có phải là subset của queue khác
    def isSubsetOf(self, other_queue):
        if self.isEmpty():
            return True
        if other_queue.isEmpty() or self.size > other_queue.size:
            return False
            
        temp_self = self.copy()
        temp_other = other_queue.copy()
        
        while not temp_self.isEmpty():
            current = temp_self.deQueue()
            found = False
            temp_array = []
            
            while not temp_other.isEmpty():
                other_val = temp_other.deQueue()
                temp_array.append(other_val)
                if other_val == current:
                    found = True
                    
            # Khôi phục other_queue
            for item in temp_array:
                temp_other.enQueue(item)
                
            if not found:
                return False
                
        return True

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo và thêm phần tử vào queue
    q1 = Queue(max_size=10)
    q1.enQueue(1)
    q1.enQueue(3)
    q1.enQueue(5)
    q1.enQueue(7)
    
    q2 = Queue(max_size=10)
    q2.enQueue(2)
    q2.enQueue(4)
    q2.enQueue(6)
    q2.enQueue(8)
    
    print("Queue 1 ban đầu:", q1.traverse())
    print("Queue 2 ban đầu:", q2.traverse())
    
    # Thử các phương thức mới
    print("\nThử nghiệm các phương thức nâng cao:")
    
    # Trộn hai queue đã sắp xếp
    q1_sorted = q1.copy()
    q2_sorted = q2.copy()
    q1_sorted.sort()
    q2_sorted.sort()
    q1_sorted.mergeSorted(q2_sorted)
    print("Sau khi trộn hai queue đã sắp xếp:", q1_sorted.traverse())
    
    # Tìm max và min
    print("Giá trị lớn nhất trong queue 1:", q1.getMax())
    print("Giá trị nhỏ nhất trong queue 1:", q1.getMin())
    
    # Chia queue thành chẵn và lẻ
    evens, odds = q1.split(lambda x: x % 2 == 0)
    print("Các số chẵn:", evens.traverse())
    print("Các số lẻ:", odds.traverse())
    
    # Xoay queue
    q1_rotated = q1.copy()
    q1_rotated.rotateRight(2)
    print("Queue 1 sau khi xoay phải 2 vị trí:", q1_rotated.traverse())
    
    q1_rotated = q1.copy()
    q1_rotated.rotateLeft(2)
    print("Queue 1 sau khi xoay trái 2 vị trí:", q1_rotated.traverse())
    
    # Kiểm tra subset
    test_subset = Queue()
    test_subset.enQueue(1)
    test_subset.enQueue(5)
    print("test_subset có phải là subset của q1?", test_subset.isSubsetOf(q1))
