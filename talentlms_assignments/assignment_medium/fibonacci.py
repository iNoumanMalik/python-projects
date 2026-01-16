def loop_fibonacci(num):
    next = 0
    first = 0
    second = 1
    result = [first,second]
    for n in range(num - 2):
        next = first + second 
        first = second 
        second = next
        result.append(next) 
    
    return result


print(loop_fibonacci(10))


#with recursion
def recursion_fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2: 
        return [0,1]
    
    fibs = recursion_fibonacci(n-1)
    fibs.append(fibs[-1]+fibs[-2])
    return fibs

print(recursion_fibonacci(8))
        

