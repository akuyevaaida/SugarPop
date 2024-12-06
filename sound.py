#############################################################
# Module Name: Sugar Pop Sound Module
# Project: Sugar Pop Program
# Date: Dec 6, 2024
# By: Aida Akuyeva
# Description: The sound implementation of the sugar pop game
#############################################################

import pygame.mixer as mixer
from settings import *

class Sound:
    def __init__(self):
        # Initialize the mixer
        mixer.init()
        
        self.sounds = {} # Dictionary to store sounds 

        # Assign channels for specific sounds
        self.channels = {
            "bucket_explode": mixer.Channel(0),
            "sugar_add": mixer.Channel(1),
            "level_complete": mixer.Channel(2)
        }

        # Load sounds
        self.load_sounds()

    def load_sounds(self):
        ''' Load all sounds from file paths.'''
        
        self.sounds = {
            "bucket_explode": mixer.Sound(SOUND_BUCKET_EXPLODE),
            "sugar_add": mixer.Sound(SOUND_SUGAR_ADD),
            "level_complete": mixer.Sound(SOUND_LEVEL_COMPLETE)
        }

    def play_sound(self, name):
        ''' Play a sound by its name on a specific channel.
        :param name: Key of the sound in the sounds dictionary.'''
        
        if name in self.sounds and name in self.channels:
            self.channels[name].play(self.sounds[name])



