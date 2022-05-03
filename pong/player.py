import pygame
from paddle import Paddle

class Player():

    def __init__(self, nickname: str, paddle_width: int, paddle_height: int, paddle_x: int, paddle_y: int) -> None:
        """Creates a player with attributes"""
        self._score = 0
        self._nickname = nickname
        self._ai = False
        self.paddle = Paddle(paddle_x, paddle_y, paddle_width, paddle_height)

    def get_lives(self) -> int:
        """Returns lives of player"""
        return self._score

    def set_lives(self, score: int) -> None:
        """Sets lives of players"""
        self._lives = score

    def get_ai(self) -> bool:
        """Returns True if player 2 is an AI. Otherwise False"""
        return self._ai

    def set_ai(self, ai: bool) -> None:
        """Sets whether or not player 2 is an AI"""
        self._ai = ai

