
# 1、构建图
grpah= {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]

}


# 2、DFS和BFS所需要的python小知识

# set()是集合，添加节点用add方法，[]是数组用append方法

# 查询所有的点
print(grpah.keys())

# 查询某个点的所有临接点
print(grpah["A"])

# 数组 动态增删 pop(弹出)  ap pend(末尾增加)
queues=[]

# 3、BFS思路
"""
1、对于BFS，用hashmap构建图
2、放入图以及开始节点
3、初始化一个数组[]（队列），set()集合作为备忘录
4、每次pop弹出队头，获取它的所有邻接节点
        遍历所有邻接节点
        判断是否在备忘录中，没有则放入队列和备忘录
        

"""


# 传入图、开始节点
def BFS(graph,s):
    #初始化一个动态数组(当做队列 )
    queue=[]
    #初始化一个set集合，作为备忘录，记录某个vertex是否被遍历过
    note = set()
    #放入初始点
    queue.append(s)
    note.add(s)

    while(len(queue)>0):
        # 弹出队列中的首个vertex
        vertex=queue.pop(0)

        # 获取某个vertex的所有邻接点
        nodes=graph[vertex]
        for i in nodes:
            # 判断vertex是否已经被遍历过
            if i  not in note:
                # 将备忘录中没有的vertex放入队列 备忘录
                queue.append(i)
                note.add(i)

        print(vertex)

# 4、DFS思路

"""
1、对于DFS，用hashmap构建图
2、放入图以及开始节点
3、初始化一个数组[]（栈），set()集合作为备忘录
4、每次pop弹出1个栈元素，获取它的所有邻接节点
        遍历所有邻接节点
        判断是否在备忘录中，没有则放入栈和备忘录
"""

# 5、总结
"""
BFS和DFS的区别在于，把栈换成队列即可
"""

# 6、BFS拓展（最短路径-无向图）

"""

1、在BFS的基础上在初始化时添加 parent{key,value}存储某个节点 和 对应的前个节点
2、在放入备忘录时，将某个节点的所有邻接节点放入parent 如<X的邻接节点，X>
3、返回parent

4、从E节点开始搜索得到了如下表，左边为节点，右边为当前节点的前一个节点


E None
C E
D E
A C
B C
F D

假设现在要找从E到B的最短路径

可以找 B->C （B的前一个节点C）-> C->E（C的前一个节点E）-> E->None（E的前面为None）->循环结束

B C E 为最短路径
"""


def ShortestPath(graph,s):
    # 初始化一个动态数组(当做队列)
    queue = []
    # 初始化一个set集合，作为备忘录，记录某个vertex是否被遍历过
    note = set()

    # 存储某个vertex的前个vertex  -最短路径
    parent = {s: None} # 首个vertex无前置vertex

    # 放入初始点
    queue.append(s)
    note.add(s)

    while(len(queue)>0):
        # 弹出队列中的首个vertex
        vertex = queue.pop(0)

        # 获取某个vertex的所有邻接点
        nodes = graph[vertex]
        for i in nodes:
            # 判断vertex是否已经被遍历过
            if i not in note:
                # 将备忘录中没有的vertex放入队列 备忘录
                queue.append(i)
                note.add(i)
                # 放入parent -最短路径
                parent[i] = vertex

        #print(vertex)
    return parent





# 测试
if __name__ == '__main__':

 def DFS(graph,s):
    # 初始化一个动态数组(当做栈 )
    stack=[]
    # 初始化一个set集合，作为备忘录，记录某个vertex是否被遍历过
    note = set()
    # 放入初始点
    stack.append(s)
    note.add(s)

    while(len(stack)>0):
        # 弹出栈中的首个vertex
        vertex=stack.pop()

        # 获取某个vertex的所有邻接点
        nodes = graph[vertex]
        for i in nodes:
            # 判断vertex是否已经被遍历过
            if i  not in note:
                # 将备忘录中没有的vertex放入栈 备忘录
                stack.append(i)
                note.add(i)

        print(vertex)



 grpah ={
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]

       }
 print("================BFS===================")
 BFS(grpah,"A")

 print("================DFS===================")
 DFS(grpah,"A")

 print("================BFS-最短路径===================")
parent=ShortestPath(grpah,"E")

for key in parent:
    print(key,parent[key])

target="B"

print("================BFS"+" E-> "+target+"-最短路径===================")
while  target!=None :
     print(target)
     target=parent[target]
