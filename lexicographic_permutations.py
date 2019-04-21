digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation_list = []

for digit_1 in digits:
  for digit_2 in digits:
    if digit_2 != digit_1:
      for digit_3 in digits:
        if (digit_3 != digit_1) & (digit_3 != digit_2):
          for digit_4 in digits:
            if (digit_4 != digit_1) & (digit_4 != digit_2) & (digit_4 != digit_3):
              for digit_5 in digits:
                if (digit_5 != digit_1) & (digit_5 != digit_2) & (digit_5 != digit_3) & (digit_5 != digit_4):
                  for digit_6 in digits:
                    if (digit_6 != digit_1) & (digit_6 != digit_2) & (digit_6 != digit_3) & (digit_6 != digit_4) & (digit_6 != digit_5):
                      for digit_7 in digits:
                        if (digit_7 != digit_1) & (digit_7 != digit_2) & (digit_7 != digit_3) & (digit_7 != digit_4) & (digit_7 != digit_5) & (digit_7 != digit_6):
                          for digit_8 in digits:
                            if (digit_8 != digit_1) & (digit_8 != digit_2) & (digit_8 != digit_3) & (digit_8 != digit_4) & (digit_8 != digit_5) & (digit_8 != digit_6) & (digit_8 != digit_7):
                              for digit_9 in digits:
                                if (digit_9 != digit_1) & (digit_9 != digit_2) & (digit_9 != digit_3) & (digit_9 != digit_4) & (digit_9 != digit_5) & (digit_9 != digit_6) & (digit_9 != digit_7)  & (digit_9 != digit_8):
                                  for digit_10 in digits:
                                    if (digit_10 != digit_1) & (digit_10 != digit_2) & (digit_10 != digit_3) & (digit_10 != digit_4) & (digit_10 != digit_5) & (digit_10 != digit_6) & (digit_10 != digit_7)  & (digit_10 != digit_8)  & (digit_10 != digit_9):
                                      permutation_list.append(str(digit_1) + str(digit_2) + str(digit_3) + str(digit_4) + str(digit_5) + str(digit_6) + str(digit_7) + str(digit_8) + str(digit_9) + str(digit_10))
print(permutation_list[999999])