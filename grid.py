import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.cellSize = 30

        self.grid = [[0 for j in range (self.cols)] for i in range(self.rows)]
        self.colors = Colors.getCellColors()


    def printGrid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end = " ")
            print()

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cellValue = self.grid[row][col]
                cellRect = pygame.Rect(col * self.cellSize + 11, row * self.cellSize + 11, self.cellSize - 1, self.cellSize - 1)

                pygame.draw.rect(screen, self.colors[cellValue], cellRect)


    def isInside(self, row, col):
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            return True
        return False

    def isEmptyCell(self, row, col):
        return self.grid[row][col] == 0

    def isRowFull(self, row):
        for cell in self.grid[row]:
            if cell == 0:
                return False

        return True

    def clearRow(self, row):
        for col in range(self.cols):
            self.grid[row][col] = 0

    def moveRowDown(self, row, numberOfRows):
        for col in range(self.cols):
            self.grid[row + numberOfRows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clearFullRows(self) -> int:
        completed = 0

        for row in range(self.rows - 1, 0, -1):
            if self.isRowFull(row):
                self.clearRow(row)
                completed += 1
            elif completed > 0:
                self.moveRowDown(row, completed)

        return completed

    def reset(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = 0
