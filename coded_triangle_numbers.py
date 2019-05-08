import string

alphabet = list(string.ascii_uppercase)
f = open('p042_words.txt', 'r')
words = f.read()
words_without_first_and_last = words[1:-1]
words_as_list = words_without_first_and_last.split('","')

def get_word_score(i):
  word_number_in_list = i + 1
  letter_value_sum = 0
  for letter in words_as_list[i]:
    letter_value = alphabet.index(letter) + 1
    letter_value_sum += letter_value
  word_score = letter_value_sum
  return word_score

def get_list_of_triangle_numbers():
  list_of_triangle_numbers = []
  for i in range(1, 100):
    triangle_number = int((i / 2) * (i + 1))
    list_of_triangle_numbers.append(triangle_number)
  return list_of_triangle_numbers

list_of_tri = get_list_of_triangle_numbers()
number_of_triangle_words = 0
for i in range(len(words_as_list)):
  if get_word_score(i) in list_of_tri:
    number_of_triangle_words += 1
  print(get_word_score(i))

print(number_of_triangle_words)

