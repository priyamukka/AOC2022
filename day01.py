file1 = open('elflist', "r")
lines = file1.readlines()
count = 0


if __name__ == '__main__':
    total = 0
    elveCount = 1
    elvesCal = []
    for line in lines:
        if line in ['\n', '\r', '\r\n']:
            print('The line is empty')
            elvesCal.append(total)
            total = 0
            elveCount += 1
            continue
        total += int(line)
print("Total Elves", elveCount)
print("Which Elf got Max:", max(elvesCal))
print("Top Total Calories", sum(sorted(elvesCal)[-3:]))
