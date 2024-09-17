from .world import world, Location

class Game():
    location: Location

    def __init__(self):
        self.location = world[0]

    def print(self):
        return self.location.print()

    def run_command(self, command: str) -> str:
        cmd = command.split(" ")
        if cmd[0] == "LOOK":
            exit = self.location.exits.get(cmd[1])
            if exit:
                return f"I can see an exit: {exit}"
            else:
                return "Nothing interesting to look at there!"
