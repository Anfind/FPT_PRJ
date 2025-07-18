from queue import Queue
from stack import Stack
from bst import BST, TreeNode
from doubly_linked_list import DoublyLinkedList

# Ví dụ 1: Kết hợp LinkedList và Queue - Quản lý hàng đợi ưu tiên
class PriorityTask:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority

class PriorityTaskManager:
    def __init__(self):
        self.high_priority = Queue()  # Queue cho tác vụ ưu tiên cao
        self.low_priority = Queue()   # Queue cho tác vụ ưu tiên thấp
        
    def addTask(self, task, priority):
        if priority > 5:  # Ưu tiên cao
            self.high_priority.enQueue(PriorityTask(task, priority))
        else:  # Ưu tiên thấp
            self.low_priority.enQueue(PriorityTask(task, priority))
    
    def processNextTask(self):
        # Xử lý tác vụ ưu tiên cao trước
        if not self.high_priority.isEmpty():
            task = self.high_priority.deQueue()
            return f"Xử lý tác vụ ưu tiên cao: {task.task} (priority: {task.priority})"
        elif not self.low_priority.isEmpty():
            task = self.low_priority.deQueue()
            return f"Xử lý tác vụ ưu tiên thấp: {task.task} (priority: {task.priority})"
        return "Không có tác vụ nào trong hàng đợi"

# Ví dụ 2: Kết hợp BST và Stack - Duyệt cây không đệ quy
class TreeTraversal:
    def __init__(self):
        self.bst = BST()
        self.stack = Stack()
    
    def insert_values(self, values):
        for value in values:
            self.bst.insert(value)
    
    # Duyệt theo thứ tự trước (Preorder) không đệ quy
    def preorder_iterative(self):
        if not self.bst.root:
            return []
        
        result = []
        self.stack = Stack()
        self.stack.push(self.bst.root)
        
        while not self.stack.isEmpty():
            node = self.stack.pop()
            result.append(node.data)
            
            # Push right trước để xử lý left trước (vì stack LIFO)
            if node.right:
                self.stack.push(node.right)
            if node.left:
                self.stack.push(node.left)
        
        return result
    
    # Tính tổng các node lá (node không có con)
    def sum_leaf_nodes(self):
        if not self.bst.root:
            return 0
        
        total = 0
        self.stack = Stack()
        self.stack.push(self.bst.root)
        
        while not self.stack.isEmpty():
            node = self.stack.pop()
            
            # Kiểm tra node lá
            if not node.left and not node.right:
                total += node.data
            
            if node.right:
                self.stack.push(node.right)
            if node.left:
                self.stack.push(node.left)
        
        return total

# Ví dụ 3: Round Robin Scheduler với Queue
class Process:
    def __init__(self, pid, name, burst_time):
        self.pid = pid
        self.name = name
        self.burst_time = burst_time
        self.remaining_time = burst_time

class RoundRobinScheduler:
    def __init__(self, time_quantum):
        self.ready_queue = Queue()
        self.time_quantum = time_quantum
        self.total_time = 0
        self.completed_processes = []
    
    def add_process(self, process):
        self.ready_queue.enQueue(process)
        
    def execute(self):
        while not self.ready_queue.isEmpty():
            current_process = self.ready_queue.deQueue()
            
            # Xử lý process trong quantum time
            execution_time = min(self.time_quantum, current_process.remaining_time)
            current_process.remaining_time -= execution_time
            self.total_time += execution_time
            
            print(f"Thực thi {current_process.name} trong {execution_time}ms. "
                  f"Thời gian còn lại: {current_process.remaining_time}ms")
            
            # Nếu process chưa hoàn thành, đưa lại vào queue
            if current_process.remaining_time > 0:
                self.ready_queue.enQueue(current_process)
            else:
                self.completed_processes.append({
                    'process': current_process,
                    'completion_time': self.total_time
                })

# Ví dụ 4: Message Broker với Priority Queue
class Message:
    def __init__(self, content, priority, topic):
        self.content = content
        self.priority = priority
        self.topic = topic
        self.timestamp = time.time()

class MessageBroker:
    def __init__(self):
        self.topics = {}  # Dict của các priority queue
        
    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = PriorityTaskManager()
            
    def publish(self, message):
        if message.topic not in self.topics:
            self.create_topic(message.topic)
        self.topics[message.topic].addTask(message.content, message.priority)
        
    def subscribe(self, topic_name):
        if topic_name not in self.topics:
            return None
        return self.topics[topic_name].processNextTask()

# Ví dụ 5: LRU Cache với Queue và LinkedList
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Dictionary lưu key-value
        self.usage_queue = Queue()  # Queue theo dõi thứ tự sử dụng
        self.key_count = {}  # Đếm số lần key xuất hiện trong queue
        
    def get(self, key):
        if key not in self.cache:
            return -1
            
        # Cập nhật usage
        self.usage_queue.enQueue(key)
        self.key_count[key] = self.key_count.get(key, 0) + 1
        self._cleanup()
        
        return self.cache[key]
        
    def put(self, key, value):
        # Cập nhật hoặc thêm giá trị mới
        self.cache[key] = value
        self.usage_queue.enQueue(key)
        self.key_count[key] = self.key_count.get(key, 0) + 1
        
        # Xóa phần tử cũ nhất nếu vượt quá capacity
        self._cleanup()
        
    def _cleanup(self):
        # Dọn dẹp queue và cache nếu cần
        while len(self.cache) > self.capacity:
            oldest_key = self.usage_queue.deQueue()
            self.key_count[oldest_key] -= 1
            if self.key_count[oldest_key] == 0:
                del self.cache[oldest_key]
                del self.key_count[oldest_key]

# Ví dụ sử dụng kết hợp cấu trúc dữ liệu
if __name__ == "__main__":
    import time
    
    print("=== Ví dụ 1: Quản lý tác vụ ưu tiên ===")
    task_manager = PriorityTaskManager()
    task_manager.addTask("Task 1", 7)
    task_manager.addTask("Task 2", 3)
    task_manager.addTask("Task 3", 8)
    task_manager.addTask("Task 4", 4)

    for _ in range(4):
        print(task_manager.processNextTask())

    print("\n=== Ví dụ 2: Duyệt cây nhị phân ===")
    tree = TreeTraversal()
    tree.insert_values([10, 5, 15, 3, 7, 12, 18])
    print("Duyệt preorder:", tree.preorder_iterative())
    print("Tổng các node lá:", tree.sum_leaf_nodes())
    
    print("\n=== Ví dụ 3: Round Robin Scheduler ===")
    scheduler = RoundRobinScheduler(time_quantum=3)
    processes = [
        Process(1, "P1", 8),
        Process(2, "P2", 4),
        Process(3, "P3", 6)
    ]
    for process in processes:
        scheduler.add_process(process)
    scheduler.execute()
    print("\nThứ tự hoàn thành:")
    for p in scheduler.completed_processes:
        print(f"{p['process'].name} hoàn thành tại {p['completion_time']}ms")
    
    print("\n=== Ví dụ 4: Message Broker ===")
    broker = MessageBroker()
    broker.publish(Message("Urgent Alert", 9, "system"))
    broker.publish(Message("Info Log", 5, "system"))
    broker.publish(Message("Debug Info", 3, "debug"))
    
    print("Đọc tin nhắn từ topic 'system':")
    for _ in range(2):
        print(broker.subscribe("system"))
    
    print("\n=== Ví dụ 5: LRU Cache ===")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("get(1):", cache.get(1))
    cache.put(3, 3)  # Xóa key 2
    print("get(2):", cache.get(2))
    cache.put(4, 4)  # Xóa key 3
    print("get(1):", cache.get(1))
    print("get(3):", cache.get(3))
    print("get(4):", cache.get(4))

    print("\n=== Ví dụ 6: Expression Evaluator (Stack + LinkedList) ===")
    class ExpressionEvaluator:
        def __init__(self):
            self.operators = Stack()
            self.operands = Stack()
            
        def _precedence(self, op):
            if op in ['+', '-']: return 1
            if op in ['*', '/']: return 2
            if op == '^': return 3
            return 0
            
        def _apply_operator(self):
            operator = self.operators.pop()
            b = float(self.operands.pop())
            a = float(self.operands.pop())
            if operator == '+': self.operands.push(a + b)
            elif operator == '-': self.operands.push(a - b)
            elif operator == '*': self.operands.push(a * b)
            elif operator == '/': self.operands.push(a / b)
            elif operator == '^': self.operands.push(a ** b)
            
        def evaluate(self, expression):
            tokens = expression.split()
            for token in tokens:
                if token in ['+', '-', '*', '/', '^']:
                    while (not self.operators.isEmpty() and 
                           self._precedence(self.operators.peek()) >= self._precedence(token)):
                        self._apply_operator()
                    self.operators.push(token)
                elif token == '(':
                    self.operators.push(token)
                elif token == ')':
                    while not self.operators.isEmpty() and self.operators.peek() != '(':
                        self._apply_operator()
                    self.operators.pop()  # Remove '('
                else:
                    self.operands.push(token)
                    
            while not self.operators.isEmpty():
                self._apply_operator()
            return self.operands.pop()

    print("\n=== Ví dụ 7: History Manager (Stack + LinkedList) ===")
    class HistoryManager:
        def __init__(self, max_size=10):
            self.undo_stack = Stack()
            self.redo_stack = Stack()
            self.max_size = max_size
            self.current_state = None
            
        def add_action(self, action):
            if self.current_state is not None:
                self.undo_stack.push(self.current_state)
                if self.undo_stack.getSize() > self.max_size:
                    # Remove oldest action if max size reached
                    temp_stack = Stack()
                    for _ in range(self.max_size - 1):
                        temp_stack.push(self.undo_stack.pop())
                    while not temp_stack.isEmpty():
                        self.undo_stack.push(temp_stack.pop())
            self.current_state = action
            # Clear redo stack when new action is added
            self.redo_stack = Stack()
            
        def undo(self):
            if not self.undo_stack.isEmpty():
                self.redo_stack.push(self.current_state)
                self.current_state = self.undo_stack.pop()
                return self.current_state
            return None
            
        def redo(self):
            if not self.redo_stack.isEmpty():
                self.undo_stack.push(self.current_state)
                self.current_state = self.redo_stack.pop()
                return self.current_state
            return None
            
        def get_current(self):
            return self.current_state

    # Test the new examples
    print("\nTesting Expression Evaluator:")
    evaluator = ExpressionEvaluator()
    expr = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
    print(f"Expression: {expr}")
    print(f"Result: {evaluator.evaluate(expr)}")

    print("\n=== Ví dụ 8: Multi-Level Index (BST + LinkedList) ===")
    class IndexNode:
        def __init__(self, key):
            self.key = key
            self.values = DoublyLinkedList()  # Store multiple values for same key
            self.left = None
            self.right = None

    class MultiLevelIndex:
        def __init__(self):
            self.root = None
            self.size = 0
            
        def _insert_recursive(self, node, key, value):
            if not node:
                new_node = IndexNode(key)
                new_node.values.addLast(value)
                return new_node
                
            if key == node.key:
                node.values.addLast(value)
            elif key < node.key:
                node.left = self._insert_recursive(node.left, key, value)
            else:
                node.right = self._insert_recursive(node.right, key, value)
            return node
            
        def insert(self, key, value):
            self.root = self._insert_recursive(self.root, key, value)
            self.size += 1
            
        def _find_recursive(self, node, key):
            if not node:
                return None
            if key == node.key:
                return node.values
            if key < node.key:
                return self._find_recursive(node.left, key)
            return self._find_recursive(node.right, key)
            
        def find(self, key):
            return self._find_recursive(self.root, key)
            
        def _range_search_recursive(self, node, start_key, end_key, result):
            if not node:
                return
                
            if start_key < node.key:
                self._range_search_recursive(node.left, start_key, end_key, result)
                
            if start_key <= node.key <= end_key:
                result.extend(node.values.traverseForward())
                
            if end_key > node.key:
                self._range_search_recursive(node.right, start_key, end_key, result)
                
        def range_search(self, start_key, end_key):
            result = []
            self._range_search_recursive(self.root, start_key, end_key, result)
            return result

    print("\n=== Ví dụ 9: Hierarchical Cache (BST + LinkedList) ===")
    class CacheLevel:
        def __init__(self, capacity):
            self.items = DoublyLinkedList()
            self.capacity = capacity
            self.lookup = {}  # Key to Node mapping
            
        def get(self, key):
            if key not in self.lookup:
                return None
            # Move to front (most recently used)
            value = self.lookup[key]
            self.items.removeByValue(value)
            self.items.addFirst(value)
            return value
            
        def put(self, key, value):
            if key in self.lookup:
                self.items.removeByValue(self.lookup[key])
            elif len(self.lookup) >= self.capacity:
                # Remove least recently used
                old_value = self.items.removeLast()
                old_key = next(k for k, v in self.lookup.items() if v == old_value)
                del self.lookup[old_key]
                
            self.items.addFirst(value)
            self.lookup[key] = value
            return True

    class HierarchicalCache:
        def __init__(self, levels):
            self.index = MultiLevelIndex()  # BST index for quick lookups
            self.levels = [CacheLevel(cap) for cap in levels]  # Multiple cache levels
            
        def get(self, key):
            # Search through cache levels
            for level in range(len(self.levels)):
                value = self.levels[level].get(key)
                if value:
                    # Found in this level, promote to higher levels
                    for i in range(level - 1, -1, -1):
                        self.levels[i].put(key, value)
                    return value
                    
            # If not in cache, check main index
            values = self.index.find(key)
            if values:
                value = values.head.data
                # Add to all cache levels
                for level in self.levels:
                    level.put(key, value)
                return value
            return None
            
        def put(self, key, value):
            # Add to main index
            self.index.insert(key, value)
            # Add to first (fastest) cache level
            if self.levels:
                self.levels[0].put(key, value)

    # Test the new data structures
    print("\nTesting Multi-Level Index:")
    index = MultiLevelIndex()
    data = [(5, "Apple"), (3, "Banana"), (7, "Orange"), 
            (2, "Grape"), (4, "Mango"), (5, "Pear")]
    
    for key, value in data:
        index.insert(key, value)
        
    print("Values for key 5:", [v for v in index.find(5).traverseForward()])
    print("Range search 3-6:", index.range_search(3, 6))

    print("\nTesting Hierarchical Cache:")
    cache = HierarchicalCache([2, 4, 8])  # Three levels with different capacities
    for key, value in data:
        cache.put(key, value)
        
    print("Get key 5:", cache.get(5))
    print("Get key 3:", cache.get(3))
    print("Get key 7:", cache.get(7))

    print("\n=== Ví dụ 10: Advanced Task Scheduler (Queue + Stack) ===")
    class Task:
        def __init__(self, id, name, priority, dependencies=None):
            self.id = id
            self.name = name
            self.priority = priority
            self.dependencies = dependencies or []
            self.completed = False

    class AdvancedTaskScheduler:
        def __init__(self):
            self.tasks = {}  # Task ID to Task mapping
            self.waiting_queue = Queue()  # Tasks waiting for dependencies
            self.ready_stack = Stack()    # Tasks ready to execute
            self.completed_stack = Stack() # Completed tasks for rollback
            
        def add_task(self, task):
            self.tasks[task.id] = task
            if not task.dependencies:
                self.ready_stack.push(task)
            else:
                self.waiting_queue.enQueue(task)
                
        def execute_next(self):
            if not self.ready_stack.isEmpty():
                task = self.ready_stack.pop()
                print(f"Executing task: {task.name}")
                task.completed = True
                self.completed_stack.push(task)
                
                # Check waiting tasks that might be ready now
                temp_queue = Queue()
                while not self.waiting_queue.isEmpty():
                    waiting_task = self.waiting_queue.deQueue()
                    if all(self.tasks[dep].completed for dep in waiting_task.dependencies):
                        self.ready_stack.push(waiting_task)
                    else:
                        temp_queue.enQueue(waiting_task)
                self.waiting_queue = temp_queue
                return task
            return None
            
        def rollback_last(self):
            if not self.completed_stack.isEmpty():
                task = self.completed_stack.pop()
                task.completed = False
                self.ready_stack.push(task)
                
                # Move tasks back to waiting queue if dependencies are no longer met
                temp_stack = Stack()
                while not self.ready_stack.isEmpty():
                    ready_task = self.ready_stack.pop()
                    if any(not self.tasks[dep].completed for dep in ready_task.dependencies):
                        self.waiting_queue.enQueue(ready_task)
                    else:
                        temp_stack.push(ready_task)
                while not temp_stack.isEmpty():
                    self.ready_stack.push(temp_stack.pop())
                return task
            return None

    print("\n=== Ví dụ 11: Expression Parser (Queue + Stack) ===")
    class ExpressionParser:
        def __init__(self):
            self.token_queue = Queue()  # For tokenization
            self.operator_stack = Stack()  # For parsing
            self.output_queue = Queue()   # For output in RPN
            
        def tokenize(self, expression):
            current_number = ""
            for char in expression:
                if char.isspace():
                    if current_number:
                        self.token_queue.enQueue(current_number)
                        current_number = ""
                elif char.isdigit() or char == '.':
                    current_number += char
                else:
                    if current_number:
                        self.token_queue.enQueue(current_number)
                        current_number = ""
                    self.token_queue.enQueue(char)
            if current_number:
                self.token_queue.enQueue(current_number)
                
        def _precedence(self, operator):
            precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
            return precedences.get(operator, 0)
            
        def parse(self, expression):
            self.tokenize(expression)
            
            while not self.token_queue.isEmpty():
                token = self.token_queue.deQueue()
                
                if token.replace('.', '').isdigit():
                    self.output_queue.enQueue(token)
                elif token in '+-*/^':
                    while (not self.operator_stack.isEmpty() and 
                           self.operator_stack.peek() != '(' and
                           self._precedence(self.operator_stack.peek()) >= self._precedence(token)):
                        self.output_queue.enQueue(self.operator_stack.pop())
                    self.operator_stack.push(token)
                elif token == '(':
                    self.operator_stack.push(token)
                elif token == ')':
                    while not self.operator_stack.isEmpty() and self.operator_stack.peek() != '(':
                        self.output_queue.enQueue(self.operator_stack.pop())
                    if not self.operator_stack.isEmpty():
                        self.operator_stack.pop()  # Discard '('
                        
            while not self.operator_stack.isEmpty():
                self.output_queue.enQueue(self.operator_stack.pop())
                
            return self._format_output()
            
        def _format_output(self):
            result = []
            while not self.output_queue.isEmpty():
                result.append(self.output_queue.deQueue())
            return ' '.join(result)

    # Test the new examples
    print("\nTesting Advanced Task Scheduler:")
    scheduler = AdvancedTaskScheduler()
    
    # Create tasks with dependencies
    task1 = Task(1, "Initialize System", 1)
    task2 = Task(2, "Load Configuration", 2, [1])
    task3 = Task(3, "Start Services", 2, [2])
    task4 = Task(4, "Setup Database", 3, [2])
    task5 = Task(5, "Start Application", 1, [3, 4])
    
    for task in [task1, task2, task3, task4, task5]:
        scheduler.add_task(task)
        
    print("\nExecuting tasks in order:")
    while True:
        executed = scheduler.execute_next()
        if not executed:
            break
            
    print("\nRolling back last two tasks:")
    scheduler.rollback_last()
    scheduler.rollback_last()
    
    print("\nRe-executing after rollback:")
    while True:
        executed = scheduler.execute_next()
        if not executed:
            break

    print("\nTesting Expression Parser:")
    parser = ExpressionParser()
    expressions = [
        "3 + 4 * 2 / ( 1 - 5 ) ^ 2",
        "1 + 2 * 3 - 4 / 5",
        "(10 + 20) * (30 + 40)"
    ]
    
    for expr in expressions:
        print(f"\nInput: {expr}")
        print(f"Output (RPN): {parser.parse(expr)}")

    print("\nTesting History Manager:")
    history = HistoryManager(max_size=5)
    history.add_action("Step 1")
    history.add_action("Step 2")
    history.add_action("Step 3")
    print(f"Current: {history.get_current()}")
    print(f"Undo: {history.undo()}")
    print(f"Undo: {history.undo()}")
    print(f"Redo: {history.redo()}")
    history.add_action("Step 4")
    print(f"Current after new action: {history.get_current()}")
