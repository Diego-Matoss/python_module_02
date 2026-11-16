#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    plants_ok = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plants_ok)

    print("\nTesting invalid plants...")
    plants_exception = ["Tomato", "lettuce", "carrots"]
    test_watering_system(plants_exception)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
