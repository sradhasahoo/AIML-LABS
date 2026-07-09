even_digits = [0, 2, 4, 6, 8]
count = 0

print("Valid 4-digit PINs are:\n")

for d1 in even_digits:
    for d2 in even_digits:
        for d3 in even_digits:
            for d4 in even_digits:
                if d1 + d2 + d3 + d4 == 16:
                    print(f"{d1}{d2}{d3}{d4}")
                    count += 1

print("\nTotal valid PINs:", count)