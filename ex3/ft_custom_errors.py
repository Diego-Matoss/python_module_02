#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water Error") -> None:
        super().__init__(message)


def plant_error(name: str) -> None:
    raise PlantError(f"The {name.lower()} plant is wilting!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_error("Tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


if __name__ == "__main__":
    main()
