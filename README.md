# Lisp Parser

A small parser that turns a Lisp expression into a nested Python list.

```
(first (list 1 (+ 2 3) 9))  ->  ['first', ['list', 1, ['+', 2, 3], 9]]
```

Integers become `int`, decimals become `float`, and everything else becomes a symbol (`str`).

## Requirements

Python 3

## Run

Pass an expression as an argument:

```sh
python3 lisp.py "(define (square x) (* x x))"
# ['define', ['square', 'x'], ['*', 'x', 'x']]
```

With no argument, it parses the example `(first (list 1 (+ 2 3) 9))`.

Malformed input raises `ParseError`:

- Empty input
- Unbalanced parentheses, e.g. `(+ 1 2` or `(+ 1 2))`
- Extra tokens after a complete expression, e.g. `(a) (b)`

## Test

From the project directory:

```sh
python3 -m unittest -v
```

The tests are in `test_lisp.py`:

- `TestParse` checks valid inputs (atoms, flat lists, nested lists, whitespace) and the result expected for each.
- `TestParseErrors` checks that malformed inputs raise `ParseError`.
