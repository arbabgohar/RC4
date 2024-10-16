#Initilizaing 
s = []
def scramble(key):
    schedule = []
    j = 0
    for i in range(256):
        s.append(i)
    #Scheduling 
    keyBytes = key.encode('utf-8')
    while len(schedule) <= 256:
        for char in keyBytes:
            schedule.append(char)
    #Scramble 
    for i in range(256):
        j = (j + s[i] + schedule[i]) % 256
        s[i], s[j] = s[j], s[i]
def randomByte():
    global p, q
    p = (p + 1) % 256
    print(p)
    q = (q + s[p]) % 256
    print(q)
    s[p], s[q] = s[q], s[p]
    pointer = (s[p] + s[q]) % 256
    return s[pointer]

def encrpytString(data):
    dataBytes = data.encode('utf-8')
    output = []
    for char in dataBytes:
        output.append(char ^ randomByte())
    return output

def encrpyt(key, string):
    global p, q
    p = q = 0
    scramble(key)
    for i in range(256):
        randomByte()
    return encrpytString(string)
key = "cis350"
string = "Assignment 2"
print(encrpyt(key, string))
