import sys
S = list(sys.stdin.readline().rstrip())

tmp = ""
tag = False

def flush(arg):
    global tmp, res, tag
    if tag:
        print(tmp, end = '')
    else:
        print("".join(reversed(tmp)), end = '')
    tmp = ""
    print(arg, end = '')


for i in S:
    if i == '<':
        flush(i)
        tag = True
    elif i == '>':
        flush(i)

        tag = False
    elif i == ' ':
        flush(i)
    else:
        tmp += i

flush("")