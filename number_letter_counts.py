one = 'one'
two = 'two'
three = 'three'
four = 'four'
five = 'five'
six = 'six'
seven = 'seven'
eight = 'eight'
nine = 'nine'
ten = 'ten'
eleven = 'eleven'
twelve = 'twelve'
thirteen = 'thirteen'
fourteen = 'fourteen'
fifteen = 'fifteen'
sixteen = 'sixteen'
seventeen = 'seventeen'
eighteen = 'eighteen'
nineteen = 'nineteen'
twenty = 'twenty'
thirty = 'thirty'
forty = 'forty'
fifty = 'fifty'
sixty = 'sixty'
seventy = 'seventy'
eighty = 'eighty'
ninety = 'ninety'
hundred = 'hundred'
thousand = 'thousand'
ampersand = 'and'

one_through_nineteen = ['', one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]
tens_place = ['', twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety]

# total_numbers = ''

def get_one_through_ninety_nine():
  total_numbers = ''
  for tens in tens_place:
    if tens == '':
      for num in one_through_nineteen:
        total_numbers += tens + num
    else:
      for i in range(10):
        total_numbers += tens + one_through_nineteen[i]
  return total_numbers

def get_one_through_one_thousand():
  total_numbers = 10 * get_one_through_ninety_nine()
  total_numbers += (99 * 9) * ampersand
  for i in range(1, 10):
    total_numbers += 100 * (one_through_nineteen[i] + hundred)
  total_numbers += one + thousand
  return total_numbers

print(len(get_one_through_one_thousand()))
