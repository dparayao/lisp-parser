"""Lisp parser for the Recurse Center pairing interview.

Run:   python3 lisp.py "(first (list 1 (+ 2 3) 9))"
Tests: python3 -m unittest -v
"""

import sys


class ParseError(Exception):
    """Raised for malformed input: empty source, unbalanced parens, trailing tokens."""


def tokenize(source):
    """Split source into tokens: '(', ')', and atoms.

    "(+ 1 2)" -> ["(", "+", "1", "2", ")"]
    """
    result = []

    index = 0
    length = len(source)
    while (index < length):
        if source[index] == "(":
            result.append(source[index])
            index += 1
            continue

        cur_token = ""
        while (index < length and source[index] != " "):
            if (source[index] == ")"):
                result.append(cur_token)
                cur_token = []
                index += 1
            else:
                cur_token += source[index]
                index += 1
        result.append(cur_token)

        index += 1

    return result


def parse_atom(token):
    """Turn one atom token into an int, a float, or a symbol (str).

    "42" -> 42, "3.14" -> 3.14, "foo" -> "foo"
    """
    if "." in token:
        return float(token)
    elif token.isdigit():
        return int(token)
    else:
        return token


def parse(source):
    """Parse one Lisp expression into a nested-list AST.

    "(first (list 1 (+ 2 3) 9))" -> ["first", ["list", 1, ["+", 2, 3], 9]]
    """

    # convert to tokens
    tokens = tokenize(source)

    # push tokens onto stack, if you see closing bracket form list
    result = []
    cur_list = []
    processed = []

    for token in tokens:
        if token != ')':
            processed.append(parse_atom(token))
        else:
            while (processed[-1] != '('):
                cur_list.append(processed.pop())

            processed.pop()

            cur_list.reverse()
            print(cur_list)
            processed.append(cur_list)
            cur_list = [] # reset to blank

    result = processed.pop()

    return result


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "(first (list 1 (+ 2 3) 9))"
    print(parse(src))