# Count the minimum total number of indices of a symmetric tensor that must be defined
# This will use a function I call Red(), where 'Red' is short for 'Reduce'
# Red^n(N) = Sum( Red^(n-1)(N-i) )
# Red^2(N) = Red(N) = Sum( N-i )
# A rank 2, N dimensional symmetric tensor (NxN matrix) has a minimum of Red(2, N) independant indices
# A rank 3, N dimensional symmetric tensor (NxNxN 'matrix') has a minimum of Red(3, N)

#__init__.py

def Red(n, N): # Only except integers
    if isinstance(n, int) != True or isinstance(N, int) != True:
        print("\nFunction not defined for non-integers\n")
        return None
    sum = 0
    if n == 0:
        return 0
    elif n == 1:
        return N
    elif n == 2:
        for i in range(N):
            sum += N - i
    else:
        for i in range(N):
            sum += Red(n-1, N-i)
    return sum

# print(Red(2,4))
