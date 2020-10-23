import plotly.express as px
import csv
import numpy as np

#with open("TVSize1.csv") as f:
    #df = csv.DictReader(f)
    #fig = px.scatter(df, x = "Coffee in ml", y = "Sleep in hours")
    #fig.show()

def GiveDataSource(data_path):
    size = []
    watch = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            size.append(float(row["Size of TV"]))
            watch.append(float(row["Average time spent watching TV in a week in hours"]))
    return {"x": size, "y": watch}

def FindCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Size of TV vs Average time spent watching TV in a week in hours:- ", correlation[0, 1])

def Setup():
    data_path = "./TVSize1.csv"
    data_source = GiveDataSource(data_path)
    FindCorrelation(data_source)

Setup()