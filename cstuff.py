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