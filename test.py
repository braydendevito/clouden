with open('sep1.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

print ''.join(lhs.split())[:-2]
