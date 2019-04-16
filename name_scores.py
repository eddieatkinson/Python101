import string
lower_case_alphabet = list(string.ascii_uppercase)
f = open('p022_names.txt', 'r')
names = f.read()
names_without_first_and_last = names[1:-1]
names_as_list = names_without_first_and_last.split('","')
# names_as_list = ['Eddie', 'Marcus', 'Jennifer']
number_of_names = len(names_as_list)

def get_name_score(i):
  name_number_in_list = i + 1
  letter_value_sum = 0
  for letter in names_as_list[i]:
    letter_value = lower_case_alphabet.index(letter) + 1
    letter_value_sum += letter_value
  name_score = name_number_in_list * letter_value_sum
  # print(names_as_list[i])
  # print(name_score)
  return name_score

def get_total_of_all_name_scores(length):
  total_of_all_name_scores = 0
  for i in range(length):
    total_of_all_name_scores += get_name_score(i)
  return total_of_all_name_scores

print(get_total_of_all_name_scores(number_of_names))