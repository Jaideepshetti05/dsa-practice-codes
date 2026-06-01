class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, value):
        if ((self.tail + 1) % self.k == self.head):
            return False
        if (self.head == -1):
            self.head = 0
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        return True

    def dequeue(self):
        if (self.head == -1):
            return False
        if (self.head == self.tail):
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return True

if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print("Enqueued items. Head is at index:", cq.head)
