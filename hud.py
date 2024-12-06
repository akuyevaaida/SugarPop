import pygame as pg
from settings import *

class Hud:
    def __init__(self, font_size=20, font_color=(255, 255, 255), bg_color=(255, 0, 0)):
        self.font = pg.font.SysFont("Open Sans", font_size)  
        self.font_color = font_color
        self.bg_color = bg_color  

    def draw(self, screen, total_sugar_count, sugar_left, buckets, gravity_reversed):
        ''' Draw the HUD with round borders.'''
        
        # Calculate dynamic height based on the number of lines
        new_height = HUD_HEIGHT + len(buckets) * 20 + 40  # Adjust for bucket count + gravity line
        hud_surface = pg.Surface((HUD_WIDTH, new_height), pg.SRCALPHA)
        pg.draw.rect(hud_surface, self.bg_color, (0, 0, HUD_WIDTH, new_height), border_radius=20)

        y_offset = 10

        # Draw Total Sugar Count
        remaining_sugar = int(total_sugar_count) - int(sugar_left)
        text_surface = self.font.render(f"Remaining Sugar: {remaining_sugar} / {total_sugar_count}", True, self.font_color)
        hud_surface.blit(text_surface, (10, y_offset))

        # Draw Bucket Counts
        y_offset += 20
        for index, bucket in enumerate(buckets):
            bucket_text = f"Bucket {index + 1}: {bucket.count}/{bucket.needed_sugar}"
            bucket_surface = self.font.render(bucket_text, True, self.font_color)
            hud_surface.blit(bucket_surface, (10, y_offset))
            y_offset += 20

        # Display Gravity Direction
        gravity_text = "Gravity: Up" if gravity_reversed else "Gravity: Down"
        gravity_surface = self.font.render(gravity_text, True, self.font_color)
        hud_surface.blit(gravity_surface, (10, y_offset))

        # Blit the entire HUD surface onto the screen
        screen.blit(hud_surface, (10, 10))
