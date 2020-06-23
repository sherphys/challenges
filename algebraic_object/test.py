"""
Test the Class Polynomial from ``algebraic_object.Polynomial``.

"""

import inspect
import sys
import algebraic_object as ao


def test_init_args():
    p = ao.Polynomial(1, 2, 3)
    assert p.coef == {"x0": 1, "x1": 2, "x2": 3}
    assert p.degree == 2


def test_init_kw():
    p = ao.Polynomial(x9=3, x2=1.0)
    assert p.coef == {"x9": 3, "x2": 1.0}
    assert p.degree == 9


def test_init_args_kw():
    p = ao.Polynomial(1, 2, 3, x10=12)
    assert p.coef == {"x0": 1, "x1": 2, "x2": 3, "x10": 12}
    assert p.degree == 10


def test_init_no_value():
    try:
        p = ao.Polynomial()
    except TypeError as err:
        assert str(err) == ao.MSG_ERROR_ARG


def test_init_bad_key():
    try:
        p = ao.Polynomial(badkey=1)
    except TypeError as err:
        assert str(err) == ao.MSG_ERROR_KW.format("badkey")


def test_init_bad_value():
    try:
        p = ao.Polynomial("2")
    except TypeError as err:
        assert str(err) == ao.MSG_ERROR_VAL.format("Coefficients", "str")


def test_change_degree():
    try:
        p = ao.Polynomial(2)
        p.degree = 5
    except AttributeError as err:
        assert str(err) == "can't set attribute"


def test_change_coef():
    try:
        p = ao.Polynomial(2)
        p.coef = [1, 2, 3]
    except AttributeError as err:
        assert str(err) == "can't set attribute"


def test_update_coef():
    p = ao.Polynomial(2)
    p.coef["x1"] = 4.5
    assert p.degree == 1


def test_add_sub_pol():
    p = ao.Polynomial(1, 2, 3)
    r = ao.Polynomial(3, 4)
    q = p + r
    s = p - r
    assert q.coef == ao.Polynomial(4, 6, 3).coef
    assert s.coef == ao.Polynomial(-2, -2, 3).coef


def test_mul_scalar():
    p = ao.Polynomial(1, 2, 3)
    r = 2 * p
    q = p * 2
    assert r.coef == ao.Polynomial(2, 4, 6).coef
    assert q.coef == ao.Polynomial(2, 4, 6).coef


def test_mul_pol():
    p = ao.Polynomial(1, 2, 3)
    r = ao.Polynomial(3, 4)
    q = p * r
    assert q.coef == ao.Polynomial(3, 10, 17, 12).coef


def test_add_other():
    try:
        p = ao.Polynomial(1, 2, 3)
        r = p + 1
    except TypeError as err:
        assert str(err) == ao.MSG_ERROR_OPER.format(" +: 'int' ")


def test_sub_other():
    try:
        p = ao.Polynomial(1, 2, 3)
        r = p - 1.8
    except TypeError as err:
        assert str(err) == ao.MSG_ERROR_OPER.format(" -: 'float' ")


def test_mul_other():
    try:
        p = ao.Polynomial(1, 2, 3)
        r = [2] * p
    except TypeError as err:
        assert str(err) == ao.MSG_ERROR_OPER.format(" *: 'list' ")


def test_eval():
    p = ao.Polynomial(1, 2, 3)
    assert p(5) == 86


def test_bad_eval():
    try:
        p = ao.Polynomial(1, 2, 3)
        p("5")
    except TypeError as err:
        assert str(err) == ao.MSG_ERROR_VAL.format("Value", "str")


def call_test(module):
    all_functions = inspect.getmembers(module, inspect.isfunction)
    for key, value in all_functions:
        if str(inspect.signature(value)) == "()":
            print(key, " ... ", end="")
            value()
            print("Ok!")


if __name__ == "__main__":
    call_test(sys.modules[__name__])
    print("Everything passed")
