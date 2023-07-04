# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Amsterdam."""

import asyncio

from odp_amsterdam import Garage, ODPAmsterdam


async def main() -> None:
    """Show example on using the ODP Amsterdam API client."""
    async with ODPAmsterdam() as client:
        garages = await client.all_garages()
        single_garage: Garage = await client.garage(
            garage_id="99b77fc5-a237-4ba0-abe4-b9a3886aa471",
        )

        print(f"Single garage: {single_garage}")
        print()

        count: int = len(garages)
        for item in garages:
            print(item)

        # Count unique id's in disabled_parkings
        unique_values: list[str] = list({garage.garage_id for garage in garages})

        print("__________________________")
        print(f"Total garages found: {count}")
        print(f"Unique ID values: {len(unique_values)}")


if __name__ == "__main__":
    asyncio.run(main())
