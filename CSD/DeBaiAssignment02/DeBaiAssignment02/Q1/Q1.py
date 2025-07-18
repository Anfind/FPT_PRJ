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
        newBill = drinkBill(name, amount, price)
        # sau do code tuong tu nhu ham addLast
        newNode = Node(newBill)
        if self.head is None:
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
        if self.head is not None:
            tmp = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
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
        #Thêm dữ liệu vào queue, trong đó, giá trị amount phải nhỏ hơn 5. Nếu amount lớn hơn 5 thì không cần thêm. Không trả về giá trị
        self.showQueue()
        # begin your code here
        if amount < 5:
            self.enQueue(name, amount, price)
        # end your code here
        self.showQueue()
        
    
    def f2(self):
        #Phục vụ cho khách hàng đầu tiên trong queue, trả về số tiền thu được
        self.showQueue()
        result = 0
        # begin your code here
        if self.head is not None:
            first_bill = self.deQueue()
            result = first_bill.amount * first_bill.price
        # end your code here
        self.showQueue()
        return result
    
    
    def f3(self):
        #Phục vụ cho 03 khách hàng đầu tiên trong queue, trả về tổng số lượng (amount) thu được
        self.showQueue()
        result = 0
        # begin your code here
        count = 0
        while count < 3 and self.head is not None:
            first_bill = self.deQueue()
            result += first_bill.amount
            count += 1
        # end your code here
        self.showQueue()
        return result
    
    def f4(self):
        #Phục vụ cho tất cả khách hàng trong queue, trả về bill có số tiền thu được lớn nhất (giả sử chỉ có 01 giá trị lớn nhất)
        self.showQueue()
        result = None
        # begin your code here
        max_revenue = 0
        max_bill = None
        while self.head is not None:
            bill = self.deQueue()
            revenue = bill.amount * bill.price
            if revenue > max_revenue:
                max_revenue = revenue
                max_bill = bill
        result = max_bill
        # end your code here
        self.showQueue()
        print("Ket Qua:")
        max_bill.show_info()
        return result
    
    
    def f5(self):
        #Giả sử quán chỉ còn tối đa 2 ly CF, hãy phục vụ nhiều khách hàng nhất có thể và tính tổng số tiền thu được
        self.showQueue()
        result = 0
        # begin your code here
        cf_remaining = 2
        while self.head is not None:
            bill = self.deQueue()
            if bill.name == "CF":
                if cf_remaining >= bill.amount:
                    cf_remaining -= bill.amount
                    result += bill.amount * bill.price
            else:
                result += bill.amount * bill.price
        # end your code here
        self.showQueue()
        return result
    
    
    def f6(self):
        #Phục vụ cho tất cả khách hàng trong queue, trả về món có số lượng được gọi nhiều nhất
        self.showQueue()
        result = ""
        # begin your code here
        drink_count = {}
        while self.head is not None:
            bill = self.deQueue()
            if bill.name in drink_count:
                drink_count[bill.name] += bill.amount
            else:
                drink_count[bill.name] = bill.amount
        
        max_amount = 0
        for drink_name, amount in drink_count.items():
            if amount > max_amount:
                max_amount = amount
                result = drink_name
        # end your code here
        self.showQueue()
        return result
    
    
    def f7(self):
        #Giả sử lượng đá và đường trong quán chỉ còn đủ cho 10 ly, quán sẽ phục vụ cho tối đa bao nhiêu người?
        self.showQueue()
        result = 0
        # begin your code here
        total_drinks = 10
        customers_served = 0
        while self.head is not None and total_drinks > 0:
            bill = self.deQueue()
            if bill.amount <= total_drinks:
                total_drinks -= bill.amount
                customers_served += 1
            else:
                break
        result = customers_served
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
        # print(r)
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
    
    