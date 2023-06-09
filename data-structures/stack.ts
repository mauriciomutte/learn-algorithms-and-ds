type StackNode<T> = {
  value: T
  prev?: StackNode<T>
}

class Stack<T> {
  public length: number
  private head?: StackNode<T>

  constructor() {
    this.length = 0
    this.head = undefined
  }

  push(item: T): void {
    const node = { value: item } as StackNode<T>

    this.length++
    if (!this.head) {
      this.head = node
      return
    }

    node.prev = this.head
    this.head = node
  }

  pop(): T | undefined {
    if (!this.head) return undefined

    const head = this.head
    this.head = head.prev
    this.length--

    return head.value
  }

  peek(): T | undefined {
    return this.head?.value
  }
}
