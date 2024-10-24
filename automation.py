from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration
url = 'https://www.270towin.com/2024-simulation/'
sim_speed_id = 'sim_speed_4'
run_simulation = 'run-simulation'
results_harris = 'dem_ev'
results_trump = 'rep_ev'
wins_harris = 0
wins_trump = 0
wins_tied = 0
wait_time = 6
simulation_count = 100

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Open the website
    driver.get(url)

    # Set Simluation Speed
    sim_speed_id_btn = driver.find_element(By.ID, sim_speed_id)
    sim_speed_id_btn.click()

    # Find the "Run Simluation" button
    run_simulation_btn = driver.find_element(By.ID, run_simulation)

    # Run the Simluation a specified number of times
    for i in range(simulation_count):

        # Click the "Run Simluation" Button
        run_simulation_btn.click()

        # Wait for the Simulation to Complete (for Speed 4, this is about 6 seconds)
        time.sleep(wait_time)

        # Recording the final Values
        results_harris_value = driver.find_element(By.ID, results_harris).text
        results_trump_value = driver.find_element(By.ID, results_trump).text

        # Convert Results to Numbers
        try:
            results_harris_value = int(results_harris_value.replace('',''))
            results_trump_value = int(results_trump_value.replace('',''))
        except ValueError:
            print(f"Count not convert values to numbers: '{results_harris_value}', '{results_trump_value}'")
            continue

        # Update the Win Record
        if results_harris_value > results_trump_value:
            wins_harris += 1
        elif results_harris_value < results_trump_value:
            wins_trump += 1
        else:
            wins_tied += 1

        # Calculate the Win Percentage
        total_runs = wins_harris + wins_trump + wins_tied
        wins_harris_percentage = (wins_harris / total_runs) * 100 if total_runs > 0 else 0
        wins_trump_percentage = (wins_trump / total_runs) * 100 if total_runs > 0 else 0
        wins_tied_percentage = (wins_tied / total_runs) * 100 if total_runs > 0 else 0

        # Print the Results, Update Win Record
        if results_harris_value > results_trump_value:
            print("-" * 80)
            print(f"Simluation {i + 1}: Harris Wins.")
            print("-" * 10)
            print(f"Harris: {results_harris_value}, Trump: {results_trump_value}")
            print(f"Harris has won {wins_harris_percentage:.2f}% of simulations. ({wins_harris} out of {total_runs})")
        elif results_harris_value < results_trump_value:
            print("-" * 80)
            print(f"Simluation {i + 1}: Trump Wins.")
            print("-" * 10)
            print(f"Harris: {results_harris_value}, Trump: {results_trump_value}")
            print(f"Trump has won {wins_trump_percentage:.2f}% of simulations. ({wins_trump} out of {total_runs})")
        else:
            print("-" * 80)
            print(f"Simluation {i + 1}: Harris and Trump have Tied.")
            print("-" * 10)
            print(f"Harris: {results_harris_value}, Trump: {results_trump_value}")
            print(f"{wins_trump_percentage:.2f}% of Simulations ({wins_tied} of {total_runs}) have resulted in a Tie.")

    # Keep the browser open after the script finishes
    print(f"{i + 1} Simluations have been completed.")

except Exception as e:
    print(f"An error occurred: {e}")

# Commented out to keep the browser open
# finally:
#     driver.quit()