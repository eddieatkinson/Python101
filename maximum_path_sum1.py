# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

y = '''3
7 4
2 4 6
8 5 9 3'''

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

x = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

# print(list(x))

def multi_line_string_to_array_of_rows(multi_line_str):
  array_of_rows = multi_line_str.split('\n')
  return array_of_rows

def row_to_array(row):
  arr = row.split()
  return arr

def multi_line_string_to_array_of_arrays(multi_line_string):
  array_of_rows = multi_line_string_to_array_of_rows(multi_line_string)
  array_of_rows_of_arrays = []
  for row in array_of_rows:
    arr = row_to_array(row)
    array_of_rows_of_arrays.append(arr)
  return array_of_rows_of_arrays

def get_greatest_value_in_array_of_strings(array_of_strings):
  greatest_value = 0
  index = -1
  for string in array_of_strings:
    index += 1
    value_as_int = int(string)
    if value_as_int > greatest_value:
      greatest_value = value_as_int
      index_of_greatest_value = index
  return [greatest_value, index_of_greatest_value]

def get_maximum_path_sum(multi_line_string):
  maximum_path_sum = 0
  array_of_arrays = multi_line_string_to_array_of_arrays(x)
  for row in array_of_arrays:
    greatest_value_in_array_of_strings = get_greatest_value_in_array_of_strings(row)
    maximum_path_sum += greatest_value_in_array_of_strings
  return maximum_path_sum

print(get_maximum_path_sum(y))
