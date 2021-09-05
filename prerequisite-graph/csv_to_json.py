import pandas as pd
import utils
import networkx as nx
import math
import json

INPUT_PATH = './mocking_courses.csv'
OUTPUT_PATH = './mocking_graph.json'

# load data
df = pd.read_csv(INPUT_PATH, encoding='utf-8')
df = df.drop(df.columns[7:], axis = 1).rename(columns = utils.transform)
df = df.fillna("")
print(df.head())

# init nodes for graph
G = nx.DiGraph()

for index, row in df.iterrows():
    G.add_node(row.ma_hp, 
               course_id = row.ma_hp, course_name = row.ten_hp, manager = row.bmql)
    
def my_add_edges(G, course, pre_courses, type):
    pre_courses = [item.strip(' \n')for item in pre_courses]

    for pre_course in pre_courses:
        if len(pre_course):
            G.add_edge(pre_course, course, type = type)

# add prerequisite edge of each course to graph
for index, row in df.iterrows():
    course = row.ma_hp
    my_add_edges(G, course, row.ma_hp_hoc_truoc.split(','), 'học trước')
    my_add_edges(G, course, row.ma_hp_tien_quyet.split(','), 'tiên quyết')

with open(OUTPUT_PATH, 'w', encoding = 'utf-8') as f:
    json.dump(nx.node_link_data(G), f)

