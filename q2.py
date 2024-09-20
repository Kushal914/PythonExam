# Lists, sets, and dictinaries are collections of variables under a common name.

# List can be created by providing comma-separated values inside braces.

my_list = ['apple', 'orange', 'banana', 'mango', 'apple']
print(my_list) # preserves order
print(my_list[0]) # apple

# Set can only have unique members. And set is not subscriptable. It consists of comma-separated values within brackets.

my_set = {'apple', 'orange', 'banana', 'mango', 'apple'} # only considers one instance of 'apple'
print(my_set) # prints out of order
# print(my_set[0]) gives error

# Dictionary is a collection of key-value pairs. Like set, it's values are also comma-separated bound by brackets.

my_dict = {
    'name' : 'Kushal',
    'age' : 24,
    'gender' : 'male'
}

print(my_dict['name']) # Kushal