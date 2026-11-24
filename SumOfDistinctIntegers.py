target = 18
for i in range(1, 8):
    for j in range(i + 1, 9):
        k = target - i - j
        if k > j and k <= 9:
            print(f"{i} + {j} + {k} = {target}")
