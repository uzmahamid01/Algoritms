class Queue(object):
    def __init__(self):
        self.q = []

    def enqueue(self,item):
        self.q.insert(0, item)

    def dequeue(self):
        return self.q.pop()
    
    def size(self):
        return len(self.q)
    

def main():
    q = Queue()

    # Enqueue some items
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Dequeue and print items
    print(q.q)

    # Enqueue some more items
    q.enqueue(4)
    q.enqueue(5)

    # Print the size of the queue
    print("Size of queue:", q.size())

    # Dequeue and print remaining items
    while q.size() >= 3:
        print(q.dequeue())

if __name__ == "__main__":
    main()