from grid import Grid
from blocks import  *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [TBlock(), LBlock(), JBlock(), SBlock(), ZBlock(), IBlock(), OBlock()]

        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()

        self.gameOver = False

        self.score = 0

        self.isPaused = False

    def getRandomBlock(self):
        if len(self.blocks) == 0:
            self.blocks = [TBlock(), LBlock(), JBlock(), SBlock(), ZBlock(), IBlock(), OBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)

        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen, 11, 11)

        if self.nextBlock.id == 3:
            self.nextBlock.draw(screen, 255, 290)
        elif (self.nextBlock.id == 4):
            self.nextBlock.draw(screen, 255, 280)
        else:
            self.nextBlock.draw(screen, 270, 270)



    def moveLeft(self):
        self.currentBlock.move(0, -1)
        if not self.isBlockInside() or not self.blocFits():
            self.currentBlock.move(0, 1)

    def moveRight(self):
        self.currentBlock.move(0, 1)
        if not self.isBlockInside() or not self.blocFits():
            self.currentBlock.move(0, -1)

    def moveDown(self):
        self.currentBlock.move(1, 0)
        if not self.isBlockInside() or not self.blocFits():
            self.currentBlock.move(-1, 0)
            self.lockBlock()

    def lockBlock(self):
        tiles = self.currentBlock.getCellPostions()
        for tile in tiles:
            self.grid.grid[tile.row][tile.col] = self.currentBlock.id

        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()

        clearedRows = self.grid.clearFullRows()

        self.updateScore(clearedRows, 0)

        # determine if we need to be game over
        if not self.blocFits():
            self.gameOver = True
            print("Game over :(")

    def isBlockInside(self):
        tiles = self.currentBlock.getCellPostions()

        for tile in tiles:
            if not self.grid.isInside(tile.row, tile.col):
                return False

        return True

    def rotate(self):
        self.currentBlock.rotate()

        if not self.isBlockInside() or not self.blocFits():
            self.currentBlock.undoRotate()


    def blocFits(self) -> bool:

        tiles = self.currentBlock.getCellPostions()

        for tile in tiles:
            if not self.grid.isEmptyCell(tile.row, tile.col):
                return False

        return True

    def reset(self):
        self.grid.reset()
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        self.score = 0


    def updateScore(self, linesCleared, blocksMovedDown):

        if linesCleared == 1:
            self.score += 100
        elif linesCleared == 2:
            self.score += 300
        elif linesCleared >= 3:
            self.score += 500

        self.score += blocksMovedDown


