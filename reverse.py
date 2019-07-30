def reverse(pattern):
  reverse = ""
  for char in pattern:
    reverse = char + reverse
  return reverse
