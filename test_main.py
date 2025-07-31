import unittest
import os
import pandas as pd
from main import load_data, plot_fifa_data, plot_flight_data

class TestDataVisualizationAssignment(unittest.TestCase):

    def setUp(self):
        self.fifa_file = 'data/fifa.csv'
        self.flight_file = 'data/flight.csv'

        self.assertTrue(os.path.exists(self.fifa_file))
        self.assertTrue(os.path.exists(self.flight_file))

    # Testing to make sure functions return proper dataframes.
    def test_load_fifa_data(self):
        data = load_data(self.fifa_file)
        self.assertIsInstance(data, pd.DataFrame)

    def test_load_flight_data(self):
        data = load_data(self.flight_file)
        self.assertIsInstance(data, pd.DataFrame)

    # Testing to make sure all three graph pngs are made.
    def test_plot_fifa_data(self):
        data = load_data(self.fifa_file)
        plot_fifa_data(data)
        self.assertTrue(os.path.exists("fifa_plot.png"))

    def test_plot_flight_data(self):
        data = load_data(self.flight_file)
        plot_flight_data(data)
        self.assertTrue(os.path.exists("spirit_airlines_plot.png"))
        self.assertTrue(os.path.exists("airline_heatmap.png"))

if __name__ == '__main__':
    unittest.main()
