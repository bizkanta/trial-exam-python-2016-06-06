# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

def doubled(num_list):
    try:
        if type(num_list) is not list:
            raise TypeError
        new_list = []
        for element in num_list:
            new_list += [element * 2]
        return new_list
    except TypeError:
        return 'The parameter is not a list'

print(doubled([1,2,3]))
print(doubled(['a','b','c']))
print(doubled('alma'))
print(doubled(4))
