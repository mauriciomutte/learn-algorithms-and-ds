class ListNode<T> {
  public value: T
  public next: ListNode<T> | null

  constructor(value: T) {
    this.value = value
    this.next = null
  }
}

class SinglyLinkedList<T> {
  public length: number
  public head: ListNode<T> | null

  constructor() {
    this.head = null
    this.length = 0
  }

  prepend(item: T): void {
    const newNode = new ListNode(item)
    newNode.next = this.head
    this.head = newNode
    this.length++
  }

  append(item: T): void {
    const newNode = new ListNode(item)

    if (this.head === null) {
      this.head = newNode
      this.length++
      return
    }

    let currentNode = this.head
    while (currentNode.next !== null) {
      currentNode = currentNode.next
    }

    currentNode.next = newNode
    this.length++
  }

  insertAt(item: T, index: number): void {
    if (index < 0 || index >= this.length) {
      throw new Error(`Index ${index} is out of bounds`)
    }

    if (index === 0 || this.head === null) {
      this.prepend(item)
      return
    }

    const newNode = new ListNode(item)
    let currentNode = this.head
    let currentIndex = 0
    while (currentIndex < index - 1) {
      currentNode = currentNode.next!
      currentIndex++
    }

    newNode.next = currentNode.next
    currentNode.next = newNode
    this.length++
  }

  remove(item: T): T | undefined {
    if (this.head === null) {
      return undefined
    }

    if (this.head.value === item) {
      const removedNode = this.head
      this.head = this.head.next
      this.length--
      return removedNode.value
    }

    let currentNode = this.head
    while (currentNode.next !== null) {
      if (currentNode.next.value === item) {
        const removedNode = currentNode.next
        currentNode.next = removedNode.next
        this.length--
        return removedNode.value
      }

      currentNode = currentNode.next
    }

    return undefined
  }

  removeAt(index: number): T | undefined {
    if (index < 0 || index >= this.length) {
      throw new Error(`Index ${index} is out of bounds`)
    }

    if (this.head === null) {
      return undefined
    }

    if (index === 0) {
      const removedNode = this.head
      this.head = this.head.next
      this.length--
      return removedNode.value
    }

    let currentNode = this.head
    let currentIndex = 0
    while (currentIndex < index - 1) {
      currentNode = currentNode.next!
      currentIndex++
    }

    const removedNode = currentNode.next!
    currentNode.next = removedNode.next
    this.length--
    return removedNode.value
  }

  get(index: number): T | undefined {
    if (index < 0 || index >= this.length) {
      throw new Error(`Index ${index} is out of bounds`)
    }

    if (this.head === null) {
      return undefined
    }

    let currentNode = this.head
    let currentIndex = 0
    while (currentIndex < index) {
      currentNode = currentNode.next!
      currentIndex++
    }

    return currentNode.value
  }
}
