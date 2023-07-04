"""
Title: Arcade Template
Name: Jonah Honsberger
Date: 10/28/2022 [MM-DD-YYYY]
"""

import arcade
import random

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "game template"


CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

class Template:
   def __init__(self):
       self.y = CENTER_Y
       self.x = CENTER_X
       self.a = 1

   def update(self):

       """do calculations for animations here"""
       self.x = self.x + 5
       if self.x > SCREEN_WIDTH:
           self.x = 0

   def draw(self):
       LENGTH = random.randint(0, 999)
       WIDTH = random.randint(0, 999)

       arcade.start_render()
       arcade.draw_rectangle_filled(self.x, self.y, WIDTH, LENGTH, (self.x % 255, 255 - self.x % 255, 0))


class MyGame(arcade.Window):
   """ Main application class. """

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       # Create our rectangle
       self.template = Template()

       # Set background color
       arcade.set_background_color(arcade.color.BLACK)

   def on_update(self, delta_time):
       # Move the rectangle
       self.template.update()

   def on_draw(self):
       """ Render the screen. """

       # Clear screen
       self.clear()
       # Draw the rectangle
       self.template.draw()


def main():
   """ Main function """
   MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   arcade.run()


if __name__ == "__main__":
   main()

