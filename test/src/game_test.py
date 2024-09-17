from inspect import cleandoc

import pytest

from src.game import Game
from src.world import World


def test_start_game():
    game = Game()
    assert game.print() == cleandoc(
        '''
        Cryosleep Chamber

        The metallic chamber is dimly lit, with frost covering the glass of several cryopods. Some are occupied, others flicker with an eerie red light. A control panel by the wall is flashing, signalling a malfunction. An airlock door to the south hums quietly, waiting to be opened.
        '''
    )


def test_can_look_at_exists():
    game = Game()
    assert game.run_command("LOOK S") == "I can see an exit: Abandoned Research Lab"


def test_nothing_to_look_at():
    game = Game()
    assert game.run_command("LOOK N") == "Nothing interesting to look at there!"


def test_can_move_to_new_room():
    game = Game()
    assert game.run_command("GO N") == "You can't go there you dummy"


def test_move_to_new_location():
    game = Game()
    new_location = World.locations[1]
    assert game.run_command("GO S") == f"{new_location.title}\n\n{new_location.description}"
