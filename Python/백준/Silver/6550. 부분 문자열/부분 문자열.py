while 1:
    try:
        line = input()
    except EOFError:
        break

    s, t = map(str, line.split())
    pos = 0
    for i in t:
        if s[pos] == i:
            pos += 1
            if pos >= len(s):
                print("Yes")
                break
    if pos < len(s):
        print("No")