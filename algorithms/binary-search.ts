function binarySearch<T>(listItems: T[], item: T) {
  let low = 0
  let high = listItems.length - 1

  while (low <= high) {
    const mid = Math.floor((low + high) / 2)
    const guess = listItems[mid]

    if (guess === item) {
      return mid
    }

    if (guess > item) {
      high = mid - 1
    }

    if (guess < item) {
      low = mid + 1
    }
  }

  return null
}
