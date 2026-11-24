inputs = [10, 20, 30, 40, -1]
total, count = 0, 0
for value in inputs:
    if value == -1:
        break
    total += value
    count += 1
    print(f"Average so far: {total / count}")
