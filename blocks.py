from colors import Colors
from position import Position

import pygame


class Block:
    def __init__(self, id):

        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rotationState = 0
        self.colors = Colors.getCellColors()
        self.rowOffset = 0
        self.colOffset = 0


    def draw(self, screen, offsetX, offsetY):
        tiles = self.getCellPostions()

        for tile in tiles:
            tileRect = pygame.Rect(tile.col * self.cellSize + offsetX, tile.row * self.cellSize + offsetY, self.cellSize - 1, self.cellSize - 1)
            pygame.draw.rect(screen, self.colors[self.id], tileRect)

    def move(self, rows, cols):
        self.rowOffset += rows
        self.colOffset += cols

    def getCellPostions(self):
        tiles = self.cells[self.rotationState]
        movedTiles = []

        for tile in tiles:
            movedTiles.append(Position(tile.row + self.rowOffset, tile.col + self.colOffset))

        return movedTiles

    def rotate(self):
        self.rotationState += 1

        if self.rotationState >= len(self.cells):
            self.rotationState = 0

    def undoRotate(self):
        self.rotationState -= 1

        if self.rotationState <= 0:
            self.rotationState = len(self.cells) - 1

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)

        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)


class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)

        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)


class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)

        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)

        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            1: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)

        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)


class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)

        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)

        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)

