class Room:
    def __init__(self, code=None, status=0,size=0,price=0):
        self.code = code
        self.status = status
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.status}, {self.size}, {self.price}"

class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class dataList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addLast(self, code, status,size, price):
        new_node = Node(Room(code, status, size, price))
        if (size >0 and price>0 and (status ==0 or status ==1)):
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

    def display(self):
        print("Data List:")
        if (self.head is None):
            print("Empty")
        current = self.head
        while current:
            print(current.info)
            current = current.next
        print("=========")

    def loadData(self, l):
        data = ['001', 0, 10, 200,
                '002', 1, 0, 50,
                '003', 0, 3, 70,
                '004', 0, 4, 100,
                '005', 0, 3, 70,
                '101', 1, 5, 120,
                '102', 0, 4, 100,
                '103', 0, 3, 80,
                '104', 0, 3, 70,
                '105', 1, 6, -10]
        for i in range(l):
            self.addLast(data[4*i], data[4*i+1], data[4*i+2], data[4*i+3])

class requestQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self,size, price):
        new_node = Node(Room(size=size, price=price))
        if (size >0 and price >0):
            if self.front is None:
                self.front = new_node
                self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node
    def deQueue(self):
        tmp = None
        if self.front != None:
            tmp = self.front.info
            self.front = self.front.next
        if self.front == None:
            self.rear = None
        return tmp

    def display(self):
        print("Request Queue:")
        if (self.front is None):
            print("Empty")
        current = self.front
        while current:
            print(str(current.info.size) + str(", ") + str(current.info.price))
            current = current.next
        print("=========")

    def loadRequest(self, l):
        data = [1, 100,
                0, 500,
                12, 500,
                4, 50,
                4, 400,
                3, 120,
                2, 300,
                5, 90,
                3, 200,
                4, 15]
        for i in range(l):
            self.enQueue(data[2*i], data[2*i+1])

class Hotel:
    def __init__(self):
        self.data = dataList()
        self.request = requestQueue()

    def load(self, m, n):
        self.data.loadData(m)
        self.request.loadRequest(n)

    def display(self):
        self.data.display()
        self.request.display()

    # This function is used for Question 1
    def f1(self,m,n):
        self.load(m,n)
        self.display()

    def rent(self, t1):
        p = self.data.head
        bestRoom = Room()
        bestRoom.price = 999999
        while (p != None):
            if (p.info.status == 0
                and p.info.size >= t1.size
                and p.info.price <= t1.price
                and p.info.price < bestRoom.price):
                bestRoom = p.info
            p = p.next
        if (bestRoom.price != 999999):
            bestRoom.status = 1
    def f2(self):
        t1 = self.request.deQueue()
        if (t1 != None):
            self.rent(t1)

    def f3(self):
        t1 = self.request.deQueue()
        while (t1 != None):
            self.rent(t1)
            t1 = self.request.deQueue()

    def f4(self):
        count = 0
        self.f3()
        p = self.data.head
        while (p != None):
            if p.info.status == 0:
                count+=1
            p = p.next
        return count


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    ds = Hotel()
    m = int(input("Input the number of Room (from 1 to 10):\nm =   "))
    while (m < 1 or m > 10):
        m = int(input("Please input the number of Room (from 1 to 10):\nm =   "))
    n1 = int(input("Input the number of requests in the request_queue (from 1 to 10):\nn =   "))
    while (n1 < 1 or n1 > 10):
        n1 = int(input("Please input the number of requests in the request_queue (from 1 to 10):\nn =   "))

    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    n = int(input("Input a question (1=>4) : "))
    if n == 1:
        print("OUTPUT:")
        ds.f1(m,n1)

    if n == 2:
        ds.load(m,n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f2()
        print("After")
        ds.display()

    if n == 3:
        ds.load(m, n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f3()
        print("After")
        ds.display()

    if n == 4:
        ds.load(m, n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        c = ds.f4()
        print("After")
        ds.display()
        print("Available Room(s): " + str(c))



# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ================================