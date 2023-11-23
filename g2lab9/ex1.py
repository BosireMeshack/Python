lambda_fun = lambda a,b : a**2/b

print(lambda_fun(4,2))

def normal_function(a:int, b:int)->float:
    return a**2/b

ls = ['B  ', 'A ', 'M   ', 'K    ', 'Z    ']
print(sorted(ls, key = lambda item: len(item) ))
