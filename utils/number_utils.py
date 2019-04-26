def fibonacci_sequence(n):
    fibonacci_array = [1]
    if n <= 0:
        raise ValueError("illegal argument '{0}', should be > 0".format(n))
    elif n > 1:
        fibonacci_array.append(1)
    for i in range(1, n - 1):
        fibonacci_array.append(fibonacci_array[i - 1] + fibonacci_array[i])
    return fibonacci_array
