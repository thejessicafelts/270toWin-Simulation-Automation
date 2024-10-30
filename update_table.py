# update-table.py

from datetime import datetime

def update_html_table(html_file_path, simulation_count, wins_democrat, wins_republican, wins_tied):

    # Calculate Total Number of Simulations
    total_simulations = wins_democrat + wins_republican + wins_tied
    
    # Calculate win percentages
    total_simulations = wins_democrat + wins_republican + wins_tied
    wins_democrat_percentage = (wins_democrat / total_simulations) * 100 if total_simulations else 0
    wins_republican_percentage = (wins_republican / total_simulations) * 100 if total_simulations else 0
    wins_tied_percentage = (wins_tied / total_simulations) * 100 if total_simulations else 0

    # Determine overall winner row class
    if wins_democrat > wins_republican:
        row_class = "dem-win"
        dem_win_row_class = "dem-win"
        rep_win_row_class = ""
        tie_win_row_class = ""
    elif wins_republican > wins_democrat:
        row_class = "rep-win"
        dem_win_row_class = ""
        rep_win_row_class = "rep-win"
        tie_win_row_class = ""
    else:
        row_class = "tie-win"
        dem_win_row_class = ""
        rep_win_row_class = ""
        tie_win_row_class = "tie-win"

    # Create a new row with the current date and time
    current_date = datetime.now().strftime('%B %d, %Y')
    current_time = datetime.now().strftime('%H:%M')
    new_row = f"""
                <tr class="{row_class}">
                    <td class="left">{current_date} &mdash; {current_time} EDT</td>
                    <td class="center">{simulation_count}</td>
                    <td class="center {dem_win_row_class}">{wins_democrat}</td>
                    <td class="center {dem_win_row_class}">{wins_democrat_percentage:.1f}%</td>
                    <td class="center {rep_win_row_class}">{wins_republican}</td>
                    <td class="center {rep_win_row_class}">{wins_republican_percentage:.1f}%</td>
                    <td class="center {tie_win_row_class}">{wins_tied}</td>
                    <td class="center {tie_win_row_class}">{wins_tied_percentage:.1f}%</td>
                </tr>
                """
    # Insert new row into the HTML file
    with open(html_file_path, 'r') as file:
        html_content = file.readlines()

    # Insert the new row at the top of the table body
    for index, line in enumerate(html_content):
        if '<tbody id="simulation-results">' in line:
            html_content.insert(index + 1, new_row)
            break

    # Write the updated HTML content back to the file
    with open(html_file_path, 'w') as file:
        file.writelines(html_content)

    print("HTML file has been updated successfully.")