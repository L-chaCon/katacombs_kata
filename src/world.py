from dataclasses import dataclass

@dataclass
class Location:
    title: str
    description: str
    # items: list[str]
    # objects: list[str]
    exits: dict[str, str]

    def print(self) -> str:
        return f"{self.title}\n\n{self.description}"


class World:
    locations: list[Location] = [
        Location(
            title="Cryosleep Chamber",
            description="The metallic chamber is dimly lit, with frost covering the glass of several cryopods. Some are occupied, others flicker with an eerie red light. A control panel by the wall is flashing, signalling a malfunction. An airlock door to the south hums quietly, waiting to be opened.",
            exits={"S": "Abandoned Research Lab"},
        ),
        Location(
            title="Abandoned Research Lab",
            description="Shattered glass tubes and overturned workstations suggest something went wrong here. A strange humming sound emits from a broken containment unit in the corner. A data pad lies on a table, its screen cracked but still operational. You can see a hatch leading upwards through the ceiling, and a bulkhead door to the east. The airlock to the north leads back to the Cryosleep Chamber.",
            exits={"N": "Cryosleep Chamber"},
        )
    ]

    @classmethod
    def get_location_by_title(cls, location_title: str) -> Location:
        for location in cls.locations:
            if location.title == location_title:
                return location
        raise ValueError("there is no location with that title")
