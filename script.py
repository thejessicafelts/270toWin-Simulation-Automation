from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Updating HTML Table
from update_table import update_html_table

# Import update_csv and get_latest_set_number
from update_csv import update_swingstates_csv, get_latest_set_number

# Auto Commit
from autocommit import auto_commit_and_push

# Import data visualization module functions
import data_visualization
from data_visualization import update_index_with_charts

# Define or retrieve the current set
output_file_path = "swingstates.csv"
current_set = get_latest_set_number(output_file_path)

# Configuration
url = 'https://www.270towin.com/2024-simulation/'
sim_speed_id = 'sim_speed_4'
run_simulation = 'run-simulation'
results_democrat = 'dem_ev'
results_republican = 'rep_ev'
wins_democrat = 0
wins_republican = 0
wins_tied = 0
wait_time = 10
simulation_count = 10

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
    
        # Click the "Run Simulation" Button
        run_simulation_btn.click()

        # Wait for the Simulation to Complete (for Speed 4, this is about 6 seconds)
        time.sleep(wait_time)

        # Extract and process results
        results_democrat_value = driver.find_element(By.ID, results_democrat).text
        results_republican_value = driver.find_element(By.ID, results_republican).text

        try:
            # Convert the extracted text to integers
            results_democrat_value = int(results_democrat_value)
            results_republican_value = int(results_republican_value)
        except ValueError:
            print(f"Could not convert values to numbers: '{results_democrat_value}', '{results_republican_value}'")
            continue

        # Update the Win Record
        if results_democrat_value > results_republican_value:
            wins_democrat += 1
        elif results_democrat_value < results_republican_value:
            wins_republican += 1
        else:
            wins_tied += 1

        # Calculate the Win Percentage
        total_runs = wins_democrat + wins_republican + wins_tied
        wins_democrat_percentage = (wins_democrat / total_runs) * 100 if total_runs > 0 else 0
        wins_republican_percentage = (wins_republican / total_runs) * 100 if total_runs > 0 else 0
        wins_tied_percentage = (wins_tied / total_runs) * 100 if total_runs > 0 else 0

        # Print the Results, Update Win Record
        if results_democrat_value > results_republican_value:
            print("-" * 80)
            print(f"Simulation {i + 1}: Democrats Win.")
            print("-" * 10)
            print(f"Democrat: {results_democrat_value}, Republican: {results_republican_value}")
            print(f"Democrats have won {wins_democrat_percentage:.2f}% of simulations. ({wins_democrat} out of {total_runs})")
        elif results_democrat_value < results_republican_value:
            print("-" * 80)
            print(f"Simulation {i + 1}: Republicans Win.")
            print("-" * 10)
            print(f"Democrats: {results_democrat_value}, Republicans: {results_republican_value}")
            print(f"Republicans have won {wins_republican_percentage:.2f}% of simulations. ({wins_republican} out of {total_runs})")
        else:
            print("-" * 80)
            print(f"Simulation {i + 1}: Democrats and Republicans have Tied.")
            print("-" * 10)
            print(f"Democrats: {results_democrat_value}, Republicans: {results_republican_value}")
            print(f"{wins_republican_percentage:.2f}% of Simulations ({wins_tied} of {total_runs}) have resulted in a Tie.")

        # After determining the overall winner for the simulation
        overall_winner = "democrat" if results_democrat_value > results_republican_value else \
                         "republican" if results_republican_value > results_democrat_value else "tie"
        
        # Ensure current_set and other necessary parameters are defined
        update_swingstates_csv(
            csv_file_path='swingstates.csv',
            driver=driver,
            current_set=current_set,
            sim_number=i + 1,
            overall_winner=overall_winner
        )

    # After the simulation loop
    update_html_table(
        html_file_path='index.html',
        simulation_count=simulation_count,
        wins_democrat=wins_democrat,
        wins_republican=wins_republican,
        wins_tied=wins_tied
    )

    # Auto-commit and push the updated files
    auto_commit_and_push(
        repo_path='.',  # Assumes script is in the repo directory
        files_to_commit=['index.html', 'swingstates.csv']
    )

    # Run data visualization to update results.html
    print("Generating visualizations...")
    data_visualization.save_overall_pie_chart()
    data_visualization.save_state_pie_charts()
    data_visualization.update_index_with_charts()

    print("Visualizations updated and saved to results.html.")

    # Update index.html with the charts
    data_visualization.update_index_with_charts()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
