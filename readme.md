## Assignment Details

This assignment will have you visualize and interpret data from a CSV file.

## Assignment Steps

1. Create a python file named main.py. This will be the only file you use for this assignment.
2. Import pandas, matplotlib.pyplot, and seaborn.
3. Define a function named **load_data(file_path)** that reads a CSV file and returns a **DataFrame** using pd.read_csv(file_path).
4. Create a function **plot_fifa_data(fifa_data)** that:
    1. Uses sns.lineplot(data=fifa_data) but only plots the ARG data.
    2. Sets the figure size and a title using plt.figure() and plt.title().
    3. Saves the plot using plt.savefig("fifa_plot.png"). Make sure **"fifa_plot.png"** is the name you use and that it is spelled correctly.
    4. Closes the plot with plt.close().
    5. Has no return statement.
5. Define a new function **plot_flight_data(flight_data)** that:
    1. Creates a barplot using sns.barplot(x=flight_data["Month"], y=flight_data["NK"]).
    2. Save the name of the barplot as "spirit_airlines_plot.png"
    3. Adds a title and y-axis label with plt.title() and plt.ylabel().
    4. Create a 2nd figure using plt.figure() this one is a heatmap.
    5. Name this one "airline_heatmap.png".
    6. Use sns.heatmap(data=flight_data, annot=True) to show the data.
    7. Add axis labels and a title.
    8. Save both plots using plt.savefig() and close them with plt.close().

### Downloading Modules for Importing

If you are having trouble importing the correct modules, make sure they are downloaded into your codespace. In your terminal, type the following:

pip install pandas matplotlib seaborn