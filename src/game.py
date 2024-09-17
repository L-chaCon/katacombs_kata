from .world import Location, World


class Game:
    location: Location

    def __init__(self):
        self.location = World.locations[0]

    def print(self) -> str:
        return self.location.print()

    def run_command(self, command: str) -> str:
        cmd = command.split(" ")
        if cmd[0] == "LOOK":
            location_title = self.location.exits.get(cmd[1])
            if location_title:
                return f"I can see an exit: {location_title}"
            else:
                return "Nothing interesting to look at there!"

        if cmd[0] == "GO":
            location_title = self.location.exits.get(cmd[1])
            if not location_title:
                return "You can't go there you dummy"
            self.location = World.get_location_by_title(location_title)
            return self.location.print()

        raise NotImplemented
