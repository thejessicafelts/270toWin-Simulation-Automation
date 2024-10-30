# update_csv.py

import csv
from swingstates import get_swing_state_results
import os

def get_latest_set_number(csv_file_path):
    """
    Returns the latest set number from the swingstates.csv file or 1 if the file is empty or doesn't exist.
    """
    if not os.path.exists(csv_file_path):
        return 1
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        sets = [int(row[0]) for row in reader if row and row[0].isdigit()]
    return max(sets, default=0) + 1

def update_swingstates_csv(csv_file_path, driver, current_set, sim_number, overall_winner):
    """
    Updates the CSV file with the swing state results for each simulation.

    Parameters:
        csv_file_path (str): Path to the swingstates.csv file.
        driver (WebDriver): Selenium WebDriver instance.
        current_set (int): The current simulation set number.
        sim_number (int): The individual simulation number within the set.
        overall_winner (str): "democrat" or "republican" for the overall winner.
    """
    # Get swing state results from the driver
    swing_state_results = get_swing_state_results(driver)

    # Prepare row data for CSV
    row_data = {
        "set": current_set,
        "sim": sim_number,
        "winner": overall_winner,
        "az": swing_state_results.get("az", "undecided"),
        "ga": swing_state_results.get("ga", "undecided"),
        "mi": swing_state_results.get("mi", "undecided"),
        "nv": swing_state_results.get("nv", "undecided"),
        "nc": swing_state_results.get("nc", "undecided"),
        "pa": swing_state_results.get("pa", "undecided"),
        "wi": swing_state_results.get("wi", "undecided")
    }

    # Read existing data if the file exists
    header = ["set", "sim", "winner", "az", "ga", "mi", "nv", "nc", "pa", "wi"]
    existing_data = []

    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            existing_data = list(reader)
            # Ensure header is in place
            if existing_data and existing_data[0] != header:
                existing_data.insert(0, header)
    
    # Add blank line only if there's a change in the set number
    if existing_data and existing_data[-1][0] != str(current_set):
        existing_data.insert(1, [])  # Insert blank line between sets

    # Add new row data at the top of the file, after the header
    new_row = [row_data[key] for key in header]
    existing_data.insert(1, new_row)

    # Write the updated data back to the CSV
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in existing_data:
            writer.writerow(row)
