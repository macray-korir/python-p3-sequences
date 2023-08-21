#!/usr/bin/env python3

def test_print_fibonacci_zero(self):
    '''prints empty list when length = 0'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(0)
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue().strip() == '[]'
