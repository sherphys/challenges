import warnings
from collections.abc import MutableMapping

MSG_ERROR_OPER = "Unsupported operand type(s) for {} and 'Polynomial'"
MSG_ERROR_ARG = "Polynomial() takes least one argument (0 given)"
MSG_ERROR_VAL = "{} must be 'int' or 'float' not '{}'"
MSG_ERROR_KW = "Unexpedted keyword argument: '{}'"
MSG_WARNING = "Repeated degree, replaced first assigned value"


class DictProxy(MutableMapping, dict):
    """Copy of the ``dict`` with the ``__setitem__`` method modified

    """

    def __getitem__(self, key):
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        """Set items key:value with check

        """
        self._check_keys(key)
        self._check_values(value)
        dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        dict.__delitem__(self, key)

    def __iter__(self):
        return dict.__iter__(self)

    def __len__(self):
        return dict.__len__(self)

    def __contains__(self, x):
        return dict.__contains__(self, x)

    def _check_keys(self, key):
        """Check the key have the form "x0", "x1", ..., "xn" when n is a
            positive integer. Raise an error otherwise.

        """
        if key[0] == "x" and key[1:].isdecimal():
            return key
        else:
            raise TypeError(MSG_ERROR_KW.format(key))

    def _check_values(self, value):
        """Check that the value is 'int' or 'float'. Raise an error otherwise.

        """
        if not isinstance(value, int) and not isinstance(value, float):
            s = value.__class__.__name__
            raise TypeError(MSG_ERROR_VAL.format("Coefficients", s))


class Polynomial():
    """Create a polynomial object.

    Polynomial provides numerical methods '+', '-', '*' and ()

    .. versionadded:: 1.0

    Instance
    --------
    It is possible to initialize in these three ways:

    Polymian(*args) --> new polynomial initialized from args,
        values must be real numbers. Example: p = Polynomial(1, 2, 3)

    Polymian(**kwargs) --> new polynomial initialized with the xn=value pairs
        in the keyword argument list, x is the symbol and n is the degree and
        values must be real numbers. Example: p = Polynomial(x7 = 1, x3 = 2)

    Polymian(*args, **kwargs) --> new polynomial initialized following the
        above rules. Example: p = Polynomial(1, 2, 3, x9 = 4)

    Parameters
    ----------

    coef : *args or/and **kwargs
        Series coefficients in order of increasing degree, the
        coefficients for the missing degrees are considering zero, i.e.:

        ``(1, 2, 3)`` gives ``1*x^1 + 2*x^2 + 3*x^3``
        ``(x7 = 1, x3 = 2)`` gives ``2*x^3 + 1*x^7``
        ``(1, 2, 3, x9 = 4)`` gives ``1*x^1 + 2*x^2 + 3*x^3 + 4*x^9``

    Attributes
    ----------
    coef : dict
        Dictionary with keys ``xi`` for degree ``i`` and its corresponding
        coefficient as value. This attribute can not reassigned, but it can
        be updated with `xi=value` pair. Otherwise it will give an error

    degree : int
        Degree polynomial (the highest of the degrees of individual terms)
        This attribute can not reassigned, but it can be updated when
        coefficients are updated.

    """
    _superscript_map = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
                        "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"}

    def __init__(self, *args, **kwargs):
        """
        Parameters
        ----------
        *args : iterable, list
            Series coefficients in order of increasing degree
        *kwargs : iterable, dict
            Series coefficients with degree in keys

        Raises
        ------
        TypeError
            If no parameters are passed or `xi=value` pair is not
            the required form. Check Instance section.

        """
        there_coef_in_args = len(args) != 0
        there_coef_in_kwargs = len(kwargs) != 0
        if not there_coef_in_args and not there_coef_in_kwargs:
            raise TypeError(MSG_ERROR_ARG)

        self._coef = DictProxy()

        if there_coef_in_args:
            self._coef.update({"x%d" % i: v for i, v in enumerate(args)})

        if there_coef_in_kwargs:
            self._parse_kwargs(kwargs)

    @property
    def degree(self):
        return self._get_max_degree()

    @property
    def coef(self):
        return self._coef

    def _parse_kwargs(self, kwargs):
        """Update coef attribute with kwargs.

        If coef already has a value assigned to a grade, it is
        replaced and a warning is displayed.

        """
        for k, v in kwargs.items():
            if self._coef.get(k, None) is not None:
                warnings.warn(MSG_WARNING, Warning, stacklevel=1)
            self._coef[k] = v

    def _get_max_degree(self):
        _max_degree_expr = max(self.coef.keys(), key=self._get_degree)
        return self._get_degree(_max_degree_expr)

    def _get_degree(self, expr):
        """Get degree of expr 'str' as 'int'.

        """
        return int(expr[1:])

    def _all_degrees(self):
        return [self._get_degree(k) for k in self.coef.keys()]

    def _result_degrees(self, other):
        """Information of the coefficients and degrees for polynomial add/sub

        Add/Sub between polynomials can be done by add/sub like terms.
        If P(x) = `3x^9 + 5x^1 + 2x^0` degrees P_d = (9,1,0), in the same way
        R(x) = `x^1 + x^0` R_d =(1,0). The resultant degrees is P_d U R_d or
        (9,1,0)

        Parameters
        ----------
        other : Polynomial
            Object of the same class as `self` for add/sub

        Returns
        -------
        coef1 : dict
            The coefficients of `self`
        coef2 : dict
            The coefficients of `other`
        result_keys: dict
            Degrees of the resulting polynomial according to the degrees of
            `self` and `other`

        """

        coef1, degree1 = self.coef, self._all_degrees()
        coef2, degree2 = other.coef, other._all_degrees()
        result_degrees = [d for d in degree1 if d not in degree2] + degree2
        result_keys = ["x%d" % i for i in result_degrees]
        return coef1, coef2, result_keys

    def _result_degrees_mul(self, other):
        """Information of the coefficients and degrees for polynomial mul

        Mul between polynomials can be done by mul each terms and
        sum like terms.

        If P(x) = `3x^9 + 5x^1 + 2x^0` degrees P_d = (9,1,0), in the same way
        R(x) = `x^1 + x^0` R_d =(1,0) so resultant oper is (P_d_i, R_d_j) for
        i,j in P_d, R_d ((9,1),(9,0),(1,1),(1,0),(0,1),(0,0))

        Ther resultant degrees  sum(resultant oper) unique values, so
        (10,9,2,1,0)

        Parameters
        ----------
        other : Polynomial
            Object of the same class as `self` for  mul

        Returns
        -------
        coef1 : dict
            The coefficients of `self`
        coef2 : dict
            The coefficients of `other`
        result_keys: dict
            Degrees of the resulting polynomial according to the degrees of
            `self` and `other`

        result_oper: list
            Combination of degrees in mul according to the degrees of
            `self` and `other`

        """

        coef1, degree1 = self.coef, self._all_degrees()
        coef2, degree2 = other.coef, other._all_degrees()
        result_degrees = []
        result_oper = []
        for d in degree1:
            result_degrees += [d + d_ for d_ in degree2
                               if d + d_ not in result_degrees]
            result_oper.extend([(d, d_) for d_ in degree2])
        result_keys = ["x%d" % i for i in result_degrees]
        return coef1, coef2, result_keys, result_oper

    def _mul_pol(self, value):
        """Polynomial Multiplication

        Multiplication between polynomials can be summarized, where P_i and R_i
        are the coefficients of P(x), R(x):

        `x^0` = `P_0*R_0`
        `x^1` = `P_1*R_0 + P_0*R_1`
        `x^2` = `P_2*R_1 + P_1*R_1 P_0*R_2`
        ....
        `x^n` = `P_n*R_1 + P_(n-1)*R_1 + ...+ P_0*R_n`

        With result_keys we select the `x^n` those are actually calculated,
        and with result_oper the coefficients other than 0 for optimization.

        Parameters
        ----------
        other : Polynomial
            Object of the same class as `self` for mul

        Returns
        -------
        Polynomial
            Degrees of the resulting polynomial according to the degrees of
            `self` and `other`

        result_oper: list
            Combination of degrees in mul according to the degrees of
            `self` and `other`

        """
        coef1, coef2, result_keys, comb = self._result_degrees_mul(value)
        result_coef = {}
        for k in result_keys:
            deg = self._get_degree(k)
            comb_deg = [c for c in comb if sum(c) == deg]
            result_coef[k] = 0
            for i, j in comb_deg:
                getc1 = coef1.get("x%d" % i, 0)
                getc2 = coef2.get("x%d" % j, 0)
                result_coef[k] += getc1*getc2

        result_coef = {k: v for k, v in result_coef.items()
                       if v != 0}

        return Polynomial(**result_coef)

    def _mul_scalar(self, value):
        """Polynomial scalar multiplication

        """
        coef1, degree1 = self.coef, self._all_degrees()
        result_keys = ["x%d" % i for i in degree1]
        result_coef = {k: value * coef1.get(k, 0) for k in result_keys}
        result_coef = {k: v for k, v in result_coef.items()
                       if v != 0}

        return Polynomial(**result_coef)

    def __repr__(self):
        """Nice print of the polynomial

        """
        nice_str = ""
        keys = list(self.coef.keys())
        keys.sort(key=self._get_degree)
        keys = keys[::-1]

        for k in keys:
            v = self.coef[k]
            deg = str(self._get_degree(k))
            nice_deg = "".join([self._superscript_map[s] for s in deg])
            nice_deg = k[0] + nice_deg
            nice_val = "%.2f%s" % (abs(v), nice_deg)
            if k == "x"+str(self.degree):
                nice_str += nice_val
            else:
                nice_str += " + " + nice_val if v > 0 else " - " + nice_val

        return nice_str[:-2]

    def __call__(self, value):
        """Polynomial evaluation

        Parameters
        ----------
        value :  int/float
            Object to be checked, must be 'float'/'int'

        Returns
        -------
        float
            Result P(value)

        """
        if not isinstance(value, int) and not isinstance(value, float):
            s = value.__class__.__name__
            raise TypeError(MSG_ERROR_VAL.format("Value", s))

        result = 0
        for k, v in self.coef.items():
            degree = self._get_degree(k)
            result += v * value ** degree
        return result

    def __add__(self, value):
        """Numerical method '+'

        Parameters
        ----------
        other :  anything
            Object to be checked, must the same class as `self`

        Returns
        -------
        Polynomial
            `self` + `other`

        """
        if not isinstance(value, self.__class__):
            s = value.__class__.__name__
            raise TypeError(MSG_ERROR_OPER.format(" +: '%s' " % s))

        coef1, coef2, result_keys = self._result_degrees(value)
        result_coef = {k: coef1.get(k, 0) + coef2.get(k, 0)
                       for k in result_keys}
        result_coef = {k: v for k, v in result_coef.items()
                       if v != 0}

        return Polynomial(**result_coef)

    def __sub__(self, value):
        """Numerical method '-'

        Parameters
        ----------
        other :  anything
            Object to be checked, must the same class as `self`

        Returns
        -------
        Polynomial
            `self` - `other`

        """

        if not isinstance(value, self.__class__):
            s = value.__class__.__name__
            raise TypeError(MSG_ERROR_OPER.format(" -: '%s' " % s))

        coef1, coef2, result_keys = self._result_degrees(value)
        result_coef = {k: coef1.get(k, 0) - coef2.get(k, 0)
                       for k in result_keys}
        result_coef = {k: v for k, v in result_coef.items()
                       if v != 0}

        return Polynomial(**result_coef)

    def __mul__(self, value):
        """Numerical method '*'

        Parameters
        ----------
        other :  anything
            Object to be checked, must the same class as `self`
            or 'float'/'int'

        Returns
        -------
        Polynomial
            `self` * `other`

        """
        if isinstance(value, int) or isinstance(value, float):
            return self._mul_scalar(value)
        elif isinstance(value, self.__class__):
            return self._mul_pol(value)
        else:
            s = value.__class__.__name__
            raise TypeError(MSG_ERROR_OPER.format(" *: '%s' " % s))

    def __rmul__(self, value):
        """Numerical method '*'

        Parameters
        ----------
        other :  anything
            Object to be checked, must the same class as `self`
            or 'float'/'int'

        Returns
        -------
        Polynomial
            `other` * `self`

        """
        if isinstance(value, int) or isinstance(value, float):
            return self._mul_scalar(value)
        else:
            s = value.__class__.__name__
            raise TypeError(MSG_ERROR_OPER.format(" *: '%s' " % s))
