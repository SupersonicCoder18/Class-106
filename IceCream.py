import plotly.express as px
import csv
import numpy as np

#with open("JunkFood1.csv") as f:
    #df = csv.DictReader(f)
    #fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
    #fig.show()

def GiveDataSource(data_path):
    temperature = []
    icecream = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            icecream.append(float(row["Ice-cream Sales"]))
    return {"x": temperature, "y": icecream}

def FindCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Temperature vs Ice-cream Sales:- ", correlation[0, 1])

def Setup():
    data_path = "./JunkFood1.csv"
    data_source = GiveDataSource(data_path)
    FindCorrelation(data_source)

Setup()