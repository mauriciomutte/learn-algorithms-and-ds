type QNode<T> = {
  value: T
  next?: QNode<T>
}

class Queue<T> {
  public length: number
  public head?: QNode<T>
  public tail?: QNode<T>

  constructor() {
    this.length = 0
    this.head = this.tail = undefined
  }

  enqueue(item: T): void {
    const node: QNode<T> = { value: item }

    if (!this.head) {
      this.head = this.tail = node
    }

    if (this.tail) {
      this.tail.next = node
      this.tail = node
    }

    this.length++
  }

  deque(): T | undefined {
    if (!this.head) return undefined

    this.length--

    const head = this.head
    this.head = head.next

    head.next = undefined

    return head.value
  }

  peek(): T | undefined {
    return this.head?.value
  }
}
