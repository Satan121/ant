# luole 

#! /usr/bin/python 

# 引入相关模块
import sys,os,random
from math import *

# 引入DAG图信息
TaskNum = 
CostOfTask = []        # 每个任务所需要的处理时间
for it in range(TaskNum):
    CostOfTask.append(0)
CostOfTask[0] = 
CostOfTask[1] = 
CostOfTask[2] = 
CostOfTask[3] = 
CostOfTask[4] = 
CostOfTask[5] = 
CostOfTask[6] = 
CostOfTask[7] = 
CostOfTask[8] = 
CostOfTask[9] = 
CostOfTask[10] = 
CostOfTask[11] = 

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



#设置全局变量
BestScheduleList = []
TaskList = []
InfoList = []
InfoChangeList = []
AntList = []

class DAG_ANT:
    def __init__(self, TaskCount=51, AntCount=51, Q=20, Alpha=2.6, Beta=6, Rou=0.2, Generation=100):
        # 类的初始化，给数据赋初值
        self.TaskCount = TaskCount
        self.AntCount = AntCount
        self.Q = Q
        self.Alpha = Alpha
        self.Beta = Beta
        self.Rou = Rou
        self.Generation = Generation
        self.Shortest = 10e4

        random.seed()

        for it in range(TaskCount):
            BestScheduleList.append(-1)
        for row in range(TaskCount):
            InfoListRow = []
            InfoChangeListRow = []
            for col in range(TaskCount):
                InfoListRow.append(100)
                InfoChangeListRow.append(0)
            InfoList.append(InfoListRow)              #初始化信息素列表，赋予初始值 100
            InfoChangeList.append(InfoChangeListRow)  #初始化信息素改变列表，赋予初始值 0

#    def ReadDagInfo(self,Filename):
#        File = open(Filename)
#        for line in file.readlines():
#
#            
#            
#
#
#
    def PutAnts(self):
        AntList.clear()
        for it in range(self.AntCount):
            CurrentTask = 0
            ant = ANT(CurrentTask)
            AntList.append(ant)

    def Search(self):
        for it in range(self.Generation):
            self.PutAnts()
            for Ant in AntList:
                for count in range(TaskCount):
                    Ant.MoveToNextTask(self.Alpha, self.Beta)
                Ant.UpdatePathLen()
            TmpLen = AntList[0].CurrLen                 # 此处的CurrLen对应的是该schedule list 对应的调度长度
            TmpScheduleList = AntList[0].TabuTaskList   # TabuTaskList 就是蚂蚁对应的schedule list
            for Ant in AntList[1:]:
                if Ant.CurrLen < TmpLen:
                    TmpLen = Ant.CurrLen
                    TmpScheduleList = Ant.TabuTaskList
            if TmpLen < self.Shortest:
                self.Shortest = TmpLen
                BestScheduleList = TmpScheduleList
            print(it,":",self.Shortest,":",BestScheduleList)
            self.UpdateInfo()                           # 更行信息素



    def UpdateInfo(self):
        for Ant in AntList:
            for task in Ant.TabuTaskList[0:-1]:
                idx = Ant.TabuTaskList.index(task)
                NextTask = Ant.TabuTaskList[idx + 1]
                InfoChangeList[task][NextTask] += self.Q / Ant.CurrLen
                #InfoChangeList[task][NextTask] += self.Q / Ant.CurrLen     这是关于顺序是否对称的问题，因为任务调度图不是对称的，此处默认不对称
        for row in range(TaskCount):
            for col in range(TaskCount):
                InfoList[row][col] = (1-self.Rou)* InfoList[row][col] + InfoChangeList[row][col]
                InfoChangeList[row][col] = 0


                
def ANT:
    def __init__(self, CurrentTask):
        self.TabuTaskList = []
        self.FreeTaskList = []
        self.TaskSelectProabilityList = []
        self.CurrentTask = 0
        self.CurrLen = 0
        self.AddTask(CurrentTask)
        pass

    def SelectNextTask(self, Alpha, Beta):
        if len(self.FreeTaskList) == 0:
            return(0)
        SumProability = 0.0
        self.TaskSelectProabilityList = []
        for Task in self.FreeTaskList:
            SumProability = SumProability + ( pow(InfoList[self.CurrentTask][Task], Alpha) *
                                              pow(1.0/CostOfCommunication[T                                #   此处是指DAG图上的距离
            Proability = SumProability
            self.TaskSelectProabilityList.append(Task, Proability)
        Threshold = SumProability * random.random()
        for (Task, Proability) in self.TaskSelectProabilityList:
            if Proability >= Threshold:
                return(Task)
        return(0)

    def MoveToNextCity(self, Alpha, Beta):
        NextTask = self.selectNextTask(Alpha, Beta)
        if NextTask>0:
            self.AddTask(NextTask)

#    def ClearTabu(self):
#        self.TabuTaskList = []
#        self.FreeTaskList = 


    def UpdateScheduleLen(self):
        self.CurrLen = SLS(self.TabuTaskList)        #   引入调度长度


    def AddTask(self, Task):
        if Task < 0:
            return
        self.CurrentTask = Task
        self.TabuTaskList.append(Task)
        self.FreeTaskList =                          #   此处是关键，  当添加任务Task后，FreeTaskList应该更新，   如何更新，更新为多少，这需要加函数






if __name__ == '__main__':
    TheDAG_ANT = DAG_ANT()
    TheDAG_ANT.Search()



        




                
                    









































        
