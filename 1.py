def sum_multiples(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

print(sum_multiples(10))
print(sum_multiples(1000))
