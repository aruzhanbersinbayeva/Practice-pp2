nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))

nums = [10, 5, 8, 3]
print(list(filter(lambda x: x > 5, nums)))

words = ["hi", "hello", "a"]
print(list(filter(lambda x: len(x) > 2, words)))