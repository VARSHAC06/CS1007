class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class Queue:
    def __init__(self):
        self.front_node = self.rear_node = None

    def is_empty(self): return self.front_node is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear_node: self.rear_node.next = new_node
        else: self.front_node = new_node
        self.rear_node = new_node

    def front(self):
        if self.is_empty(): raise IndexError("Queue is empty")
        return self.front_node.data

    def dequeue(self):
        if self.is_empty(): raise IndexError("Queue is empty")
        data = self.front_node.data
        self.front_node = self.front_node.next
        if not self.front_node: self.rear_node = None
        return data

if __name__ == "__main__":
    q = Queue()
    while True:
        choice = input("\n1. Enqueue\n2. Dequeue\n3. Front\n4. Check Empty\n5. Exit\nChoice: ")
        if choice == "1": q.enqueue(input("Value: "))
        elif choice == "2": print(f"Dequeued: {q.dequeue()}" if not q.is_empty() else "Queue is empty")
        elif choice == "3": print(f"Front: {q.front()}" if not q.is_empty() else "Queue is empty")
        elif choice == "4": print("Empty" if q.is_empty() else "Not empty")
        elif choice == "5": break
        else: print("Invalid choice.")

