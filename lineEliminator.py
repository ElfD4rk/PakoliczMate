outputFile = open('C:/Users/user/PycharmProjects/PakoliczMate/beadando/output.txt', "a")

inputFile = open('C:/Users/user/PycharmProjects/PakoliczMate/beadando/input.txt', "r")

lines_seen_so_far = set()

for line in inputFile:

    if line.rstrip('\n') not in lines_seen_so_far:
        outputFile.write(line)

        lines_seen_so_far.add(line.rstrip('\n'))

inputFile.close()
outputFile.close()
