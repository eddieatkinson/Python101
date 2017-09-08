num_matr1 = [[7, 3],[-2, 4]]
num_matr2 = [[3, 4], [3, 5]]
new_matr = [[],[]]
# print num_matr1[1][0]
for i in range(0, len(num_matr1)):
 	for j in range (0, len(num_matr1)):
 		new_matr[i].append(num_matr1[i][j] + num_matr2[i][j])
 		#print num_matr2[i][j]
 		#new_matr[i][j] = num_matr1[i][j] + num_matr2[i][j]
print new_matr
		
