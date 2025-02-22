{% extends "abbreviations.txt" %}
{% block cc %}
"""
Seeder module for the {{ db }} database.
{#
The sql seeder module. If 'postgres' or 'mysql' is selected,
this will be moved to  `src/flask/flaskapp/seeder.py`.
#}
"""
import json

from . import models

def seed_data(db, filename:str) -> None:
    """Uses the JSON file to populate the database"""
    with open(filename) as f:
        data = json.load(f)
        session = db.session

        for entry in data:
            if entry["model"] == "relecloud.destination":
                destination = session.get(models.Destination, entry["pk"])

                if destination is None:
                    destination = models.Destination(
                       name=entry["fields"]["name"],
                        id=entry["pk"],
                        description=entry["fields"]["description"],
                    )
                    session.add(destination)
                    session.commit()
                    session.refresh(destination)
            if entry["model"] == "relecloud.cruise":
                cruise = session.get(models.Cruise, entry["pk"])
                if cruise is None:
                    destinations = []

                    for destination_id in entry["fields"]["destinations"]:
                        destination = session.get(models.Destination, destination_id)
                        if destination is None:
                            raise Exception(f"Destination with id {destination_id} not found")
                        destinations.append(destination)

                    cruise = models.Cruise(
                        name=entry["fields"]["name"],
                        id=entry["pk"],
                        description=entry["fields"]["description"],
                        destinations=destinations,
                    )
                    session.add(cruise)
                    session.commit()
                    session.refresh(cruise)

{% endblock %}