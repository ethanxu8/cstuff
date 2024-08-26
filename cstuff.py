print('hello world')

def multiply_numbers(n):
    return n*n

print(multiply_numbers(4))

# O(1) time complexity because the only function is n*n regardless of what number n is. 



def range_values(n): 
    for i in range(n):
        print(i)
        
print(range_values(10))

# O(n) time complexity because the number of functions increases linearly with the number n. 

def range_values(n): 
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
        
range_values(10)

# This is technically O(2n) time complexity because it is n + n. However, when n gets really large, 2 becomes negligible. Therefore when we have a constant like 2 we can just drop it. So O(2n) = O(n)

def range_values(n): 
    for i in range(n):
        for j in range(n):
            print(i, j)
        
range_values(10)

# This is what we call a nested loop and it has a time complexity of O(n^2). For the outer loop which is "for i in range(n)" to move on from 0 to 1, the inner loop "for j in range(n)" must be satisfied. Think about it like layers. For the outer loop to
# on, the inner loop must first be satisfied. This explains why the outer loop stays at one number 9 times to allow the inner loop to iterate fully before moving on to the next. 