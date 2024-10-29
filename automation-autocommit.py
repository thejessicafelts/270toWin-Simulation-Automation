from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import git  # You may need to install GitPython with: pip install gitpython

# Configuration
url = 'https://www.270towin.com/2024-simulation/'
sim_speed_id = 'sim_speed_4'
run_simulation = 'run-simulation'
results_harris = 'dem_ev'
results_trump = 'rep_ev'
wins_harris = 0
wins_trump = 0
wins_tied = 0
wait_time = 7
simulation_count = 10
html_file_path = 'index.html'  # Path to your HTML file

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Open the website
    driver.get(url)

    # Set Simulation Speed
    sim_speed_id_btn = driver.find_element(By.ID, sim_speed_id)
    sim_speed_id_btn.click()

    # Find the "Run Simulation" button
    run_simulation_btn = driver.find_element(By.ID, run_simulation)

    # Run the Simulation a specified number of times
    for i in range(simulation_count):
        run_simulation_btn.click()
        time.sleep(wait_time)  # Wait for the Simulation to Complete

        # Recording the final Values
        results_harris_value = driver.find_element(By.ID, results_harris).text
        results_trump_value = driver.find_element(By.ID, results_trump).text

        # Convert Results to Numbers
        try:
            results_harris_value = int(results_harris_value.replace('', ''))
            results_trump_value = int(results_trump_value.replace('', ''))
        except ValueError:
            print(f"Could not convert values to numbers: '{results_harris_value}', '{results_trump_value}'")
            continue

        # Update the Win Record
        if results_harris_value > results_trump_value:
            wins_harris += 1
        elif results_harris_value < results_trump_value:
            wins_trump += 1
        else:
            wins_tied += 1

    # Summary Information
    total_runs = wins_harris + wins_trump + wins_tied
    wins_harris_percentage = (wins_harris / total_runs) * 100 if total_runs > 0 else 0
    wins_trump_percentage = (wins_trump / total_runs) * 100 if total_runs > 0 else 0
    wins_tied_percentage = (wins_tied / total_runs) * 100 if total_runs > 0 else 0

    # Determine Overall Winner
    overall_winner = "Harris" if wins_harris > wins_trump else "Trump" if wins_trump > wins_harris else "Tie"

    # Determine Overall Winner and Row Class
    if wins_harris > wins_trump:
        overall_winner = "Harris"
        row_class = "dem-win"
        dem_win_row_class = "dem-win"
        rep_win_row_class = ""
        tie_win_row_class = ""
    elif wins_trump > wins_harris:
        overall_winner = "Trump"
        row_class = "rep-win"
        dem_win_row_class = ""
        rep_win_row_class = "rep-win"
        tie_win_row_class = ""
    elif wins_harris == wins_harris:
        overall_winner = "Candidates have Tied"
        row_class = "dem-rep-tie"
        dem_win_row_class = "dem-rep-tie"
        rep_win_row_class = "dem-rep-tie"
        tie_win_row_class = ""
    else:
        overall_winner = "Tie"
        dem_win_row_class = ""
        rep_win_row_class = ""
        tie_win_row_class = "tie-win"

    # Format the data
    today = datetime.now().strftime('%B %d, %Y')
    new_row = f"""
            <tr class="{row_class}">
                <td class="left">{today}</td>
                <td class="center">{simulation_count}</td>
                <td class="center {dem_win_row_class}">{wins_harris}</td>
                <td class="center {dem_win_row_class}">{wins_harris_percentage:.1f}%</td>
                <td class="center {rep_win_row_class}">{wins_trump}</td>
                <td class="center {rep_win_row_class}">{wins_trump_percentage:.1f}%</td>
                <td class="center {tie_win_row_class}">{wins_tied}</td>
                <td class="center {tie_win_row_class}">{wins_tied_percentage:.1f}%</td>
            </tr>
    """

    # Append the new row as the first row in the HTML file
    with open(html_file_path, 'r') as file:
        html_content = file.readlines()

    # Find the start of the table body in the HTML file and insert the new row right after it
    for index, line in enumerate(html_content):
        if '<tbody id="simulation-results">' in line:
            # Insert the new row immediately after the <tbody> tag
            html_content.insert(index + 1, new_row)
            break

    # Write the modified HTML content back to the file
    with open(html_file_path, 'w') as file:
        file.writelines(html_content)


    # Automatically commit the change
    # repo = git.Repo('.')
    # repo.git.add(html_file_path)
    # repo.git.commit(m=f"Add simulation results for {today}")

    # print("HTML file updated and changes committed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

# finally:
#     driver.quit()
