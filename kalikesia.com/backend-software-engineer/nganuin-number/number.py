buf = 1
for i in range(1,100):
    buf = i * buf

print ">" + str(buf) # + 0

bufstr = str(buf)
buflen = len(bufstr)
result = 0

for i in range(0, int(buflen)):
    if i == 0:
        result = i
    else:
        split = int(bufstr[i])
        assign = result + split
        result = assign

print result
