constant = ''
i = 1

while len(constant) < 1000001:
  constant += str(i)
  i += 1

print(int(constant[0]) * int(constant[99]) * int(constant[999]) * int(constant[9999]) * int(constant[99999]) * int(constant[999999]))
