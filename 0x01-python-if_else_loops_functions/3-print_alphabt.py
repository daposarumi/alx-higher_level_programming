#!/usr/bin/python3
for i in range(97, 123):
    if i == 101 or i == 114:
        continue
    else:
        print("{}".format(chr(i)), end='')
