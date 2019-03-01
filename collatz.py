count = 0
num = 0
highest_count = 0
highest_count_num = 0

def collatz(num, count):
  count += 1
  if num == 1:
    return count
  if num % 2 == 0:
    return collatz(num / 2, count)
  else:
    return collatz((3 * num) + 1, count)

while num < 1000000:
  num += 1
  this_count = collatz(num, count)
  if this_count > highest_count:
    highest_count = this_count
    highest_count_num = num

  
print(highest_count_num, highest_count)
