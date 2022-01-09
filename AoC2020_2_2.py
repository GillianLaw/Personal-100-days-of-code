
def passwordcheck(passrule):
    total = 0
    """First, split the line into useful pieces. I could probably do this on
        one line, but it follows the way my brain thinks (slowly!), and it works.."""
    for line in passrule:
        i = line.split(':')
        j = i[0].split(' ')
        k = j + i

        count = 0
        g = k[0].split()
        if g[0][1] == '-':
            h = int(g[0][0])
        else:
            h = int(g[0][0:2])
        if g[0][-2:-1] == '-':
            hh = int(g[0][-1:])
        else:
            hh = int(g[0][-2:])

            """Does letter appear in those precise spots?"""
        if k[1] == k[3][h] or k[1] == k[3][hh]:
            count += 1
        if k[1] == k[3][h] and k[1] == k[3][hh]:
            count -= 1

        if count == 1:
            total += 1
            print('Total Part 2:', total)


with open('data.txt') as f:
    change = [line.rstrip() for line in f]

passwordcheck(change)
