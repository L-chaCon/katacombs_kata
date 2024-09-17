from dataclasses import dataclass
from typing import Literal

Direction = Literal["N", "E", "S", "W", "UP", "DOWN"]


@dataclass
class Location:
    title: str
    description: str
    exits: dict[Direction, str]
    items: dict[Direction, str]
    # objects: list[str]

    def print(self) -> str:
        return f"{self.title}\n\n{self.description}"

    def take_item(self, direction: Direction, item_name) -> bool:
        if direction in self.items:
            item = self.items[direction]
            if item == item_name:
                del self.items[direction]
                return True
        return False

    def drop_item(self, direction: Direction, item_name) -> bool:
        if direction in self.items:
            return False
        self.items[direction] = item_name
        return True


class World:
    locations: list[Location]

    def __init__(self):
        self.locations = [
            Location(
                title="Cryosleep Chamber",
                description="The metallic chamber is dimly lit, with frost covering the glass of several cryopods. Some are occupied, others flicker with an eerie red light. A control panel by the wall is flashing, signalling a malfunction. An airlock door to the south hums quietly, waiting to be opened.",
                exits={"S": "Abandoned Research Lab"},
                items={"E": "Cryopod Keycard", "W": "Emergency Toolkit"},
            ),
            Location(
                title="Abandoned Research Lab",
                description="Shattered glass tubes and overturned workstations suggest something went wrong here. A strange humming sound emits from a broken containment unit in the corner. A data pad lies on a table, its screen cracked but still operational. You can see a hatch leading upwards through the ceiling, and a bulkhead door to the east. The airlock to the north leads back to the Cryosleep Chamber.",
                exits={"N": "Cryosleep Chamber"},
                items={},
            ),
        ]

    def get_location_by_title(self, location_title: str) -> Location:
        for location in self.locations:
            if location.title == location_title:
                return location
        raise ValueError("there is no location with that title")
