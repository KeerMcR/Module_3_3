def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(3, 4, 5)
print_params('Hello', 'world', '!')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [43, 'Hello World!', 33.3]
value_dict = {'a': 666, 'b': 'Python', 'c': False}

print_params(*value_list)
print_params(**value_dict)

values_list_2 = ['Urban', 777]
print_params(*values_list_2, 42)
