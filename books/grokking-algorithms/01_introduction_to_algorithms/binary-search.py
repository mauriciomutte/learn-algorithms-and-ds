def binary_search(listItems, item):
  low = 0
  high = len(listItems) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = listItems[mid]

    if (guess == item):
      return mid
    if (guess > item):
      high = mid - 1
    else:
      low = mid + 1

  return None
