class drinkBill:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    def show_info(self):
        print(self.name, "-", self.amount, "-", self.price)


class Node:
    def __init__(self, value):
        self.data = value 
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enQueue(self, name, amount, price):
        # begin your code here
        # goi y: cac em bat dau code bang lenh sau:
        # newBill = drinkBill(name, amount, price)
        # sau do code tuong tu nhu ham addLast
        newBill = drinkBill(name, amount, price)
        newNode = Node(newBill)

        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode            
        # end your code here
        self.size += 1  # sau khi them du lieu thi tang size
        
    def deQueue(self):
        tmp = None
        # begin your code here
        # goi y: tuong tu nhu ham deleteFirst()
        if self.size == 0:
            return None
        tmp = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        # end your code here
        return tmp

    def createData(self, n):
        name = ["CF", "Tea", "Coca", "Pepsi", "CF", "Coca", "CF", "CF", "Tea", "Tea"]
        amount = [1, 2, 2, 3, 1, 3, 4, 4, 5, 2]
        price = [12, 12, 8, 10, 10, 8, 8, 10, 12, 8]
        if (n>=3 and n<=10):
            for i in range(n):
                self.enQueue(name[i], amount[i], price[i])

    def showQueue(self):
        print("Data in the Queue:")
        cur = self.head
        while cur is not None:
            cur.data.show_info()
            cur = cur.next
        print("---------------------")

    def f0(self):
        print("Test ham createData va enQueue:")
        self.showQueue()
        print("Test ham deQueue:")
        x = self.deQueue()
        x.show_info()

    
    def f1(self, name, amount, price):
        self.showQueue()
        # begin your code here
        if (amount < 5):
            self.enQueue(name, amount, price)
        # end your code here
        self.showQueue()
        
    
    def f2(self):
        self.showQueue()
        result = 0
        # begin your code here
        tmp = self.deQueue()  
        result = tmp.amount * tmp.price      
        # end your code here
        self.showQueue()
        return result
    
    
    def f3(self):
        self.showQueue()
        result = 0
        # begin your code here
        for i in range(3):
            result += self.deQueue().amount
        # end your code here
        self.showQueue()
        return result
    
    
    def f4(self):
        self.showQueue()
        result = None
        # begin your code here
        current_node = self.head
        maxData = 0
        while self.size > 0:
            current_bill = self.deQueue()
            if ((current_bill.amount) * (current_bill.price) > maxData):
                result = current_bill
                maxData = (current_bill.amount) * (current_bill.price)
        # end your code here
        self.showQueue()
        result.show_info()
        return result
    
    
    def f5(self):
        self.showQueue()
        result = 0
        # begin your code here
        
        # end your code here
        self.showQueue()
        return result
    
    
    def f6(self):
        self.showQueue()
        result = 0
        # begin your code here
        
        
        # end your code here
        self.showQueue()
        return result
    
    
    def f7(self):
        self.showQueue()
        result = 0
        # begin your code here
        
        
        # end your code here
        self.showQueue()
        return result
    
   

if __name__ == '__main__':
    lst = Queue()
    print("Nhap do dai cua Queue (tu 3 den 10) de phat sinh data\nsize =  ")
    n = input()
    n = int(n)
    lst.createData(n)

    print("Data trong Queue da khoi tao xong")
    print("Ban muon lam gi?")
    print("0. test ham createData, enQueue, va deQueue")
    print("1. test f1")
    print("2. test f2")
    print("3. test f3")
    print("4. test f4")
    print("5. test f5")
    print("6. test f6")
    print("7. test f7")
    
    print("Default: thoat chuong trinh")
    choice = input()
    choice = int(choice)
    print('OUTPUT:')
    if (choice == 0):
        lst.f0()
    if (choice == 1):
        lst.f1("Coca", 10, 10)
        lst.f1("Coca", 3, 10)
    if (choice == 2):
        r = lst.f2()
        print("Ket Qua:")
        print(r)
    if (choice == 3):
        r = lst.f3()
        print("Ket Qua:")
        print(r)
    if (choice == 4):
        r = lst.f4()
        print("Ket Qua:")
        print(r)
    if (choice == 5):
        r = lst.f5()
        print("Ket Qua:")
        print(r)
    if (choice == 6):
        r = lst.f6()
        print("Ket Qua:")
        print(r)
    if (choice == 7):
        r = lst.f7()
        print("Ket Qua:")
        print(r)
    
    