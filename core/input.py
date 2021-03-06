# AEDIFICUS: FATHERS OF ROME
# by Ethan Aldrich

import pygame, sys, my
from pygame.locals import *

class Input:
    """A class to handle input accessible by all other classes"""
    def __init__(self):
        self.pressedKeys = []
        self.mousePressed = False
        self.mouseUnpressed = False
        self.mousePos = (0, 0)
        self.hoveredCell = (0, 0)
        

    def get(self):
        """Update variables - mouse position, occupied cell and click state, and pressed keys"""
        self.checkForQuit()
        self.mouseUnpressed = False
        self.unpressedKeys = []
        self.lastCell = self.hoveredCell
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.event.post(event)
            elif event.type == KEYDOWN:
                self.pressedKeys.append(event.key)
            elif event.type == KEYUP:
                for key in self.pressedKeys:
                    if event.key == key:
                        self.pressedKeys.remove(key)
                    self.unpressedKeys.append(key)
            elif event.type == MOUSEMOTION:
                self.mousePos = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                self.mousePressed = event.button
                self.mouseUnpressed = False
            elif event.type == MOUSEBUTTONUP:
                self.mousePressed = False
                self.mouseUnpressed = event.button
        
        if my.gameRunning:
            self.hoveredPixel = my.map.screenToGamePix(self.mousePos)
            hoveredCoords = my.map.screenToCellCoords(self.mousePos)
            if not my.UIhover and my.map.inBounds(hoveredCoords):
                self.hoveredCell = my.map.screenToCellCoords(self.mousePos)
                self.hoveredCellType = my.map.cellType(self.hoveredCell)
            else:  
                self.hoveredCell = None
                self.hoveredCellType = None


    def checkForQuit(self):
        """Terminate if QUIT events or K_ESCAPE"""
        for event in pygame.event.get(QUIT): # get all the QUIT events
            self.terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                self.terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back


    def terminate(self):
        """Safely end the program"""
        pygame.quit()
        sys.exit()