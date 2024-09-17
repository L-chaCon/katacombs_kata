from .world import Location, world


class Game():
    location: Location

    def __init__(self):
        self.location = world[0]

    def print(self) -> str:
        return self.location.print()

    def run_command(self, command: str) -> str:
        cmd = command.split(" ")
        if cmd[0] == "LOOK":
            exit = self.location.exits.get(cmd[1])
            if exit:
                return f"I can see an exit: {exit}"
            else:
                return "Nothing interesting to look at there!"

        if cmd[0] == "GO":
            exit = self.location.exits.get(cmd[1])
            if not exit:
                return "You can't go there you dummy"
            self.location = get_location_by_title(exit)
            return self.location.print()
        
        raise NotImplemented
            

def get_location_by_title(location_title: str) -> Location:
    for location in world:
        if location.title == location_title:
            return location
    raise ValueError("there is no location")
