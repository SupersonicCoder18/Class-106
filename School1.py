import plotly.express as px
import csv
import numpy as np

#with open("School1.csv") as f:
    #df = csv.DictReader(f)
    #fig = px.scatter(df, x = "Coffee in ml", y = "Sleep in hours")
    #fig.show()

def GiveDataSource(data_path):
    marks = []
    present = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            present.append(float(row["Days Present"]))
    return {"x": marks, "y": present}

def FindCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Marks in Percentage vs Days Present:- ", correlation[0, 1])

def Setup():
    data_path = "./School1.csv"
    data_source = GiveDataSource(data_path)
    FindCorrelation(data_source)

Setup()