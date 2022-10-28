#!/bin/env python3

from random import choice, shuffle

def en(code = None):

    def serpirator(inp):
        letters = 'QWERTYUIOPLKJHGFDSZXCVBNMwertyiolhgfdsazxcvbnmjpk:;()|_-&@.,?! =[(#)]'
        out = ''
        for i in inp:
            s = [
                i,
                choice(letters)]
            shuffle(s)
            out += ''.join(s)
        return out

    result = ''
    for i in code:
        result += str(ord(i)) + choice('Aqu')
    return serpirator(result)


def de(code):
    for i in 'QWERTYUIOPLKJHGFDSZXCVBNMwertyiolhgfdsazxcvbnmjpk:;()|_-&@.,?! =[(#)]':
        code = code.replace(i, '')
    return ''.join((lambda .0: [ chr(int(i)) for i in .0 ])((lambda .0: [ k for i in .0 for j in i.split('q') for k in j.split('u') ])(code.split('A'))[:-1]))