
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

            """Check whether the letter is in the password, and how often"""
        for letter in k[3]:
            if letter == k[1]:
                count +=1
                """Does it appear within the range of times allowed?"""
        if count in range(h,hh+1):
            total += 1
        print("Total:", total)

with open('data.txt') as f:
    change = [line.rstrip() for line in f]

passwordcheck(change)

# if __name__ == "__main__":
