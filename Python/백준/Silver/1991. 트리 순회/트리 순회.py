from sys import stdin

L = [list(i.split()) for i in stdin.read().splitlines()]

def front_traverse(c):
    if 'A' <= c <= 'Z':
        for i in L:
            if i[0] == c:
                print(c, end = '')
                front_traverse(i[1])
                front_traverse(i[2])
def mid_traverse(c):
    if 'A' <= c <= 'Z':
        for i in L:
            if i[0] == c:
                mid_traverse(i[1])
                print(c, end = '')
                mid_traverse(i[2])
def back_traverse(c):
    if 'A' <= c <= 'Z':
        for i in L:
            if i[0] == c:
                back_traverse(i[1])
                back_traverse(i[2])
                print(c, end = '')

front_traverse('A')
print()
mid_traverse('A')
print()
back_traverse('A')