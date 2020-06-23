Help on module chessmoves:

NAME
    chessmoves

CLASSES
    builtins.object
        ChessBoard
        ChessPiece
            Bishop
            King
            Knight
            Pawn
            Queen
            Rook
        MoveRules
    builtins.tuple(builtins.object)
        Point
        Points
    
    class Bishop(ChessPiece)
     |  Create a chess piece Bishop
     |  
     |  The Bishop class is a subclass of `Chess Piece`, the attributes
     |  and methods are listed in the `Chess Piece` documentation
     |  
     |  .. versionadded:: 1.0
     |  
     |  Method resolution order:
     |      Bishop
     |      ChessPiece
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  possible_moves(self, position, board=None)
     |      Check a square of the board where the Bishop can make a move
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      board: ChessBoard, optional
     |          The chessboard where the chess piece moves
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If position is not in algebraic notation or is off the board
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from ChessPiece:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  set_color_black(self)
     |  
     |  set_color_white(self)
     |  
     |  set_legal_moves(self, position, moves, rules=None)
     |      Check that the assigned movements comply with the
     |      chess piece's movement rules
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ChessPiece:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  name
    
    class ChessBoard(builtins.object)
     |  Create chessboard.
     |  
     |  .. versionadded:: 1.0
     |  
     |  Algebraic notation (chess)
     |    _______________
     |  8|_|_|_|_|_|_|_|_|
     |  7|_|_|_|_|_|_|_|_|
     |  6|_|_|_|_|_|_|_|_|
     |  5|_|_|_|_|_|_|_|_|
     |  4|_|_|_|_|_|_|_|_|
     |  3|_|_|_|_|_|_|_|_|
     |  2|_|_|_|_|_|_|_|_|
     |  1|_|_|_|_|_|_|_|_|
     |    A B C D E F G H
     |  
     |  Attributes
     |  ----------
     |  state : list of list
     |      8x8 chess board represented in a list of lists.
     |      Empty square of the board have a value of 0.
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  in_place(self, position)
     |      Place a chess piece in one position
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If position is not in algebraic notation or is off the board
     |  
     |  is_free_position(self, position)
     |      Check a square of the board in position is free
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      Return
     |      ------
     |      Bool
     |          Is empty o not
     |  
     |  is_free_xyposition(self, xyposition)
     |      Check a square of the board in xyposition is free
     |      
     |      Parameters
     |      ----------
     |      xyposition : Point
     |          Position in (x,y)
     |      
     |      Return
     |      ------
     |      Bool
     |          Is empty o not
     |  
     |  mark_place(self, xyposition)
     |      Mark a square of the board in xyposition
     |      
     |      Parameters
     |      ----------
     |      xyposition : Point
     |          Position in (x,y)
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
     |  axis_x = ('1', '2', '3', '4', '5', '6', '7', '8')
     |  
     |  axis_y = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
     |  
     |  cols = 8
     |  
     |  rows = 8
    
    class ChessPiece(builtins.object)
     |  Create a chess piece.
     |  
     |  .. versionadded:: 1.0
     |  
     |  Attributes
     |  ----------
     |  position : str
     |     Current position in algebraic notation. Example `A1`
     |  
     |  chessboard: ChessBoard
     |      The chessboard where the chess piece moves
     |  
     |  legal_move: Points
     |      Legals movements of the chess piece on the chessboard
     |  
     |  color: str
     |      The color of the chess piece
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  possible_moves(self, position, moves, rules=None, board=None)
     |      Check a square of the board where the chess piece can make a move
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      board: ChessBoard, optional
     |          The chessboard where the chess piece moves
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      ValueError
     |          If position is not in algebraic notation or is off the board
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
     |  
     |  set_color_black(self)
     |  
     |  set_color_white(self)
     |  
     |  set_legal_moves(self, position, moves, rules=None)
     |      Check that the assigned movements comply with the
     |      chess piece's movement rules
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
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
     |  name
    
    class King(ChessPiece)
     |  Create a chess piece King
     |  
     |  The King class is a subclass of `Chess Piece`, the attributes
     |  and methods are listed in the `Chess Piece` documentation
     |  
     |  .. versionadded:: 1.0
     |  
     |  Method resolution order:
     |      King
     |      ChessPiece
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  possible_moves(self, position, board=None)
     |      Check a square of the board where the King can make a move
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      board: ChessBoard, optional
     |          The chessboard where the chess piece moves
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If position is not in algebraic notation or is off the board
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from ChessPiece:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  set_color_black(self)
     |  
     |  set_color_white(self)
     |  
     |  set_legal_moves(self, position, moves, rules=None)
     |      Check that the assigned movements comply with the
     |      chess piece's movement rules
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ChessPiece:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  name
    
    class Knight(ChessPiece)
     |  Create a chess piece Knight
     |  
     |  The Knight class is a subclass of `Chess Piece`, the attributes
     |  and methods are listed in the `Chess Piece` documentation
     |  
     |  .. versionadded:: 1.0
     |  
     |  Method resolution order:
     |      Knight
     |      ChessPiece
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  possible_moves(self, position, board=None)
     |      Check a square of the board where the Knight can make a move
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      board: ChessBoard, optional
     |          The chessboard where the chess piece moves
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If position is not in algebraic notation or is off the board.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from ChessPiece:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  set_color_black(self)
     |  
     |  set_color_white(self)
     |  
     |  set_legal_moves(self, position, moves, rules=None)
     |      Check that the assigned movements comply with the
     |      chess piece's movement rules
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ChessPiece:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  name
    
    class MoveRules(builtins.object)
     |  MoveRules(max_steps, jump=False, special_move=None)
     |  
     |  Create a move rule for a chess piece in on the chessboard.
     |  
     |  .. versionadded:: 1.0
     |  
     |  Attributes
     |  ----------
     |  max_steps : int
     |      Maximum number of steps per movement in a turn.
     |  
     |  jump : bool
     |      If the chess piece can jump occupied squares
     |  
     |  special_move: dict
     |      Special movement of the chess piece in certain position
     |      on the chessboard
     |  
     |  Methods defined here:
     |  
     |  __init__(self, max_steps, jump=False, special_move=None)
     |      Parameters
     |      ----------
     |      max_steps : positive int
     |          Maximum number of steps per movement in a turn.
     |      
     |      jump : bool, optional
     |          If the chess piece can jump occupied squares
     |      
     |      special_move: (iterable, Points), optional
     |          Special movement of the chess piece in certain positions
     |          on the chessboard
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If max_steps is not positive integer
     |          If special moves has wrong number of elements
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Pawn(ChessPiece)
     |  Create a chess piece Pawn
     |  
     |  The Pawn class is a subclass of `Chess Piece`, the attributes
     |  and methods are listed in the `Chess Piece` documentation
     |  
     |  .. versionadded:: 1.0
     |  
     |  Method resolution order:
     |      Pawn
     |      ChessPiece
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  possible_moves(self, position, board=None)
     |      Check a square of the board where the Pawn can make a move
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      board: ChessBoard, optional
     |          The chessboard where the chess piece moves
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If position is not in algebraic notation or is off the board
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from ChessPiece:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  set_color_black(self)
     |  
     |  set_color_white(self)
     |  
     |  set_legal_moves(self, position, moves, rules=None)
     |      Check that the assigned movements comply with the
     |      chess piece's movement rules
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ChessPiece:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  name
    
    class Point(builtins.tuple)
     |  Point(x, y)
     |  
     |  tuple (x, y)
     |  
     |  Method resolution order:
     |      Point
     |      builtins.tuple
     |      builtins.object
     |  
     |  Static methods defined here:
     |  
     |  __new__(cls, x, y)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
    
    class Points(builtins.tuple)
     |  Points(*args)
     |  
     |  tuple (tuple (x1, y2), tuple(x2, y2), ...)
     |  
     |  Method resolution order:
     |      Points
     |      builtins.tuple
     |      builtins.object
     |  
     |  Static methods defined here:
     |  
     |  __new__(cls, *args)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
    
    class Queen(ChessPiece)
     |  Create a chess piece Queen
     |  
     |  The Queen class is a subclass of `Chess Piece`, the attributes
     |  and methods are listed in the `Chess Piece` documentation
     |  
     |  .. versionadded:: 1.0
     |  
     |  Method resolution order:
     |      Queen
     |      ChessPiece
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  possible_moves(self, position, board=None)
     |      Check a square of the board where the Queen can make a move
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      board: ChessBoard, optional
     |          The chessboard where the chess piece moves
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If position is not in algebraic notation or is off the board
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from ChessPiece:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  set_color_black(self)
     |  
     |  set_color_white(self)
     |  
     |  set_legal_moves(self, position, moves, rules=None)
     |      Check that the assigned movements comply with the
     |      chess piece's movement rules
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ChessPiece:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  name
    
    class Rook(ChessPiece)
     |  Create a chess piece Rook
     |  
     |  The Rook class is a subclass of `Chess Piece`, the attributes
     |  and methods are listed in the `Chess Piece` documentation
     |  
     |  .. versionadded:: 1.0
     |  
     |  Method resolution order:
     |      Rook
     |      ChessPiece
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  possible_moves(self, position, board=None)
     |      Check a square of the board where the Rook can make a move
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      board: ChessBoard, optional
     |          The chessboard where the chess piece moves
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If position is not in algebraic notation or is off the board
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from ChessPiece:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  set_color_black(self)
     |  
     |  set_color_white(self)
     |  
     |  set_legal_moves(self, position, moves, rules=None)
     |      Check that the assigned movements comply with the
     |      chess piece's movement rules
     |      
     |      Parameters
     |      ----------
     |      position : str
     |          Position in algebraic notation. Example `A1`
     |      
     |      moves : Points
     |          Assigned movements in a set of (x,y)
     |      
     |      rules : MovesRules, optional
     |          Move rule for a chess piece
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If moves's class is not Points
     |          If rules is not None and rules's class is not MoveRules
     |      
     |      TODO
     |      ----
     |      More rules, in addition to movement rules, can be added with
     |      a Rules parent class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ChessPiece:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  name

FUNCTIONS
    show_chessboards()
        Placing all the chess pieces in a random position,
        show their possible movements on a chessboard.

DATA
    AXIS_X = ('1', '2', '3', '4', '5', '6', '7', '8')
    AXIS_Y = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    MARK_POSITION = 1
    MSG_ERROR_LEN = '{} must be {} item (given {})'
    MSG_ERROR_POS = 'The position {} is not valid'
    MSG_ERROR_TYPE = "must be '{}' not '{}'"
    MSG_ERROR_VALUE = '{} must be a positive integer'
    OCCUPY_POSITION = 8

FILE
    /home/shersnape/Proyectos/Repositorio/challenges/chessboards/chessmoves.py


