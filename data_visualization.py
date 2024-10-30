import os
import pandas as pd
import matplotlib.pyplot as plt

# Define consistent colors
COLORS = {
    "democrat": "#244999",
    "republican": "#d22532",
    "tie": "#ffde21"
}

# Directory for saving charts
IMAGE_DIR = "data_visualization"
os.makedirs(IMAGE_DIR, exist_ok=True)  # Create the directory if it doesn't exist

# Configure global font properties for autopct
plt.rcParams.update({
    'font.size': 20,
    'font.weight': 'bold'
})

def save_overall_pie_chart():
    data = pd.read_csv('swingstates.csv')
    results = data['winner'].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot pie chart without labels, keeping only percentages
    results.plot.pie(
        ax=ax,
        autopct='%1.1f%%',
        labels=None,
        colors=[COLORS.get(label, "#444444") for label in results.index],
        startangle=90,
        textprops={'color': "#f4f4f4", 'fontsize': 20, 'weight': 'bold'}
    )

    ax.set_title("National Results", color="#333333", fontsize=24, weight='bold')
    ax.set_ylabel('')

    ax.legend(
        title="Party",
        labels=[f"{label.capitalize()}" for label in results.index],
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=16,
        title_fontsize=16,
        prop={"weight": "regular", "size": 16}
    )

    plt.savefig(os.path.join(IMAGE_DIR, 'national_pie_chart.png'), bbox_inches='tight')
    plt.close()

def save_state_pie_charts():
    data = pd.read_csv('swingstates.csv')
    states = ["az", "ga", "mi", "nv", "nc", "pa", "wi"]

    for state in states:
        state_results = data[state].value_counts()

        fig, ax = plt.subplots(figsize=(10, 6))

        state_results.plot.pie(
            ax=ax,
            autopct='%1.1f%%',
            labels=None,
            colors=[COLORS.get(label, "#444444") for label in state_results.index],
            startangle=90,
            textprops={'color': "#f4f4f4", 'fontsize': 20, 'weight': 'bold'}
        )

        ax.set_title(f"{state.upper()} Results", color="#333333", fontsize=24, weight='bold')
        ax.set_ylabel('')

        ax.legend(
            title="Party",
            labels=[f"{label.capitalize()}" for label in state_results.index],
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            fontsize=16,
            title_fontsize=16,
            prop={"weight": "regular", "size": 16}
        )

        plt.savefig(os.path.join(IMAGE_DIR, f'{state}_pie_chart.png'), bbox_inches='tight')
        plt.close()

def update_index_with_charts():
    """
    Inserts the national chart into <section id="national-graph"></section>
    and the state charts into <section id="state-graphs"></section> in index.html.
    """
    charts_folder = "data_visualization"
    chart_files = sorted(
        [f for f in os.listdir(charts_folder) if f.endswith(".png")]
    )

    # Prepare HTML for National and State charts separately
    national_chart_html = ""
    state_charts_html = ""

    for chart_file in chart_files:
        if "national" in chart_file:
            national_chart_html = f'<div class="chart"><img src="{charts_folder}/{chart_file}" alt="{chart_file}"></div>\n'
        else:
            state_charts_html += f'<div class="chart"><img src="{charts_folder}/{chart_file}" alt="{chart_file}"></div>\n'

    # Read index.html content
    with open("index.html", "r") as file:
        html_content = file.read()

    # Replace sections in index.html with new chart HTML
    updated_html = html_content.replace(
        '<section id="national-graph"></section>',
        f'<section id="national-graph">\n{national_chart_html}\n</section>'
    ).replace(
        '<section id="state-graphs"></section>',
        f'<section id="state-graphs">\n{state_charts_html}\n</section>'
    )

    # Write the updated HTML back to index.html
    with open("index.html", "w") as file:
        file.write(updated_html)

    print("index.html updated with the latest charts in <section id='national-graph'> and <section id='state-graphs'>.")
