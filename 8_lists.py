friends = ['Kevin', 'John', 'Tom']
random = ['Kevin', 1, True]
print(friends)
print(random)

# Using Index Position
print('Using Index Position')
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])

# Getting some part of list
print('Getting some part of list')
my_list = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
print(my_list[1:])
# ['john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
print(my_list[5:])
# ['harry', 'ben', 'jimmy']
print(my_list[:5])
# ['kevin', 'john', 'tom', 'tim', 'bob']
print(my_list[1:5])
# ['john', 'tom', 'tim', 'bob']
print(my_list[4:5])
# ['bob']
print(my_list[::2])
# ['kevin', 'tom', 'bob', 'ben']
print(my_list[:4:2])
# ['kevin', 'tom']
print(my_list[3::2])
# ['tim', 'harry', 'jimmy']
print(my_list[::3])
# ['kevin', 'tim', 'ben']

# OUTPUT
# ['Kevin', 'John', 'Tom']
# ['Kevin', 1, True]      
# Using Index Position    
# Kevin
# Tom  
# Tom  
# John
# Getting some part of list
# ['john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
# ['harry', 'ben', 'jimmy']
# ['kevin', 'john', 'tom', 'tim', 'bob']
# ['john', 'tom', 'tim', 'bob']
# ['bob']
# ['kevin', 'tom', 'bob', 'ben']
# ['kevin', 'tom']
# ['tim', 'harry', 'jimmy']
# ['kevin', 'tim', 'ben']