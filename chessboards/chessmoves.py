import random

OCCUPY_POSITION = 8
MARK_POSITION = 1
AXIS_Y = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
AXIS_X = tuple([str(i) for i in range(1, 9)])

MSG_ERROR_VALUE = "{} must be a positive integer"
MSG_ERROR_LEN = "{} must be {} item (given {})"
MSG_ERROR_POS = "The position {} is not valid"
MSG_ERROR_TYPE = "must be '{}' not '{}'"


class MoveRules():
    """Create a move rule for a chess piece in on the chessboard.

    .. versionadded:: 1.0

    Attributes
    ----------
    max_steps : int
        Maximum number of steps per movement in a turn.

    jump : bool
        If the chess piece can jump occupied squares

    special_move: dict
        Special movement of the chess piece in certain position
        on the chessboard

    """
    def __init__(self, max_steps, jump=False, special_move=None):
        """
        Parameters
        ----------
        max_steps : positive int
            Maximum number of steps per movement in a turn.

        jump : bool, optional
            If the chess piece can jump occupied squares

        special_move: (iterable, Points), optional
            Special movement of the chess piece in certain positions
            on the chessboard

        Raises
        ------
        ValueError
            If max_steps is not positive integer
            If special moves has wrong number of elements

        """

        if max_steps < 1:
            raise ValueError(MSG_ERROR_VALUE.format("max_steps"))

        self.max_steps_for_turn = max_steps
        self.jump_piece_in_path = jump

        if special_move is not None:
            self._check_special_move(special_move)
        else:
            self.special_move_for_position = {}

    def _check_special_move(self, special_move):
        if len(special_move) != 2:
            raise ValueError(MSG_ERROR_LEN.format("special_move",
                                                  2, len(special_move)))
        self.special_move_for_position = {'positions': special_move[0],
                                          'newmove': special_move[1]}


class Point(tuple):
    """tuple (x, y)

    """
    def __new__(cls, x, y):
        return tuple.__new__(Point, (x, y))


class Points(tuple):
    """tuple (tuple (x1, y2), tuple(x2, y2), ...)

    """
    def __new__(cls, *args):
        return tuple.__new__(Points, (Point(*arg) for arg in args))


class ChessBoard():
    """Create chessboard.

    .. versionadded:: 1.0

    Algebraic notation (chess)
      _______________
    8|_|_|_|_|_|_|_|_|
    7|_|_|_|_|_|_|_|_|
    6|_|_|_|_|_|_|_|_|
    5|_|_|_|_|_|_|_|_|
    4|_|_|_|_|_|_|_|_|
    3|_|_|_|_|_|_|_|_|
    2|_|_|_|_|_|_|_|_|
    1|_|_|_|_|_|_|_|_|
      A B C D E F G H

    Attributes
    ----------
    state : list of list
        8x8 chess board represented in a list of lists.
        Empty square of the board have a value of 0.

    """
    axis_y = AXIS_Y
    axis_x = AXIS_X
    rows = len(axis_y)
    cols = len(axis_x)

    def __init__(self):
        self.state = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def _as_number_form(self, position):
        pos_y = self.axis_y.index(position[0])
        pos_x = self.axis_x[::-1].index(position[1])
        return pos_x, pos_y

    def _as_string_form(self, xyposition):
        if self._is_in_bounds(xyposition):
            return self.axis_y[xyposition[1]] + self.axis_x[-xyposition[0]-1]
        else:
            return "--"

    def _is_in_bounds(self, xyposition):
        pos_x, pos_y = xyposition
        return 0 <= pos_x <= self.rows - 1 and 0 <= pos_y <= self.cols - 1

    def _is_empty(self, xyposition):
        pos_x, pos_y = xyposition
        return self.state[pos_x][pos_y] != OCCUPY_POSITION

    def _is_valid_position(self, position):
        position = position.upper()
        col, row = position
        return col in self.axis_y and row in self.axis_x

    def is_free_position(self, position):
        """Check a square of the board in position is free

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        Return
        ------
        Bool
            Is empty o not
        """

        xyposition = self._as_number_form(position)
        return self._is_valid_position(position) and self._is_empty(xyposition)

    def is_free_xyposition(self, xyposition):
        """Check a square of the board in xyposition is free

        Parameters
        ----------
        xyposition : Point
            Position in (x,y)

        Return
        ------
        Bool
            Is empty o not
        """

        return self._is_in_bounds(xyposition) and self._is_empty(xyposition)

    def in_place(self, position):
        """Place a chess piece in one position

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        Raises
        ------
        ValueError
            If position is not in algebraic notation or is off the board

        """
        if self.is_free_position(position):
            pos_x, pos_y = self._as_number_form(position)
            self.state[pos_x][pos_y] = OCCUPY_POSITION
        else:
            raise ValueError(MSG_ERROR_POS.format(position))

    def mark_place(self, xyposition):
        """Mark a square of the board in xyposition

        Parameters
        ----------
        xyposition : Point
            Position in (x,y)

        """
        if self.is_free_xyposition(xyposition):
            pos_x, pos_y = xyposition
            self.state[pos_x][pos_y] = MARK_POSITION

    def __repr__(self):
        board = self.state.copy()
        board.extend([["─"]*self.cols, self.axis_y])
        new_board = []
        for i, row in enumerate(board):
            if i < self.rows:
                change_row = [" %d|" % (self.rows - i)]
            else:
                change_row = ["   "]
            change_row.extend([str(cell) for cell in row])
            new_board.append(change_row)
        list_board = [' '.join([cell for cell in row]) for row in new_board]
        nice_board = '\n'.join(list_board)
        return nice_board


class ChessPiece(object):
    """Create a chess piece.

    .. versionadded:: 1.0

    Attributes
    ----------
    position : str
       Current position in algebraic notation. Example `A1`

    chessboard: ChessBoard
        The chessboard where the chess piece moves

    legal_move: Points
        Legals movements of the chess piece on the chessboard

    color: str
        The color of the chess piece

    """

    def __init__(self):
        self.position = None
        self.chessboard = None
        self.legal_moves = None
        self.color = "white"

    def set_color_black(self):
        self.color = "black"

    def set_color_white(self):
        self.color = "white"

    def set_legal_moves(self, position, moves, rules=None):
        """Check that the assigned movements comply with the
        chess piece's movement rules

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        moves : Points
            Assigned movements in a set of (x,y)

        rules : MovesRules, optional
            Move rule for a chess piece

        Raises
        ------
        TypeError
            If moves's class is not Points
            If rules is not None and rules's class is not MoveRules

        TODO
        ----
        More rules, in addition to movement rules, can be added with
        a Rules parent class.

        """

        if isinstance(moves, Points):
            nrow = self.chessboard.rows - 1
            ncol = self.chessboard.cols - 1
            self.legal_moves = Points(*(m for m in moves if abs(m[0]) < nrow
                                        and abs(m[1]) < ncol))
        else:
            s = moves.__class__.__name__
            raise TypeError(MSG_ERROR_TYPE.format("Points", s))

        if rules is None:
            self.rules_move = MoveRules(
                max(self.chessboard.rows, self.chessboard.cols))
        elif isinstance(rules, MoveRules):
            self.rules_move = rules
        else:
            s = rules.__class__.__name__
            raise TypeError(MSG_ERROR_TYPE.format("MoveRules", s))

        check_moves = position in \
            self.rules_move.special_move_for_position.get("positions", {})

        if check_moves:
            self.legal_moves += \
                self.rules_move.special_move_for_position["newmove"]

    def possible_moves(self, position,
                       moves,
                       rules=None,
                       board=ChessBoard()):
        """Check a square of the board where the chess piece can make a move

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        moves : Points
            Assigned movements in a set of (x,y)

        rules : MovesRules, optional
            Move rule for a chess piece

        board: ChessBoard, optional
            The chessboard where the chess piece moves

        Raises
        ------
        TypeError
            If moves's class is not Points
            If rules is not None and rules's class is not MoveRules
        ValueError
            If position is not in algebraic notation or is off the board

        TODO
        ----
        More rules, in addition to movement rules, can be added with
        a Rules parent class.

        """
        self.position = position
        self.chessboard = board
        self.chessboard.in_place(position)
        place = self.chessboard._as_number_form(position)

        self.set_legal_moves(position, moves, rules)

        for move in self.legal_moves:
            for step in range(1, self.rules_move.max_steps_for_turn + 1):
                dest = Point(place[0]+move[0]*step, place[1]+move[1]*step)

                dest_is_empty = self.chessboard.is_free_xyposition(dest)
                piece_can_jump = self.rules_move.jump_piece_in_path
                stop_move = not dest_is_empty and not piece_can_jump
                if stop_move:
                    break

                self.chessboard.mark_place(dest)

    @property
    def name(self):
        return self.__class__.__name__

    def __repr__(self):
        return "<" + self.name + ">"


class Pawn(ChessPiece):
    """Create a chess piece Pawn

    The Pawn class is a subclass of `Chess Piece`, the attributes
    and methods are listed in the `Chess Piece` documentation

    .. versionadded:: 1.0

    """
    def __init__(self):
        ChessPiece.__init__(self)

    def possible_moves(self, position, board=ChessBoard()):
        """Check a square of the board where the Pawn can make a move

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        board: ChessBoard, optional
            The chessboard where the chess piece moves

        Raises
        ------
        ValueError
            If position is not in algebraic notation or is off the board

        """
        moves = Points((-1, 0), ) if self.color == "white" else Points((1, 0),)
        positions = (l+"2" for l in AXIS_Y)
        special = Points((-2, 0),) \
            if self.color == "white" else Points((2, 0),)
        rules = MoveRules(1, special_move=(positions, special))
        return super(Pawn, self).possible_moves(position, moves,
                                                rules=rules, board=board)


class Knight(ChessPiece):
    """Create a chess piece Knight

    The Knight class is a subclass of `Chess Piece`, the attributes
    and methods are listed in the `Chess Piece` documentation

    .. versionadded:: 1.0

    """
    def __init__(self):
        ChessPiece.__init__(self)

    def possible_moves(self, position, board=ChessBoard()):
        """Check a square of the board where the Knight can make a move

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        board: ChessBoard, optional
            The chessboard where the chess piece moves

        Raises
        ------
        ValueError
            If position is not in algebraic notation or is off the board.

        """
        moves = Points((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1))

        rules = MoveRules(1, jump=True)
        return super(Knight, self).possible_moves(position, moves,
                                                  rules=rules, board=board)


class Rook(ChessPiece):
    """Create a chess piece Rook

    The Rook class is a subclass of `Chess Piece`, the attributes
    and methods are listed in the `Chess Piece` documentation

    .. versionadded:: 1.0

    """
    def __init__(self):
        ChessPiece.__init__(self)

    def possible_moves(self, position, board=ChessBoard()):
        """Check a square of the board where the Rook can make a move

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        board: ChessBoard, optional
            The chessboard where the chess piece moves

        Raises
        ------
        ValueError
            If position is not in algebraic notation or is off the board

        """
        moves = Points((-1, 0), (0, -1), (0, 1), (1, 0))
        return super(Rook, self).possible_moves(position, moves, board=board)


class Bishop(ChessPiece):
    """Create a chess piece Bishop

    The Bishop class is a subclass of `Chess Piece`, the attributes
    and methods are listed in the `Chess Piece` documentation

    .. versionadded:: 1.0

    """
    def __init__(self):
        ChessPiece.__init__(self)

    def possible_moves(self, position, board=ChessBoard()):
        """Check a square of the board where the Bishop can make a move

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        board: ChessBoard, optional
            The chessboard where the chess piece moves

        Raises
        ------
        ValueError
            If position is not in algebraic notation or is off the board

        """
        moves = Points((-1, -1), (-1, 1), (1, -1), (1, 1))
        return super(Bishop, self).possible_moves(position, moves, board=board)


class Queen(ChessPiece):
    """Create a chess piece Queen

    The Queen class is a subclass of `Chess Piece`, the attributes
    and methods are listed in the `Chess Piece` documentation

    .. versionadded:: 1.0

    """
    def __init__(self):
        ChessPiece.__init__(self)

    def possible_moves(self, position, board=ChessBoard()):
        """Check a square of the board where the Queen can make a move

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        board: ChessBoard, optional
            The chessboard where the chess piece moves

        Raises
        ------
        ValueError
            If position is not in algebraic notation or is off the board

        """
        moves = Points((-1, 0), (0, -1), (0, 1), (1, 0),
                       (-1, -1), (-1, 1), (1, -1), (1, 1))
        return super(Queen, self).possible_moves(position, moves, board=board)


class King(ChessPiece):
    """Create a chess piece King

    The King class is a subclass of `Chess Piece`, the attributes
    and methods are listed in the `Chess Piece` documentation

    .. versionadded:: 1.0

    """
    def __init__(self):
        ChessPiece.__init__(self)

    def possible_moves(self, position, board=ChessBoard()):
        """Check a square of the board where the King can make a move

        Parameters
        ----------
        position : str
            Position in algebraic notation. Example `A1`

        board: ChessBoard, optional
            The chessboard where the chess piece moves

        Raises
        ------
        ValueError
            If position is not in algebraic notation or is off the board

        """
        moves = Points((-1, 0), (0, -1), (0, 1), (1, 0),
                       (-1, -1), (-1, 1), (1, -1), (1, 1))
        rules = MoveRules(1)
        return super(King, self).possible_moves(position, moves,
                                                rules=rules, board=board)


def show_chessboards():
    """Placing all the chess pieces in a random position,
    show their possible movements on a chessboard.

    """
    pieces = [Pawn(), Knight(), Bishop(),
              Rook(), Queen(), King()]

    random_position = random.choice(AXIS_Y) + random.choice(AXIS_X)

    for piece in pieces:
        piece.possible_moves(random_position)
        print("\n**-> " + piece.name + ' <-**\n')
        print(piece.chessboard)


if __name__ == "__main__":
    show_chessboards()
