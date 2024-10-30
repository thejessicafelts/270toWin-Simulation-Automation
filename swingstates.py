# swingstates.py

from selenium.webdriver.common.by import By

# Swing states and their corresponding HTML element IDs
swing_state_ids = {
    "az": "04",
    "ga": "13",
    "mi": "26",
    "nv": "32",
    "nc": "37",
    "pa": "42",
    "wi": "55"
}

def get_swing_state_results(driver):
    """
    Determines the winner of each swing state based on the fill color of each state's SVG.

    Parameters:
        driver (WebDriver): Selenium WebDriver instance.

    Returns:
        dict: A dictionary with each swing state and its winner ("democrat" or "republican").
    """
    swing_state_results = {}

    for state, state_id in swing_state_ids.items():
        state_element = driver.find_element(By.ID, state_id)
        fill_color = state_element.value_of_css_property("fill")

        # Determine winner based on fill color (adjust colors as needed)
        if fill_color == "rgb(36, 73, 153)":  # Blue color for Democrat
            swing_state_results[state] = "democrat"
        elif fill_color == "rgb(210, 37, 50)":  # Red color for Republican
            swing_state_results[state] = "republican"
        else:
            swing_state_results[state] = "undecided"  # For any other color

    return swing_state_results
