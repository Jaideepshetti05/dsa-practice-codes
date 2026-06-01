class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued")

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(f"{q.dequeue()} dequeued")
