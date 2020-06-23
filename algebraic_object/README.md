Help on package algebraic_object:

NAME
    algebraic_object

PACKAGE CONTENTS
    algebraic_object
    test

FILE
    (built-in)


Help on module algebraic_object:

NAME
    algebraic_object

CLASSES
    builtins.dict(builtins.object)
        DictProxy(collections.abc.MutableMapping, builtins.dict)
    builtins.object
        Polynomial
    collections.abc.MutableMapping(collections.abc.Mapping)
        DictProxy(collections.abc.MutableMapping, builtins.dict)
    
    class DictProxy(collections.abc.MutableMapping, builtins.dict)
     |  Copy of the ``dict`` with the ``__setitem__`` method modified
     |  
     |  Method resolution order:
     |      DictProxy
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.dict
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __contains__(self, x)
     |      True if the dictionary has the specified key, else False.
     |  
     |  __delitem__(self, key)
     |      Delete self[key].
     |  
     |  __getitem__(self, key)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __iter__(self)
     |      Implement iter(self).
     |  
     |  __len__(self)
     |      Return len(self).
     |  
     |  __setitem__(self, key, value)
     |      Set items key:value with check
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset()
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |  
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |  
     |  pop(self, key, default=<object object at 0x7ff34d1ac090>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |  
     |  popitem(self)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair
     |      as a 2-tuple; but raise KeyError if D is empty.
     |  
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |  
     |  update(*args, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  get(self, key, default=None)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |  
     |  items(self)
     |      D.items() -> a set-like object providing a view on D's items
     |  
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |  
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |  
     |  __hash__ = None
     |  
     |  __reversed__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |  
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |      
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.dict:
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __sizeof__(...)
     |      D.__sizeof__() -> size of D in memory, in bytes
     |  
     |  copy(...)
     |      D.copy() -> a shallow copy of D
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from builtins.dict:
     |  
     |  fromkeys(iterable, value=None, /) from abc.ABCMeta
     |      Create a new dictionary with keys from iterable and values set to value.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.dict:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class Polynomial(builtins.object)
     |  Polynomial(*args, **kwargs)
     |  
     |  Create a polynomial object.
     |  
     |  Polynomial provides numerical methods '+', '-', '*' and ()
     |  
     |  .. versionadded:: 1.0
     |  
     |  Instance
     |  --------
     |  It is possible to initialize in these three ways:
     |  
     |  Polymian(*args) --> new polynomial initialized from args,
     |      values must be real numbers. Example: p = Polynomial(1, 2, 3)
     |  
     |  Polymian(**kwargs) --> new polynomial initialized with the xn=value pairs
     |      in the keyword argument list, x is the symbol and n is the degree and
     |      values must be real numbers. Example: p = Polynomial(x7 = 1, x3 = 2)
     |  
     |  Polymian(*args, **kwargs) --> new polynomial initialized following the
     |      above rules. Example: p = Polynomial(1, 2, 3, x9 = 4)
     |  
     |  Parameters
     |  ----------
     |  
     |  coef : *args or/and **kwargs
     |      Series coefficients in order of increasing degree, the
     |      coefficients for the missing degrees are considering zero, i.e.:
     |  
     |      ``(1, 2, 3)`` gives ``1*x^1 + 2*x^2 + 3*x^3``
     |      ``(x7 = 1, x3 = 2)`` gives ``2*x^3 + 1*x^7``
     |      ``(1, 2, 3, x9 = 4)`` gives ``1*x^1 + 2*x^2 + 3*x^3 + 4*x^9``
     |  
     |  Attributes
     |  ----------
     |  coef : dict
     |      Dictionary with keys ``xi`` for degree ``i`` and its corresponding
     |      coefficient as value. This attribute can not reassigned, but it can
     |      be updated with `xi=value` pair. Otherwise it will give an error
     |  
     |  degree : int
     |      Degree polynomial (the highest of the degrees of individual terms)
     |      This attribute can not reassigned, but it can be updated when
     |      coefficients are updated.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value)
     |      Numerical method '+'
     |      
     |      Parameters
     |      ----------
     |      other :  anything
     |          Object to be checked, must the same class as `self`
     |      
     |      Returns
     |      -------
     |      Polynomial
     |          `self` + `other`
     |  
     |  __call__(self, value)
     |      Polynomial evaluation
     |      
     |      Parameters
     |      ----------
     |      value :  int/float
     |          Object to be checked, must be 'float'/'int'
     |      
     |      Returns
     |      -------
     |      float
     |          Result P(value)
     |  
     |  __init__(self, *args, **kwargs)
     |      Parameters
     |      ----------
     |      *args : iterable, list
     |          Series coefficients in order of increasing degree
     |      *kwargs : iterable, dict
     |          Series coefficients with degree in keys
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If no parameters are passed or `xi=value` pair is not
     |          the required form. Check Instance section.
     |  
     |  __mul__(self, value)
     |      Numerical method '*'
     |      
     |      Parameters
     |      ----------
     |      other :  anything
     |          Object to be checked, must the same class as `self`
     |          or 'float'/'int'
     |      
     |      Returns
     |      -------
     |      Polynomial
     |          `self` * `other`
     |  
     |  __repr__(self)
     |      Nice print of the polynomial
     |  
     |  __rmul__(self, value)
     |      Numerical method '*'
     |      
     |      Parameters
     |      ----------
     |      other :  anything
     |          Object to be checked, must the same class as `self`
     |          or 'float'/'int'
     |      
     |      Returns
     |      -------
     |      Polynomial
     |          `other` * `self`
     |  
     |  __sub__(self, value)
     |      Numerical method '-'
     |      
     |      Parameters
     |      ----------
     |      other :  anything
     |          Object to be checked, must the same class as `self`
     |      
     |      Returns
     |      -------
     |      Polynomial
     |          `self` - `other`
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  coef
     |  
     |  degree

DATA
    MSG_ERROR_ARG = 'Polynomial() takes least one argument (0 given)'
    MSG_ERROR_KW = "Unexpedted keyword argument: '{}'"
    MSG_ERROR_OPER = "Unsupported operand type(s) for {} and 'Polynomial'"
    MSG_ERROR_VAL = "{} must be 'int' or 'float' not '{}'"
    MSG_WARNING = 'Repeated degree, replaced first assigned value'

FILE
    /home/shersnape/Proyectos/Repositorio/challenges/algebraic_object/algebraic_object.py


Help on module test:

NAME
    test - Test the Class Polynomial from ``algebraic_object.Polynomial``.

FUNCTIONS
    call_test(module)
    
    test_add_other()
    
    test_add_sub_pol()
    
    test_bad_eval()
    
    test_change_coef()
    
    test_change_degree()
    
    test_eval()
    
    test_init_args()
    
    test_init_args_kw()
    
    test_init_bad_key()
    
    test_init_bad_value()
    
    test_init_kw()
    
    test_init_no_value()
    
    test_mul_other()
    
    test_mul_pol()
    
    test_mul_scalar()
    
    test_sub_other()
    
    test_update_coef()

FILE
    /home/shersnape/Proyectos/Repositorio/challenges/algebraic_object/test.py


