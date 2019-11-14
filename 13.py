def line_ints():
    with open("13.txt", "r") as f:
        for line in f:
            yield int(line)

result = sum(line_ints())
print(str(result)[:10])
