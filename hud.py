#############################################################
# Module Name: Sugar Pop Hud Module
# Project: Sugar Pop Program
# Date: Dec 6, 2024
# By: Aida Akuyeva
# Description: The hud implementation of the sugar pop game
#############################################################

import pygame as pg
from settings import *

class Hud:
    def __init__(self, font_size=20, font_color=(255, 255, 255), bg_color=(255, 0, 0)):
        self.font = pg.font.SysFont("Open Sans", font_size)  
        self.font_color = font_color
        self.bg_color = bg_color  
        
    def draw(self, screen, total_sugar_count, sugar_dropped, level_number, buckets, gravity_reversed, show_hud=True):
        ''' Draw the HUD with round borders.'''
        if not show_hud:
            return  # Skip if Hud isn't displayed
    
        # Calculate height based on the number of lines
        new_height = HUD_HEIGHT + len(buckets) * 20 + 40  # Adjust for bucket count + gravity line
        hud_surface = pg.Surface((HUD_WIDTH, new_height), pg.SRCALPHA)
        pg.draw.rect(hud_surface, self.bg_color, (0, 0, HUD_WIDTH, new_height), border_radius=20)

        y_offset = 10

        # Draw Remaining Sugar Count
        remaining_sugar = total_sugar_count - sugar_dropped
        text_surface = self.font.render(f"Remaining Sugar: {remaining_sugar}/{total_sugar_count}", True, self.font_color)
        hud_surface.blit(text_surface, (10, y_offset))

        # Draw Level Count
        y_offset += 18
        level_surface = self.font.render(f"Level: {level_number}", True, self.font_color)
        hud_surface.blit(level_surface, (10, y_offset))

        # Draw Bucket Counts
        y_offset += 18
        for index, bucket in enumerate(buckets):
            bucket_text = f"Bucket {index + 1}: {bucket.count}/{bucket.needed_sugar}"
            bucket_surface = self.font.render(bucket_text, True, self.font_color)
            hud_surface.blit(bucket_surface, (10, y_offset))
            y_offset += 18

        # Display Gravity Direction
        if gravity_reversed:
            gravity_text = "Gravity: Up" 
        else:
            gravity_text = "Gravity: Down"
        gravity_surface = self.font.render(gravity_text, True, self.font_color)
        hud_surface.blit(gravity_surface, (10, y_offset))

        # Blit the entire HUD surface onto the screen
        screen.blit(hud_surface, (10, 10))
