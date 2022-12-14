import logic

class Piece:
	name: str
	is_first_move: bool
	is_alive: bool
	colour: str
	position =  []

	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None):
		self.name = name
		self.colour = colour
		self.position = self.set_default_position(position)
		self.is_first_move = self.check_if_first_move(is_first_move)
		self.is_alive = self.check_is_alive(is_alive)

	def get_offsets(self):
		pass

	def get_squares_from_offsets(self,offsets):
		squares = []
		for offset_x,offset_y in offsets:
			new_valid_square = [self.position[0] + offset_x, self.position[1] + offset_y]
			squares.append(new_valid_square)
		return squares

	def get_nth_row(self,colour,n):
		return self.get_backrank(colour) + ((n-1) * self.get_forward_direction(colour))

	def get_forward_direction(self,colour):
		if colour == "white":
			return 1
		elif colour == "black":
			return -1
		else:
			raise Exception("the piece is neither white nor black!")

	def get_ememy_colour(self):
		if self.colour == "white":
			return "black"
		elif self.colour == "black":
			return "white"

	def get_backrank(self,colour):
		if colour == "white":
			return 1
		elif colour == "black":
			return 8
		else:
			raise Exception("the piece is neither white nor black!")			

	def set_default_position(self,position):
		if position is None:
			return []
		else:
			return position

	def check_if_first_move(self,is_first_move):
		if is_first_move is None:
			return True
		else:
			return is_first_move

	def check_is_alive(self,is_alive):	
		if is_alive is None:
			return True
		else:
			return is_alive

class King(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None):
		super().__init__(name, colour, position, is_first_move, is_alive)

class Queen(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Pawn(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Rook(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Bishop(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Knight(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)
