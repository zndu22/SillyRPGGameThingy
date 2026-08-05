from constants import *
import heapq
import math
from collections import deque
from Node import Node

# Very kindly provided by my dear friend Chet Gepeiti, ofc slightly edited and fixed by yours truly
class Pathfinder:

	def __init__(self, world, walkableTiles):
		self.world = world
		self.path = deque()
		self.walkableTiles = walkableTiles

	# sets the path variable to a list of movements to get to the end.
	def findPath(self, start, goal):
		openSet = []
		closedSet = set()
		nodes = {}
		startNode = Node(start)
		startNode.gCost = 0
		startNode.hCost = self.heuristic(start, goal)
		nodes[start] = startNode

		heapq.heappush(openSet, (startNode.fCost, start))

		while openSet:
			_, currentPos = heapq.heappop(openSet)
			if currentPos in closedSet:
				continue
			current = nodes[currentPos]
			if currentPos == goal:
				self.path = deque(self.reconstructPath(current))
				return
			closedSet.add(currentPos)
			for neighborPos, movementCost in self.getNeighbors(currentPos):
				if neighborPos in closedSet:
					continue
				tentativeG = current.gCost + movementCost
				if neighborPos not in nodes:
					node = Node(neighborPos)
					node.parent = current
					node.gCost = tentativeG
					node.hCost = self.heuristic(neighborPos, goal)
					nodes[neighborPos] = node
					heapq.heappush(
						openSet,
						(node.fCost, neighborPos)
					)

				else:
					node = nodes[neighborPos]
					if tentativeG < node.gCost:
						node.gCost = tentativeG
						node.parent = current

						heapq.heappush(
							openSet,
							(node.fCost, neighborPos)
						)

		return []

	def getNeighbors(self, position):
		x, y = position
		offsets = [
			(-1,-1), (0,-1), (1,-1),
			(-1, 0),         (1, 0),
			(-1, 1), (0, 1), (1, 1)
		]
		neighbors = []

		for dx, dy in offsets:
			nx = x + dx
			ny = y + dy
			if self.world.worldMap.getPixel(nx, ny) in self.walkableTiles:
				continue
			#
			# Prevent corner cutting
			#
			if dx != 0 and dy != 0:

				if (
					# not self.world.isWalkable(x + dx, y)
					# or
					# not self.world.isWalkable(x, y + dy)
					
					not self.world.worldMap.getPixel(x+dx, y) in self.walkableTiles
					or
					not self.world.worldMap.getPixel(x, y+dy) in self.walkableTiles

				):
					continue
			if dx == 0 or dy == 0:
				cost = 1.0
			else:
				cost = math.sqrt(2)
			neighbors.append(((nx, ny), cost))
		return neighbors

	def heuristic(self, a, b):
		dx = abs(a[0] - b[0])
		dy = abs(a[1] - b[1])
		return max(dx, dy) + 0.41421356237 * min(dx, dy)

	def reconstructPath(self, node):
		positions = []

		while node is not None:
			positions.append(node.position)
			node = node.parent
		positions.reverse()
		#
		# Convert positions into movement vectors
		#
		moves = []
		for i in range(1, len(positions)):
			x0, y0 = positions[i - 1]
			x1, y1 = positions[i]
			moves.append((x1 - x0, y1 - y0))
		return moves

	# returns and pops the next move in the path
	def nextMove(self):
		if self.path:
			return self.path.popleft()
		return None

	def hasPath(self):
		return len(self.path) > 0

	def finishedPath(self):
		return len(self.path) == 0
