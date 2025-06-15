# sillytetris stuff
# https://youtu.be/nF_crEtmpBo?t=6354

import pygame
import sys
from blocks import *
from game import Game
from colors import Colors

from grid import Grid

print("sillytetris stuff")

pygame.init()

titleFont = pygame.font.Font(None, 40)

scoreSurface = titleFont.render("Score", True, Colors.white)
nextSurface = titleFont.render("Next", True, Colors.white)
gameOverSurface = titleFont.render("GAME OVER", True, Colors.white)
escToRestartSurface = titleFont.render("Press ESC to restart", True, Colors.white)
playerSurface = titleFont.render("Player", True, Colors.white)
playerValueSurface = titleFont.render("Stefanita", True, Colors.white)
pauseSurface = titleFont.render("PAUSED", True, Colors.white)

scoreRect = pygame.Rect(320, 55, 170, 60)
playerRect = pygame.Rect(320, 505, 170, 60) #(320, 455, 170, 60)
nextRect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Silly Tetris")

clock = pygame.time.Clock()

game = Game()
GAME_UPDATE = pygame.USEREVENT

pygame.time.set_timer(GAME_UPDATE, 400)

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("bye bye")
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.gameOver and event.key == pygame.K_ESCAPE:
                game.gameOver = False
                game.reset()
                print("New Game started!")

            if event.key == pygame.K_SPACE:
                if game.isPaused:
                    game.isPaused = False
                    print("Resume")
                else:
                    game.isPaused = True
                    print("Paused")

            if event.key == pygame.K_LEFT and not game.gameOver and not game.isPaused:
                game.moveLeft()

            if event.key == pygame.K_RIGHT and not game.gameOver and not game.isPaused:
                game.moveRight()

            if event.key == pygame.K_DOWN and not game.gameOver and not game.isPaused:
                game.moveDown()
                # also give some score when the user pushes the block down
                game.updateScore(0, 1)

            if event.key == pygame.K_UP and not game.gameOver and not game.isPaused:
                game.rotate()

        # update object positions
        if event.type == GAME_UPDATE and not game.gameOver and not game.isPaused:
            game.moveDown()



    # draw objects on screen
    screen.fill(Colors.darkBlue)

    screen.blit(scoreSurface, (365, 20, 50, 50))
    pygame.draw.rect(screen, Colors.lightBlue, scoreRect, 0, 10)

    screen.blit(nextSurface, (375, 180, 50, 50))
    pygame.draw.rect(screen, Colors.lightBlue, nextRect, 0, 10)

    screen.blit(playerSurface, (365, 470, 50, 50))
    pygame.draw.rect(screen, Colors.lightBlue, playerRect, 0, 10)

    scoreValueSurface = titleFont.render(str(game.score), True, Colors.white)
    screen.blit(scoreValueSurface, scoreValueSurface.get_rect(centerx = scoreRect.centerx, centery = scoreRect.centery))
    screen.blit(playerValueSurface, playerValueSurface.get_rect(centerx=playerRect.centerx, centery=playerRect.centery))

    game.draw(screen)

    if game.isPaused:
        screen.blit(pauseSurface, (105, 220, 50, 50))

    if game.gameOver == True:
        screen.blit(gameOverSurface, (85, 220, 50, 50))
        screen.blit(escToRestartSurface, (38, 250, 50, 10))

    # update display
    pygame.display.update()

    clock.tick(60)