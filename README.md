# 270toWin Election Simulation Automation

This Python script automates running simulations on the [270toWin 2024 Election Simulation](https://www.270towin.com/2024-simulation/) website. It sets the simulation speed, runs the simulation a specified number of times, and tracks the results for each run. Throughout the process, it prints out information on which candidate won each simulation.

## Features
- Automatically set the simulation speed on the 270toWin website.
- Run the simulation a specified number of times.
- Track how many times each candidate wins or ties during the simulation.
- Print results for each simulation run, including which candidate won and the running percentage of wins.

## Prerequisites
Before running the script, make sure you have the following installed:

- **Python 3.7 or higher**: You can download it from [python.org](https://www.python.org/downloads/).
- **Google Chrome**: The script uses the Chrome browser to run the automation.
- **ChromeDriver**: Managed automatically by `webdriver-manager`.
- **Selenium**: To install Selenium, run:
  ```bash
  pip install selenium webdriver-manager
  ```

## Setup Instructions

### Step 1: Clone the Repository
To download this script, clone the repository using:
```bash
git clone https://github.com/thejessicafelts/270towin-simulation-automation.git
cd 270towin-simulation-automation
```

### Step 2: Install Required Packages
Make sure you have `selenium` and `webdriver-manager` installed:
```bash
pip install selenium webdriver-manager
```

### Step 3: Preventing Your Computer from Sleeping During the Simulation
- **For Mac Users**: Use the `caffeinate` command to prevent your Mac from going to sleep while the script runs:
  ```bash
  caffeinate -i python3 script_name.py
  ```
  Replace `script_name.py` with the actual name of your Python script. The `-i` option ensures your Mac stays awake as long as the script is running.

- **For Windows Users**: Adjust your power settings to prevent the computer from sleeping:
  1. Go to **Settings > System > Power & Sleep**.
  2. Under **Sleep**, set **"When plugged in, PC goes to sleep after"** to **"Never."**
  3. Alternatively, you can use third-party tools to keep your system awake, such as `Caffeine.exe` or `NoSleep.exe`.

## Running the Script

### Step 1: Modify Configuration (Optional)
Edit the following variables in the script if you need to adjust the settings:
- **`url`**: The URL of the 270toWin simulation page (default is set correctly).
- **`sim_speed_id`**: The ID for the simulation speed button (default: `sim_speed_4`).
- **`simulation_count`**: Number of times to run the simulation (default: `1000`).
- **`wait_time`**: Time to wait (in seconds) between simulations (default: `6`).

### Step 2: Run the Script
Execute the script using:
- **Mac**:
  ```bash
  caffeinate -i python3 script_name.py
  ```
- **Windows**:
  ```bash
  python script_name.py
  ```

### Example Output
```plaintext
--------------------------------------------------------------------------------
Simulation 1: Harris Wins.
----------
Harris: 320, Trump: 218
Harris has won 100.00% of simulations. (1 out of 1)
--------------------------------------------------------------------------------
Simulation 2: Trump Wins.
----------
Harris: 249, Trump: 289
Trump has won 50.00% of simulations. (1 out of 2)
--------------------------------------------------------------------------------
Simulation 3: Harris and Trump have Tied.
----------
Harris: 269, Trump: 269
50.00% of Simulations (1 of 3) have resulted in a Tie.
--------------------------------------------------------------------------------
```

## Code Walkthrough

1. **Initialization**:
   - The script sets up the WebDriver using ChromeDriver and `webdriver-manager`.
   - The simulation speed is set by finding and clicking the appropriate button on the website.

2. **Simulation Loop**:
   - The script runs the simulation the specified number of times.
   - After each simulation run, it waits for the results to appear and retrieves them using the designated HTML element IDs.
   - The results are converted to integers, and the script tracks how many times each candidate wins or if there's a tie.

3. **Result Calculation & Display**:
   - The script calculates and prints the win percentage for Harris and Trump, as well as the number of ties, after each simulation run.

## Future Enhancements

- **Final Summary**: Add a final summary that prints the overall win percentages for Harris, Trump, and ties at the end of all simulations.
- **Robust Error Handling**: Implement more error handling to gracefully handle issues, such as network interruptions or missing elements on the page.
- **Command-Line Arguments**: Allow users to specify `simulation_count`, `wait_time`, and other configurations via command-line arguments for easier usage.

## Troubleshooting

- **ChromeDriver Issues**:
  - Ensure that your Chrome browser is up to date. `webdriver-manager` should handle most ChromeDriver version issues, but sometimes mismatches can occur. Updating Chrome typically resolves these.

- **Permissions Errors**:
  - If you encounter permissions issues when running the script on Windows, try running the command prompt as an Administrator.

- **System Goes to Sleep**:
  - Make sure to use the `caffeinate` command on Mac or adjust the power settings on Windows as described above.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to improving the script. Make sure to follow proper coding standards and provide thorough explanations for any changes made.
