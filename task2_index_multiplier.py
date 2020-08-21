def index_multiplier(lst):
  sum_lst = []
  if len(lst):
    for index, number in enumerate(lst):
      sum_lst.append(number * index)
    return sum(sum_lst)
  return 0


print(index_multiplier([1, 2, 3, 4, 5]))
print(index_multiplier([]))