def find_prime_numbers_in_range(start, end):
    all_nums = []
    factors_count = 0   # variable to keep count of how many factors a number has
    while start <= end:
        temp = 1    # temp variable to divide by and set to 1 by then end of each iteration
        while temp <= start:
            if start == 0:  # zero division eliminated
                break
            if start % temp == 0:
                factors_count += 1  # adding one each time the reminder of the division is 0
            temp += 1
        if factors_count == 2:  # if the number has only two factors then it is added
            all_nums.append(start)
        start += 1
        factors_count = 0

    return all_nums


x = int(input("Enter a start for the range to test for prime numbers: "))
y = int(input("Enter the end: "))
z = find_prime_numbers_in_range(x, y)
print(z)
