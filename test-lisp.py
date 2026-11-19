import unittest
 
from lisp import parse
 
 
class TestParse(unittest.TestCase):
    """Valid inputs and the AST each one should produce."""
 
    CASES = [
        # atoms
        ("42", 42),
        ("-7", -7),
        ("3.14", 3.14),
        ("x", "x"),
        ("+", "+"),
        ("-", "-"),  # "-" alone is a symbol, not a number
        # flat lists
        ("()", []),
        ("(  )", []),
        ("(+ 1 2)", ["+", 1, 2]),
        ("(list 1 2.5 x)", ["list", 1, 2.5, "x"]),
        # nesting
        ("((a))", [["a"]]),
        ("(() (()))", [[], [[]]]),
        ("(((1)))", [[[1]]]),
        ("(first (list 1 (+ 2 3) 9))", ["first", ["list", 1, ["+", 2, 3], 9]]),
        ("(define (square x) (* x x))", ["define", ["square", "x"], ["*", "x", "x"]]),
        # whitespace
        ("  42  ", 42),
        ("  ( +\n 1\t2 )  ", ["+", 1, 2]),
        ("(\n  list\n  1\n  2\n)", ["list", 1, 2]),
    ]
 
    def test_valid_inputs(self):
        for source, expected in self.CASES:
            with self.subTest(source=source):
                self.assertEqual(parse(source), expected)
 
    def test_ints_stay_ints(self):
        # assertEqual treats 42 == 42.0, so check the type separately
        self.assertIsInstance(parse("42"), int)
        self.assertIsInstance(parse("3.14"), float)
 
 
if __name__ == "__main__":
    unittest.main()