def fib(num):
    """
    the fib(num) is used to calculate the sum of the previous value of this number and the previous two values
    """
    the_sum1 = 0
    the_sum2 = 0
    the_sum = 0
    times = 1
    the_b = 0
    for i in range(1, num+1):
        if times <= 2:
            the_sum1 = 0
            the_sum2 = 1
        else:
            the_sum2 = the_sum
            the_sum1 = the_b
        the_b = the_sum2
        the_sum = the_sum1 + the_sum2
        times += 1
    print("the_num1 =", the_sum1)
    print("the_num2 =", the_sum2)
    print("the_b =", the_b)
    return the_sum


print(fib(10))
