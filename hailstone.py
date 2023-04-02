def hailstone(num):
    """
    This function multiplies the input number by three plus one if it is an odd number,
    divides it by two if it is an even number, and ends when it reaches one for the first time.
    """
    steps = 0
    if num == 1:
        steps = 0
    else:
        while num != 1:
            if num % 2 != 0:
                num = num*3+1
            else: num = num/2
            steps += 1
    return steps
print(hailstone(7))