import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import networkx as nx

df = pd.read_csv("road_network.csv")

print(df.head())

print("\nDataset Shape:", df.shape)
print("\nDataset Information")

print(df.info())
print("\nMissing Values")

print(df.isnull().sum())
df["VC_Ratio"] = (
    df["avg_daily_traffic"]
    /
    df["capacity_vehicles_per_hour"]
)

df["Congestion"] = (
    df["VC_Ratio"] > 1
).astype(int)

print("\nV/C Ratio Calculation")

print(
    df[
        [
            "road_id",
            "VC_Ratio",
            "Congestion"
        ]
    ].head()

)
print("\nSVM Training")

X = df[["VC_Ratio"]]

y = df["Congestion"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = SVC(kernel="rbf")

model.fit(X_train, y_train)

print("SVM Model Trained Successfully")
pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("\nSVM Evaluation")

print("Accuracy =", acc)
cm = confusion_matrix(y_test, pred)

print("\nConfusion Matrix")

print(cm)
G = nx.Graph()

for i in range(20):

    G.add_node(df["road_id"][i])

for i in range(19):

    G.add_edge(
        df["road_id"][i],
        df["road_id"][i+1],
        weight=df["length_km"][i]
    )

print("\nGraph Construction")

print("Nodes =", G.number_of_nodes())

print("Edges =", G.number_of_edges())
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

nx.draw(G, with_labels=True)

plt.title("Road Network Graph")

plt.show()
path = nx.dijkstra_path(
    G,
    "RD-0001",
    "RD-0020"
)

print("\nDijkstra Execution")

print(path)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1000,
    font_size=8
)

# Highlight Dijkstra route
route_edges = list(zip(path, path[1:]))

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=route_edges,
    width=3
)

plt.title("Final Recommended Route using Dijkstra Algorithm")

plt.show()
print("\nFinal Output")

print("Traffic Congestion Prediction Completed Successfully")

print("Predicted Route:", path)

print("Total Nodes:", G.number_of_nodes())

print("Total Edges:", G.number_of_edges())


