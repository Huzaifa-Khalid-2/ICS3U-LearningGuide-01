#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This constants file is for the space aliens game

# PyBadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5
NEOPIXEL_COUNT = 5
NEOPIXEL_BRIGHTNESS = 10
SHIP_SPEED = 1
ALIEN_SPEED = 1
LASER_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just_pressed",
    "button_still_pressed": "still_pressed",
    "button_released": "released",
}

# new pallete for red filled text
RED_PALETTE = (b'\xf8\x1f\x00\x00\xcey\x00\xff\xf8\x1f\xff\x19\xfc\xe0\xfd\xe0'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff')

# new pallete for blue filled text
WHI_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff')
