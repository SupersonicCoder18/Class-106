import plotly.express as px
import csv
import numpy as np

#with open("CoffeeSleep.csv") as f:
    #df = csv.DictReader(f)
    #fig = px.scatter(df, x = "Coffee in ml", y = "Sleep in hours")
    #fig.show()

def GiveDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["Sleep in hours"]))
    return {"x": coffee, "y": sleep}

def FindCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Coffee in ml vs Sleep in hours:- ", correlation[0, -1])

def Setup():
    data_path = "./CoffeeSleep.csv"
    data_source = GiveDataSource(data_path)
    FindCorrelation(data_source)

Setup()