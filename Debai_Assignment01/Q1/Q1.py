class Laptop:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_info(self):
        print(self.name, "-", self.price)


class Node:
    def __init__(self, value):
        self.data = value  # value o day la Laptop
        self.next = None
        self.prev = None


class Doubly_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, name, price):
        newLt = Laptop(name, price)
        newNode = Node(newLt)
        if (self.size == 0):  # list rong
            self.head = newNode
            self.tail = newNode
        else:  # list da co du lieu
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        # sau khi them du lieu thi tang size
        self.size += 1  
        
    def createData(self, n):
        name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        price = [12, 32, 18, 9, 50, 37, 7, 10, 29, 49]
        if (n>=3 and n<=10):
            for i in range(n):
                self.add_last(name[i], price[i])

    def show_fw(self):
        # show info from head to tail
        current = self.head
        while current:
            current.data.show_info()
            current = current.next

    def show_bw(self):
        # show info from tail to head
        current = self.tail
        while current:
            current.data.show_info()
            current = current.prev

    def f1(self):
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f2(self, name, price): #Thêm phần tử đã cho vào vị trí đầu tiên 
        # begin your code here
        newLt = Laptop(name, price)
        newNode = Node(newLt)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()
    
    def f3(self): # Xoá phần tử thứ hai của list 
        # begin your code here
        second = self.head.next
        if second.next:
            self.head.next = second.next
            second.next.prev = self.head
        else:
            self.head.next = None
            self.tail = self.head
        self.size -= 1
        second = None
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f4(self): #Xoá phần tử áp chót của list 
        # begin your code here
        if self.size < 2:
            return
        if self.size == 2:
            self.head = self.tail
            self.head.prev = None
            self.size -= 1
        else:
            second_last = self.tail.prev
            before_second_last = second_last.prev
            before_second_last.next = self.tail
            self.tail.prev = before_second_last
            self.size -= 1
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f5(self): #Đếm số lượng Laptop có giá lớn hơn 10 
        result = 0
        # begin your code here
        current = self.head
        while current:
            if current.data.price > 10:
                result += 1
            current = current.next
        # end your code here
        return result

    def f6(self): #Tính giá trung bình của 5 Laptop cuối cùng (giả sử list có từ 5 node trở lên)
        result = 0
        # begin your code here
        if self.size < 5:
            return 0
        current = self.tail
        total = 0
        count = 0
        while current and count < 5:
            total += current.data.price
            current = current.prev
            count += 1
        result = total / 5
        # end your code here
        return result

    def f7(self):
        result = 0
        # begin your code here
        current = self.head
        lst = []
        while current:
            lst.append(current.data.price)
            current = current.next
        lst.sort(reverse=True)
        for i in lst:
            if i < lst[0]:
                result = i
                break
        # end your code here
        return result

    def f8(self):#Giảm giá 10% cho tất cả Laptop có giá trên 20 (làm tròn kết quả thành số nguyên,dùng lệnh p.data.price = round(p.data.price*0.9)) 
        # begin your code here
        p = self.head
        while p:
            if p.data.price > 20:
                p.data.price = round(p.data.price * 0.9)
            p = p.next
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f9(self): #Đảo vị trí của phần tử đầu tiên và phần tử cuối cùng của list 
        # begin your code here
        if self.size <= 1:
            return
        temp = self.head.data
        self.head.data = self.tail.data
        self.tail.data = temp
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()


    def f10(self):  # Đảo chiều list 
        # begin your code here
        if self.size <= 1:
            return
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f11(self):  # Xoá tất cả Laptop có giá trên 15
        # begin your code here
        current = self.head
        while current:
            next_node = current.next  
            
            if current.data.price > 15:
                if current == self.head:  # First node
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:  # Last node
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:  # Middle node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                self.size -= 1
            
            current = next_node  
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()


if __name__ == '__main__':
    lst = Doubly_LinkedList()
    print("nhap do dai cua list (tu 3 den 10) de phat sinh list\nsize =  ")
    n = input()
    n = int(n)
    lst.createData(n)

    print("List da khoi tao xong")
    print("Ban muon lam gi?")
    print("1. show list")
    print("2. them phan tu dau tien")
    print("3. xoa phan tu thu hai")
    print("4. xoa phan tu ap chot")
    print("5. dem so luong Laptop co price>10")
    print("6. tinh price trung binh cua 5 laptop cuoi cung trong list (gia su list co nhieu hon 5 phan tu)")
    print("7. Laptop dat tien thu hai trong list co gia bao nhieu")
    print("8. giam gia 10% cho tat ca Laptop co gia tren 20")
    print("9. dao vi tri cua Laptop dau tien va cuoi cung trong list")
    print("10. dao chieu list")
    print("11. xoa tat ca Laptop co gia tren 15")
    print("Default: thoat chuong trinh")
    choice = input()
    choice = int(choice)
    print('OUTPUT:')
    
    if (choice == 1):
        lst.f1()
    if (choice == 2):
        lst.f2("New", 20)
    if (choice == 3):
        lst.f3()
    if (choice == 4):
        lst.f4()
    if (choice == 5):
        r = lst.f5()
        print(r)
    if (choice == 6):
        r = lst.f6()
        print(r)
    if (choice == 7):
        r = lst.f7()
        print(r)
    if (choice == 8):
        lst.f8()
    if (choice == 9):
        lst.f9()
    if (choice == 10):
        lst.f10()
    if (choice == 11):
        lst.f11()