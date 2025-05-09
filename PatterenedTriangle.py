
for row in range(1, 11):
    for star in range(1, row + 1):
        print('*', end='')
    print()

print()  

# Pattern (b)
for row in range(10, 0, -1):
    for star in range(1, row + 1):
        print('*', end='')
    print()

print()

# Pattern (c)
for row in range(10, 0, -1):
    for space in range(10 - row):
        print(' ', end='')
    for star in range(row):
        print('*', end='')
    print()

print()

# Pattern (d)
for row in range(1, 11):
    for space in range(10 - row):
        print(' ', end='')
    for star in range(row):
        print('*', end='')
    print()
