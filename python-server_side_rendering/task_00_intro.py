#!/usr/bin/python3
"""Creating a Simple Templating Program module"""
import logging

logging.basicConfig(level=logging.ERROR)

def generate_invitations(template, attendees):
    """Function that generates personalized invitations from a template with placeholders and a list of objects"""
    if not isinstance(template, str):
        logging.error("Invalid input: template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees is not a list of dictionaries.")
        return
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(output)
        except Exception as e:
            logging.error(f"Error writing to file {filename}: {e}")
