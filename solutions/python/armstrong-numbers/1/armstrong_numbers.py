def is_armstrong_number(number):
    power = count_digits(number)

    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == number

def count_digits(number):
    if number == 0:
        return 1

    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
        
