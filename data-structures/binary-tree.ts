class BinaryTree<T> {
  public root: BinaryTree<T>
  public left?: BinaryTree<T>
  public right?: BinaryTree<T>

  constructor(value: T) {
    this.root = new BinaryTree(value)
    this.left = undefined
    this.right = undefined
  }

  insertLeft(value: T) {
    const node = new BinaryTree(value)

    if (!this.left) {
      this.left = node
    } else {
      node.left = this.left
      this.left = node
    }
  }

  insertRight(value: T) {
    const node = new BinaryTree(value)

    if (!this.right) {
      this.right = node
    } else {
      node.right = this.right
      this.right = node
    }
  }
}
