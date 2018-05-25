import sys

birthdays = {}

def test():
    for line in sys.stdin:
        line = line.strip()
        # print(line)
        tokens = line.split()
        # print(tokens)
        m = int(tokens[1])
        if birthdays.get(m):
            birthdays[m] += 1
        else:
            birthdays[m] = 1

    for i in range(1,13):
        print(i, birthdays.get(i))
test()