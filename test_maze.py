import maze
import unittest

class TryTesting(unittest.TestCase):

	def test_maze1(self):
		laberinto = maze.Maze("maze1.txt")
		laberinto.solve()
		self.assertEqual(laberinto.solution,(['up', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'up', 'up'], [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (1, 5), (0, 5)]))

	def test_maze2(self):
		laberinto = maze.Maze("maze2.txt")
		laberinto.solve()
		self.assertEqual(laberinto.solution,(['right', 'right', 'right', 'right', 'right', 'right', 'up', 'up', 'up', 'left', 'left', 'left', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down'], [(15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (14, 6), (13, 6), (12, 6), (12, 5), (12, 4), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (8, 4), (8, 5), (8, 6), (7, 6), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (7, 13), (8, 13)]))

	def test_maze3(self):
		laberinto = maze.Maze("maze3.txt")
		laberinto.solve()
		self.assertEqual(laberinto.solution,(['up', 'right', 'up', 'up'], [(4, 0), (4, 1), (3, 1), (2, 1)]))

	def test_maze4(self):
		laberinto = maze.Maze("mazeT1.txt")
		laberinto.solve()
		self.assertEqual(laberinto.solution,(['down', 'left', 'left', 'up'], [(1, 3), (1, 2), (1, 1), (0, 1)]))

	def test_maze5(self):
		laberinto = maze.Maze("mazeT2.txt")
		laberinto.solve()
		self.assertEqual(laberinto.solution,(['up', 'up', 'right', 'right', 'right', 'right', 'right'], [(2, 6), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11)]))

