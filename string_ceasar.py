import string
alpha_list = list(string.ascii_lowercase)
user_message = raw_input("What is your message? ")
user_msg_list = list(user_message)
for i in range (0, len(user_msg_list)):
 	for j in range (0, len(alpha_list)):
 		if (user_msg_list[i] == alpha_list[j]):
 			user_msg_list[i] = alpha_list[j - 13]
 			break
new_msg_str = "".join(user_msg_list)
print new_msg_str