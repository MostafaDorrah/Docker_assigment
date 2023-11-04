from sklearn.cluster import KMeans
import pandas as pd

def model(df):

    X = df.drop(["Outcome"],axis=1) 

    kmeans = KMeans(n_clusters=2)

    kmeans.fit(X)

    df['Cluster'] = kmeans.labels_
    values = df['Cluster'].value_counts()
    
    lines = []
    for i in range(1,3):
        lines.append(f'This is cluster {i} and it contains : {values[i-1]}\n')
    lines
    
    
    with open("k.txt","w+") as f:
        for line in lines:
            f.write(line)
 