from .world import Direction, Location, World


class Game:
    location: Location
    bag: list[str]
    direction: Direction

    def __init__(self):
        self.world = World()
        self.location = self.world.locations[0]
        self.look_direction = "N"
        self.bag = []

    def print(self) -> str:
        return self.location.print()

    def run_command(self, command: str) -> str:
        cmd = command.split(" ", maxsplit=1)
        if cmd[0] == "LOOK":
            self.look_direction = cmd[1]
            location_title = self.location.exits.get(cmd[1])
            if location_title:
                return f"I can see an exit: {location_title}"
            else:
                return "Nothing interesting to look at there!"

        if cmd[0] == "GO":
            location_title = self.location.exits.get(cmd[1])
            if not location_title:
                return "You can't go there you dummy"
            self.location = self.world.get_location_by_title(location_title)
            return self.location.print()

        if cmd[0] == "TAKE":
            item = self.location.take_item(self.look_direction, cmd[1])
            if item:
                self.bag.append(item)
                return "Picked up: {}".format(item)
            else:
                return "That item isn't here."

        if cmd[0] == "BAG":
            return "The bag contains: {}".format(", ".join(self.bag))

        if cmd[0] == "DROP":
            if cmd[1] not in self.bag:
                return "Cannot drop {}, it's not in your bag".format(cmd[1])

            if self.location.drop_item(self.look_direction, cmd[1]):
                self.bag.remove(cmd[1])
                return "Dropped item: {}".format(cmd[1])
            else:
                return "Cannot drop item, another item is here"

        raise NotImplemented
