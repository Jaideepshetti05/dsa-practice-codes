public class CircularQueue {
    int[] queue;
    int front, rear, size, capacity;

    public CircularQueue(int capacity) {
        this.capacity = capacity;
        queue = new int[capacity];
        front = -1;
        rear = -1;
        size = 0;
    }

    public void enqueue(int item) {
        if (size == capacity) return;
        if (front == -1) front = 0;
        rear = (rear + 1) % capacity;
        queue[rear] = item;
        size++;
    }

    public int dequeue() {
        if (size == 0) return -1;
        int item = queue[front];
        front = (front + 1) % capacity;
        size--;
        if (size == 0) { front = -1; rear = -1; }
        return item;
    }

    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(5);
        cq.enqueue(10);
        cq.enqueue(20);
        cq.enqueue(30);
        System.out.println(cq.dequeue() + " dequeued");
    }
}
