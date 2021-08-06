from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher
import xlrd
import re
from aip import AipNlp

APP_ID = '19052765'
API_KEY = 'uToZ2OK0hkXXXlkXFLgu9lV1'
SECRET_KEY = '3XOQxlI5X4S2jKCs1aQ5hS3Vu7EShpdq'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
# 数据库
graph = Graph("http://localhost:7474", auth=("neo4j", "123456"))

matcher = NodeMatcher(graph)
relMatcher = RelationshipMatcher(graph)

# xlsx路径
path = '/Users/fuuujy/Desktop/三常知识图谱/历史三元组.xlsx'
data = xlrd.open_workbook(path)  # 打开Excel文件读取数据
table = data.sheets()[0]  # 通过索引顺序获取
# 循环xlsx
for j in range(0, table.nrows):  # 循环行列表数据
    title1 = str(table.row(j)[0].value)  # 使用行索引
    title2 = str(table.row(j)[1].value)
    title3 = str(table.row(j)[5].value)
    print("title3=", title3)
    node_a = matcher.match(title3, name=title3, source1='历史', source2=title1, source3=title2).first()
    if not node_a:
        node_a = Node(title3, name=title3, source1='历史', source2=title1, source3=title2)
        graph.create(node_a)
        print(node_a)

    title4 = str(table.row(j)[6].value)
    print("title4=", title4)

    title5 = str(table.row(j)[7].value)
    print("title5=", title5)
    node_c = matcher.match(title5, name=title5, source1='历史', source2=title1, source3=title2).first()
    if not node_c:
        node_c = Node(title5, name=title5, source1='历史', source2=title1, source3=title2)
        graph.create(node_c)
        print(node_c)
    rel = relMatcher.match((node_a, node_c), r_type=title4).first()
    if rel == None:
        rel = Relationship(node_a, title4, node_c)
        graph.create(rel)
        print(rel)

print('Finish')