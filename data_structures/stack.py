from linked_list import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0  # Theo dõi kích thước stack
        self.min_element = None  # Theo dõi phần tử nhỏ nhất
        
    # Kiểm tra stack rỗng
    def isEmpty(self):
        return self.top is None
        
    # Lấy kích thước stack
    def getSize(self):
        return self.size
    
    # Thêm phần tử vào đỉnh stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        
        # Cập nhật phần tử nhỏ nhất
        if self.min_element is None or data < self.min_element:
            self.min_element = data
    
    # Lấy phần tử từ đỉnh stack
    def pop(self):
        if self.isEmpty():
            return None
        temp = self.top
        self.top = self.top.next
        self.size -= 1
        
        # Cập nhật phần tử nhỏ nhất nếu cần
        if temp.data == self.min_element:
            self.min_element = self._findMin()
            
        return temp.data
        
    # Tìm phần tử nhỏ nhất trong stack
    def _findMin(self):
        if self.isEmpty():
            return None
        current = self.top
        min_val = current.data
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val
        
    # Lấy phần tử nhỏ nhất trong O(1)
    def getMin(self):
        return self.min_element
    
    # Xem phần tử đỉnh stack mà không xóa
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data
    
    # Duyệt stack
    def traverse(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    # Đảo ngược stack
    def reverse(self):
        if self.isEmpty():
            return
        temp_stack = Stack()
        while not self.isEmpty():
            temp_stack.push(self.pop())
        self.top = temp_stack.top
        self.size = temp_stack.size
        self.min_element = temp_stack.min_element
    
    # Sao chép stack
    def copy(self):
        new_stack = Stack()
        temp_stack = Stack()
        
        # Copy tất cả phần tử sang temp_stack
        current = self.top
        while current:
            temp_stack.push(current.data)
            current = current.next
            
        # Copy từ temp_stack sang new_stack để giữ thứ tự
        while not temp_stack.isEmpty():
            new_stack.push(temp_stack.pop())
            
        return new_stack
    
    # Kiểm tra stack có phải palindrome
    def isPalindrome(self):
        if self.isEmpty():
            return True
            
        # Tạo một stack mới và copy dữ liệu
        stack_copy = self.copy()
        stack_copy.reverse()
        
        # So sánh từng phần tử
        current1 = self.top
        current2 = stack_copy.top
        
        while current1:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
            
        return True
    
    # Kiểm tra xem một stack có phải là subsequence của stack hiện tại
    def isSubsequence(self, other_stack):
        if other_stack.isEmpty():
            return True
            
        current_main = self.top
        current_sub = other_stack.top
        
        while current_main and current_sub:
            if current_main.data == current_sub.data:
                current_sub = current_sub.next
            current_main = current_main.next
            
        return current_sub is None
    
    # Xóa tất cả các phần tử có giá trị lớn hơn x
    def removeGreaterThan(self, x):
        if self.isEmpty():
            return
            
        temp_stack = Stack()
        while not self.isEmpty():
            current = self.pop()
            if current <= x:
                temp_stack.push(current)
                
        while not temp_stack.isEmpty():
            self.push(temp_stack.pop())
    
    # Sắp xếp stack theo thứ tự tăng dần
    def sort(self):
        if self.isEmpty():
            return
            
        temp_stack = Stack()
        
        while not self.isEmpty():
            temp = self.pop()
            
            while not temp_stack.isEmpty() and temp_stack.peek() > temp:
                self.push(temp_stack.pop())
                
            temp_stack.push(temp)
            
        # Copy lại vào stack gốc
        while not temp_stack.isEmpty():
            self.push(temp_stack.pop())
        
        self.reverse()  # Để có thứ tự tăng dần từ đỉnh xuống đáy
        
    # Kiểm tra xem stack có được sắp xếp chưa
    def isSorted(self):
        if self.isEmpty() or self.size == 1:
            return True
            
        temp_stack = self.copy()
        prev = temp_stack.pop()
        
        while not temp_stack.isEmpty():
            current = temp_stack.pop()
            if prev > current:  # Kiểm tra thứ tự tăng dần
                return False
            prev = current
            
        return True
        
    # Trộn hai stack đã sắp xếp
    def mergeSorted(self, other_stack):
        """Trộn hai stack đã sắp xếp thành một stack được sắp xếp"""
        if not self.isSorted() or not other_stack.isSorted():
            raise ValueError("Cả hai stack phải được sắp xếp trước")
            
        result = Stack()
        temp1 = self.copy()
        temp2 = other_stack.copy()
        
        # Sử dụng một stack phụ để đảo ngược kết quả
        temp_result = Stack()
        
        while not temp1.isEmpty() and not temp2.isEmpty():
            if temp1.peek() <= temp2.peek():
                temp_result.push(temp1.pop())
            else:
                temp_result.push(temp2.pop())
                
        # Thêm các phần tử còn lại từ stack 1
        while not temp1.isEmpty():
            temp_result.push(temp1.pop())
            
        # Thêm các phần tử còn lại từ stack 2
        while not temp2.isEmpty():
            temp_result.push(temp2.pop())
            
        # Đảo ngược kết quả để có thứ tự đúng
        while not temp_result.isEmpty():
            result.push(temp_result.pop())
            
        # Cập nhật stack hiện tại
        self.top = result.top
        self.size = result.size
        self.min_element = result.min_element

    # Lấy phần tử lớn nhất trong stack
    def getMax(self):
        if self.isEmpty():
            return None
        current = self.top
        max_val = current.data
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val
    
    # Đếm số lần xuất hiện của một giá trị
    def count(self, value):
        count = 0
        current = self.top
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count
    
    # Xoay stack n phần tử
    def rotate(self, n):
        """Xoay n phần tử từ đỉnh xuống đáy của stack"""
        if self.size <= 1 or n <= 0:
            return
            
        n = n % self.size  # Chuẩn hóa n
        temp_stack = Stack()
        
        # Lấy n phần tử đầu tiên
        for _ in range(n):
            temp_stack.push(self.pop())
            
        # Lưu phần còn lại
        remaining = Stack()
        while not self.isEmpty():
            remaining.push(self.pop())
            
        # Đưa n phần tử vào vị trí mới
        while not temp_stack.isEmpty():
            remaining.push(temp_stack.pop())
            
        # Khôi phục stack
        while not remaining.isEmpty():
            self.push(remaining.pop())
    
    # Xóa phần tử tại vị trí k từ đỉnh (1-based)
    def removeAt(self, k):
        if k <= 0 or k > self.size:
            raise ValueError("Invalid position")
            
        if k == 1:
            return self.pop()
            
        temp_stack = Stack()
        
        # Lưu k-1 phần tử đầu tiên
        for _ in range(k-1):
            temp_stack.push(self.pop())
            
        # Lấy phần tử cần xóa
        result = self.pop()
        
        # Khôi phục stack
        while not temp_stack.isEmpty():
            self.push(temp_stack.pop())
            
        return result
    
    # Chèn phần tử vào vị trí k từ đỉnh (1-based)
    def insertAt(self, value, k):
        if k <= 0 or k > self.size + 1:
            raise ValueError("Invalid position")
            
        if k == 1:
            self.push(value)
            return
            
        temp_stack = Stack()
        
        # Lưu k-1 phần tử đầu tiên
        for _ in range(k-1):
            temp_stack.push(self.pop())
            
        # Chèn phần tử mới
        self.push(value)
        
        # Khôi phục stack
        while not temp_stack.isEmpty():
            self.push(temp_stack.pop())
    
    # Kiểm tra biểu thức ngoặc
    @staticmethod
    def checkBrackets(expr):
        """Kiểm tra tính hợp lệ của biểu thức ngoặc"""
        stack = Stack()
        brackets = {')': '(', ']': '[', '}': '{'}
        
        for char in expr:
            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if stack.isEmpty():
                    return False
                if stack.pop() != brackets[char]:
                    return False
                    
        return stack.isEmpty()
    
    # Chuyển đổi biểu thức trung tố sang hậu tố
    @staticmethod
    def infixToPostfix(expr):
        """Chuyển đổi biểu thức trung tố sang hậu tố"""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = Stack()
        result = []
        
        for char in expr:
            if char.isalnum():
                result.append(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while not stack.isEmpty() and stack.peek() != '(':
                    result.append(stack.pop())
                stack.pop()  # Bỏ dấu '('
            else:
                while (not stack.isEmpty() and stack.peek() != '(' and 
                       precedence.get(char, 0) <= precedence.get(stack.peek(), 0)):
                    result.append(stack.pop())
                stack.push(char)
                
        while not stack.isEmpty():
            result.append(stack.pop())
            
        return ''.join(result)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Khởi tạo và thử nghiệm các thao tác cơ bản
    s1 = Stack()
    s1.push(3)
    s1.push(1)
    s1.push(4)
    s1.push(1)
    s1.push(5)
    
    print("Stack ban đầu:", s1.traverse())
    print("Kích thước:", s1.getSize())
    print("Phần tử nhỏ nhất:", s1.getMin())
    print("Phần tử lớn nhất:", s1.getMax())
    
    # Thử nghiệm các thao tác nâng cao
    s2 = Stack()
    s2.push(2)
    s2.push(4)
    s2.push(6)
    
    # Sắp xếp và trộn hai stack
    s1.sort()
    s2.sort()
    print("\nStack 1 sau khi sắp xếp:", s1.traverse())
    print("Stack 2 sau khi sắp xếp:", s2.traverse())
    
    s1.mergeSorted(s2)
    print("Stack sau khi trộn:", s1.traverse())
    
    # Xoay stack
    s1.rotate(2)
    print("\nSau khi xoay 2 phần tử:", s1.traverse())
    
    # Chèn và xóa tại vị trí cụ thể
    s1.insertAt(7, 3)  # Chèn 7 vào vị trí thứ 3
    print("Sau khi chèn 7 vào vị trí 3:", s1.traverse())
    
    removed = s1.removeAt(3)  # Xóa phần tử ở vị trí 3
    print(f"Đã xóa {removed} tại vị trí 3, stack sau xóa:", s1.traverse())
    
    # Kiểm tra biểu thức ngoặc
    expr1 = "(()){[]}"
    expr2 = "(()"
    print(f"\nBiểu thức '{expr1}' hợp lệ?", Stack.checkBrackets(expr1))
    print(f"Biểu thức '{expr2}' hợp lệ?", Stack.checkBrackets(expr2))
    
    # Chuyển đổi biểu thức trung tố sang hậu tố
    infix = "a+b*(c^d-e)^(f+g*h)-i"
    postfix = Stack.infixToPostfix(infix)
    print(f"\nBiểu thức trung tố: {infix}")
    print(f"Biểu thức hậu tố: {postfix}")
