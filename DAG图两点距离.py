# 用来计算DAG图两点之间的距离

CostOfCommunication = []      # 任务之间通信时间，没有通信默认为0
for row in range(TaskNum):
    CostOfCommunicationRow = []
    for col in range(TaskNum):
        CostOfCommunicationRow.append(0)
    CostOfCommunication.append(CostOfCommunicationRow)

CostOfCommunication[][] = 
CostOfCommunication[][] = 
CostOfCommunication[][] = 
CostOfCommunication[][] = 
CostOfCommunication[][] = 
CostOfCommunication[][] = 
CostOfCommunication[][] = 
CostOfCommunication[][] = 
CostOfCommunication[][] = 




TaskDistance = []                          #DAG图两task之间的距离
for row in range(TaskNum):
    TaskDistanceRow = []
    for col in range(TaskNum):
        TaskDistanceRow.append(0)
    TaskDistance.append(TaskDistanceRow)
        
for row in range(TaskNum):
    for col in range(TaskNum):
        if CostOfCommunication[row][col] == 0:
            TaskDistance[row][col] = CONST - 0.01*BL(col)                     # 没有连接的两个任务之间的距离，等于一个固定常数（CONST） 减去 col对应任务的BL值,需要添加一个BL函数
        else:
            TaskDistance[row][col] = CostOfCommunication[row][col]






        
