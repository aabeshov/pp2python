code = 'print("hello world")'
code1 = '''
x = int(input())
y = 2 * x
print(x)
print(y)
'''
exec(code)
exec(code1)