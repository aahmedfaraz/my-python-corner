luckcy_numbers = [11, 23, 44, 54, 6, 7, 88, 93]
friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends.extend(luckcy_numbers)
print(friends)
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy', 11, 23, 44, 54, 6, 7, 88, 93]

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends.append('Ahmed')
print(friends)
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy', 'Ahmed']

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends.insert(1, 'Ahmed')
print(friends)
# ['kevin', 'Ahmed', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends.remove('tom')
print(friends)
# ['kevin', 'john', 'tim', 'bob', 'harry', 'ben', 'jimmy']

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends.clear()
print(friends)
# []

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
print(friends.pop())
print(friends)
# jimmy
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben']

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
print(friends.index('tom'))
# 2

friends = ['kevin', 'john', 'tom', 'tom', 'tom',
           'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
print(friends.count('tom'))
# 4

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends.sort()
print(friends)
luckcy_numbers.sort()
print(luckcy_numbers)
# ['ben', 'bob', 'harry', 'jimmy', 'john', 'kevin', 'tim', 'tom']
# [6, 7, 11, 23, 44, 54, 88, 93]

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends.reverse()
print(friends)
luckcy_numbers.reverse()
print(luckcy_numbers)
print(friends)
# [93, 88, 54, 44, 23, 11, 7, 6]
# ['jimmy', 'ben', 'harry', 'bob', 'tim', 'tom', 'john', 'kevin']

friends = ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
friends2 = friends.copy()
print(friends2)
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']

# OUTPUT
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy', 11, 23, 44, 54, 6, 7, 88, 93]
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy', 'Ahmed']
# ['kevin', 'Ahmed', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
# ['kevin', 'john', 'tim', 'bob', 'harry', 'ben', 'jimmy']
# []
# jimmy
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben']
# 2
# 4
# ['ben', 'bob', 'harry', 'jimmy', 'john', 'kevin', 'tim', 'tom']
# [6, 7, 11, 23, 44, 54, 88, 93]
# ['jimmy', 'ben', 'harry', 'bob', 'tim', 'tom', 'john', 'kevin']
# [93, 88, 54, 44, 23, 11, 7, 6]
# ['jimmy', 'ben', 'harry', 'bob', 'tim', 'tom', 'john', 'kevin']
# ['kevin', 'john', 'tom', 'tim', 'bob', 'harry', 'ben', 'jimmy']
