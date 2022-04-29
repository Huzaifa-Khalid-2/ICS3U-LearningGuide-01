for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                     lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                     aliens[alien_number].x + 1, aliens[alien_number].y,
                                     aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                       # you hit an alien
                       aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                       lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                       sound.stop()
                       sound.play(boom_sound)
                       show_alien()
                       show_alien()
                       score = score + 1
                      
                      
                          # for score
    score = 0
