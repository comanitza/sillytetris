# sillytetris stuff
# https://youtu.be/nF_crEtmpBo?t=6354

import pygame
import sys
from blocks import *
from game import Game
from colors import Colors

from grid import Grid
class GameRunner:
    def __init__(self):
        pygame.init()

        self.titleFont = pygame.font.Font(None, 40)

        self.scoreSurface = self.titleFont.render("Score", True, Colors.white)
        self.nextSurface = self.titleFont.render("Next", True, Colors.white)
        self.gameOverSurface = self.titleFont.render("GAME OVER", True, Colors.white)
        self.escToRestartSurface = self.titleFont.render("Press ESC to restart", True, Colors.white)
        self.playerSurface = self.titleFont.render("Player", True, Colors.white)
        self.playerValueSurface = self.titleFont.render("Stefanita", True, Colors.white)
        self.pauseSurface = self.titleFont.render("PAUSED", True, Colors.white)

        self.scoreRect = pygame.Rect(320, 55, 170, 60)
        self.playerRect = pygame.Rect(320, 505, 170, 60)
        self.nextRect = pygame.Rect(320, 215, 170, 180)

        self.screen = pygame.display.set_mode((500, 620))
        pygame.display.set_caption("Silly Tetris")

        self.clock = pygame.time.Clock()

        self.game = Game()
        self.GAME_UPDATE = pygame.USEREVENT

        pygame.time.set_timer(self.GAME_UPDATE, 400)


    def runGame(self):
        while True:
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("bye bye")
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if self.game.gameOver and event.key == pygame.K_ESCAPE:
                        self.game.gameOver = False
                        self.game.reset()
                        print("New Game started!")

                    if event.key == pygame.K_SPACE:
                        if self.game.isPaused:
                            self.game.isPaused = False
                            print("Resume")
                        else:
                            self.game.isPaused = True
                            print("Paused")

                    if event.key == pygame.K_LEFT and not self.game.gameOver and not self.game.isPaused:
                        self.game.moveLeft()

                    if event.key == pygame.K_RIGHT and not self.game.gameOver and not self.game.isPaused:
                        self.game.moveRight()

                    if event.key == pygame.K_DOWN and not self.game.gameOver and not self.game.isPaused:
                        self.game.moveDown()
                        # also give some score when the user pushes the block down
                        self.game.updateScore(0, 1)

                    if event.key == pygame.K_UP and not self.game.gameOver and not self.game.isPaused:
                        self.game.rotate()

                # update object positions
                if event.type == self.GAME_UPDATE and not self.game.gameOver and not self.game.isPaused:
                    self.game.moveDown()

                # draw objects on screen
                self.screen.fill(Colors.darkBlue)

                self.screen.blit(self.scoreSurface, (365, 20, 50, 50))
                pygame.draw.rect(self.screen, Colors.lightBlue, self.scoreRect, 0, 10)

                self.screen.blit(self.nextSurface, (375, 180, 50, 50))
                pygame.draw.rect(self.screen, Colors.lightBlue, self.nextRect, 0, 10)

                self.screen.blit(self.playerSurface, (365, 470, 50, 50))
                pygame.draw.rect(self.screen, Colors.lightBlue, self.playerRect, 0, 10)

                scoreValueSurface = self.titleFont.render(str(self.game.score), True, Colors.white)
                self.screen.blit(scoreValueSurface, scoreValueSurface.get_rect(centerx = self.scoreRect.centerx, centery = self.scoreRect.centery))
                self.screen.blit(self.playerValueSurface, self.playerValueSurface.get_rect(centerx=self.playerRect.centerx, centery=self.playerRect.centery))

                self.game.draw(self.screen)

                if self.game.isPaused:
                    self.screen.blit(self.pauseSurface, (105, 220, 50, 50))

                if self.game.gameOver == True:
                    self.screen.blit(self.gameOverSurface, (85, 220, 50, 50))
                    self.screen.blit(self.escToRestartSurface, (38, 250, 50, 10))

                # update display
                pygame.display.update()

                self.clock.tick(60)