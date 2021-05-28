#!/usr/bin/env python3

# Created by: Jonathan
# Created on: May 28, 2021
# This program displays the the numbers from 0 to 255 for each RGB

import constants


def main():
    # initilizations
    counter_red = 0
    counter_green = 0
    counter_blue = 0
    # do a nested loop do display the RGB from 0 to 50
    for counter_red in range(constants.MAX_COLOUR_VALUE):
        for counter_green in range(constants.MAX_COLOUR_VALUE):
            for counter_blue in range(constants.MAX_COLOUR_VALUE):
                # display the RGB in a list format
                print("RGB ({},{}"
                      ",{})". format(counter_red, counter_green, counter_blue))


if __name__ == "__main__":
    main()
