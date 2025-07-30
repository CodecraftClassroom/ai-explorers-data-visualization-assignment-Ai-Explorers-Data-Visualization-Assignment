## Assignment Details

This assignment will have you visualize and interpret data from a CSV file.

## Assignment Steps

1. Create a python file named main.py. This will be the only file you use for this assignment.
2. Import pandas, matplotlib.pyplot, and seaborn.
3. Define a function named load_data(file_path) that reads a CSV file and returns the loaded DataFrame using pd.read_csv(file_path).
4. Create a function plot_fifa_data(fifa_data) that:
    1. Uses sns.lineplot(data=fifa_data) to plot the whole dataset.
    2. Sets the figure size and a title using plt.figure() and plt.title().
    3. Saves the plot using plt.savefig("fifa_plot.png").
    4. Closes the plot with plt.close().
5. Plot Lineplot for Only "ARG" Data.
6. Define a new function plot_flight_data(flight_data) that:
    1. Creates a barplot using sns.barplot(x=flight_data["Month"], y=flight_data["NK"]).
    2. Adds a title and y-axis label with plt.title() and plt.ylabel().
    3. Create a new figure using plt.figure().
    4. Use sns.heatmap(data=flight_data, annot=True) to show the data.
    5. Add axis labels and a title.
    6. Save both plots using plt.savefig() and close them with plt.close().

### Downloading Modules for Importing

If you are having trouble importing the correct modules, make sure they are downloaded into your codespace. In your terminal, type the following:

pip install pandas matplotlib seaborn