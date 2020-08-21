def find_even_nums(number):
  return [x for x in range(number + 1) if x != 0 and
  x % 2 == 0]

print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(1))