import pygame_widgets as pw


class Button(pw.Button):

    def draw(self, surface):
        self.win = surface
        super().draw()
