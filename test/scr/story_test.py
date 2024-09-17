import pytest

from src.game import Game


def test_start_game():
    game = Game()
    assert game.print() == '''
## 1. Cryosleep Chamber

The metallic chamber is dimly lit, with frost covering the glass of several cryopods. Some are occupied, others flicker with an eerie red light. A control panel by the wall is flashing, signalling a malfunction. An airlock door to the south hums quietly, waiting to be opened.

Items: Cryopod Keycard, Emergency Toolkit
Objects: Cryopod (can be opened), Control Panel (can be used)
'''
