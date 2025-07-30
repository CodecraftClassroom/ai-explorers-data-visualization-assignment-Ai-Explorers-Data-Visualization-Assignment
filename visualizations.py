import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_fifa_data(file_path):
    return pd.read_csv(file_path)

def plot_fifa_data(fifa_data):
    plt.figure(figsize=(16, 6))
    sns.lineplot(data=fifa_data)
    plt.title("ARG FIFA Data")
    sns.lineplot(data=fifa_data['ARG'])
    plt.savefig("fifa_plot.png")
    plt.close()

def load_flight_data(file_path):
    return pd.read_csv(file_path)

def plot_flight_data(flight_data):
    plt.figure(figsize=(10, 6))
    plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
    plt.ylabel("Arrival delay (in minutes)")
    sns.barplot(x=flight_data['Month'], y=flight_data['NK'])
    plt.savefig("spirit_airlines_plot.png")
    plt.close()

    plt.figure(figsize=(14, 7))
    plt.title("Average Arrival Delay for Each Airline, by Month")
    plt.xlabel("Airline")
    sns.heatmap(data=flight_data, annot=True)
    plt.savefig("airline_heatmap.png")
    plt.close()
