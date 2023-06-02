function linearSearch<T>(haystack: T[], needle: T): boolean {
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle) {
      return true
    }
  }

  return false
}
