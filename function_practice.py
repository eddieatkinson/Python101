# # A function (callled a definition in python) is a piece of code that can be called
# # from somewhere else. They are meant to be reusable and to make
# # things clean.
# # If you have complicated code, you can break it into pieces that are
# # easier to understand.
# # Repeating yourself is BAD.
# # - Copy and paste errors
# # - Odd behaviors
# # - etc...
# # To declare a function in python, you use "def"
# # functions ALWAYS have a ()

# # This defines the function.
# def say_hello():
# 	print "Hello"

# # This calls the function.
# say_hello()

# # Passing variables into functions, are called arguments on the way in,
# # parameters once inside.

# def say_hello_with_name(name):
# 	print "Hello %s" % name

# # say_hello_with_name("Jamie")
# # say_hello_with_name("Sally")
# # say_hello_with_name("You")
# # say_hello_with_name("Eddie")

# students = ['Jamie', 'Sally', 'You', 'Eddie']
# for i in range(0,len(students)):
# 	say_hello_with_name(students[i])

# # say_hello_with_name() # This will FAIL!

# You can set a default for a parameter
def say_hello_safe(name, in_class="Yes"):
	print "%s, %s is in the class." % (in_class, name)

say_hello_safe("Jong")
say_hello_safe("Eddie",23)

# functions ALWAYS return a value
# return value is a function's chance to send ONE and only ONE thing back to
# whoever called it

def return_user_name(name):
	normalized_name = name.upper() # makes all to upper case
	return normalized_name

print return_user_name("Chris")