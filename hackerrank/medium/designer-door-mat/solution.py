n, m = map(int, input().split())

# Upper part
for i in range(1, n, 2):
    pattern = '.|.' * i
    print(pattern.center(m, '-'))

# Center
print('WELCOME'.center(m, '-'))

# Lower part
for i in range(n - 2, 0, -2):
    pattern = '.|.' * i
    print(pattern.center(m, '-'))
