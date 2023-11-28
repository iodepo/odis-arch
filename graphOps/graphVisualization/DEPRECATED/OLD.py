import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# load mdp into a dataframe

df = pd.read_csv('/content/drive/MyDrive/Data/vizSetSmall.csv')

edges = df[['source', 'target', 'type']]

ids = pd.concat([df['source'], df['target']]).reset_index(drop=True)
types = pd.concat([df['sType'], df['tType']]).reset_index(drop=True)
nodes = pd.DataFrame({'Id': ids, 'SDOType': types})

nodes.drop_duplicates()

nodes['Label'] = ['Label ' + str(i) for i in range(len(nodes))]

edges.to_csv('./edges.csv', index=False)
nodes.to_csv('./nodes.csv', index=False)

