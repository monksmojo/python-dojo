input_user_tuple = eval(input("user pls enter you tuple"))
# the elements inside the tuple from the user should be doubled
# (11,22,33) (22,44,66)
print(input_user_tuple)
a, b, c = input_user_tuple
a *= 2
b *= 2
c *= 2
input_user_tuple = (a, b, c)
print(input_user_tuple)

input_user_tuple = eval(input("user pls enter you tuple"))
result_list=[]
for element in input_user_tuple:
    element *= 2
    result_list.append(element)


print(input_user_tuple)
print(tuple(result_list))
