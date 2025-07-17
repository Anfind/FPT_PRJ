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
        # begin your code here
        current = self.head
        while current is not None:
            current.data.show_info()
            current = current.next
        # end your code here

    def show_bw(self):
        # show info from tail to head
        # begin your code here
        current = self.tail
        while current is not None:
            current.data.show_info()
            current = current.prev
        # end your code here

    def f1(self):
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f2(self, name, price):
        # begin your code here
        current = self.head
        if current is not None:
            newLT = Laptop(name, price)
            newNode = Node(newLT)
            current.prev = newNode
            newNode.next = current
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
        
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()
    
    def f3(self):
        # begin your code here
        if self.size < 2:
            return
        second_node = self.head.next
        self.head.next = second_node.next
        if (second_node.next is not None):
            second_node.next.prev = self.head
        else:
            self.tail = self.head        
        self.size -= 1
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f4(self):
        # begin your code here
        if self.size < 2:
            return
        semiLast_mode = self.tail.prev
        self.tail.prev = semiLast_mode.prev
        semiLast_mode.prev.next = self.tail
        self.size -= 1
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f5(self):
        result = 0
        # begin your code here
        current_node = self.head
        while current_node is not None:
            if( current_node.data.price > 10):
                result += 1
            current_node = current_node.next
        # while current_node 
        # end your code here
        return result

    def f6(self):
        result = 0
        # begin your code here
        current_node = self.tail
        for i in range(5):
            result += current_node.data.price
            current_node = current_node.prev
        result = result/5
        # end your code here
        return result

    def maxPriceLap(self):
        current_node = self.head
        max = 0
        res = self.head
        while current_node is not None:
            if (current_node.data.price > max):
                res = current_node
            current_node = current_node.next
        return res
    
    def f7(self):
        result = 0
        # begin your code here
        current_node = self.head
        max = 0
        while current_node is not None:
            if (current_node.data.price > max):
                result = max
                max = current_node.data.price
            elif(current_node.data.price > result and current_node.data.price < max ):
                result = current_node.data.price
            current_node = current_node.next
        # end your code here
        return result

    def f8(self):
        # begin your code here
        current_node = self.head
        while current_node is not None:
            if( current_node.data.price > 20):
                current_node.data.price = round(current_node.data.price*0.9)
            current_node = current_node.next        
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f9(self):
        # begin your code here
        first = self.head
        last = self.tail
        # Swap nodes, not just data
        # Adjust neighbors of first and last
 
        # Save neighbors
        first_next = first.next
        last_prev = last.prev

        # Swap prev pointers
        if last_prev:
        last_prev.next = first
        if first_next:
        first_next.prev = last

        # Swap next pointers
        first.next, last.next = last.next, first_next
        first.prev, last.prev = last_prev, first.prev

        # Update head and tail
        self.head, self.tail = last, first
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()


    def f10(self):
        # begin your code here

        
        # end your code here
        print("from head to tail:")
        self.show_fw()
        print("\nfrom tail to head:")
        self.show_bw()

    def f11(self):
        # begin your code here

        
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