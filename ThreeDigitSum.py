for first_value in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            number = first_value * 100 + b * 10 + c
            if first_value * first_value + b * b + c * c == number:
                print(number)
