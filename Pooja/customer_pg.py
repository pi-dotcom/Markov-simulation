#!/usr/bin/env python
# coding: utf-8

# In[ ]:

OFS = 50
TILE_SIZE=32
class Customer:

    def __init__(self, terrain_map, image, x, y):

        self.terrain_map = terrain_map
        self.image = image
        self.x = x
        self.y = y
        
    def draw(self, frame):
        xpos = OFS + self.x * TILE_SIZE
        xpos1 = OFS + (self.x+1) * TILE_SIZE
        ypos = OFS + self.y * TILE_SIZE
        ypos1 = OFS + (self.y+1) * TILE_SIZE
        
        frame[ypos:ypos1, xpos:xpos1] = self.image
        
        
    def move(self, direction):
        newx = self.x
        newy = self.y
        if direction == 'up':
            newy -= 1
        elif direction == 'down':
            newy += 1
        elif direction == 'right':
            newx += 1
        elif direction == 'left':
            newx -= 1

        if self.terrain_map.contents[newy][newx] == '.':
            self.x = newx
            self.y = newy

