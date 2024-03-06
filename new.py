# Create a range object
r = range(3)

# Create the first iterator from the range object
it1 = iter(r)

# Iterate over the first iterator
print(next(it1))  # Output: 0
print(next(it1))  # Output: 1

# Create the second iterator from the same range object
it2 = iter(r)

# Iterate over the second iterator
print(next(it2))  # Output: 0 (it starts again from the beginning)
print(next(it2))  # Output: 1

# The first iterator is unaffected by the iteration of the second iterator
print(next(it1))  # Output: 2
