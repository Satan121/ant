#_*_coding:utf-8_*_
import sys, os, random
from math import *

# 设置全局变量
TIME_MAX_LIMIT = 10000       # 最大时间限制，若cc[i][j] = TIME_MAX_LIMIT 则代表i，j任务之间没有通信
BestScheduleList = []
InfoList = []
InfoChangeList = []
AntList = []
CONST_DISTANCE = 10  # 此处设计的是没有通信的两个任务之间距离为固定值 ，可以改动



'''   #任务图1
# 引入DAG图信息
NumOfProcessor = 3           # Number of processor
TaskNum = 12         # 注意，在DAG_ant 类的初始化参数中，有一个 TaskCount，也需要设为同样的值
TaskList = [0,1,2,3,4,5,6,7,8,9,10,11]  # 一定要将 TaskList初始化

CostOfTask = []      # 每个任务所需要的处理时间,task从0开始
for it in range(TaskNum):
    CostOfTask.append(0)
CostOfTask[0] = 11
CostOfTask[1] = 18
CostOfTask[2] = 18
CostOfTask[3] = 7
CostOfTask[4] = 11
CostOfTask[5] = 18
CostOfTask[6] = 11
CostOfTask[7] = 7
CostOfTask[8] = 18
CostOfTask[9] = 11
CostOfTask[10]= 21
CostOfTask[11]= 7

CostOfCommunication = []  # 任务之间通信时间，没有通信默认为TIME_MAX_LIMIT
for row in range(TaskNum):
    CostOfCommunicationRow = []
    for col in range(TaskNum):
        CostOfCommunicationRow.append(TIME_MAX_LIMIT)
    CostOfCommunication.append(CostOfCommunicationRow)
CostOfCommunication[0][1] = 23
CostOfCommunication[0][2] = 23
CostOfCommunication[0][3] = 23
CostOfCommunication[1][8] = 18
CostOfCommunication[1][9] = 18
CostOfCommunication[1][10] = 44
CostOfCommunication[2][11] = 1
CostOfCommunication[2][7] = 1
CostOfCommunication[3][7] = 18
CostOfCommunication[3][4] = 18
CostOfCommunication[3][6] = 18
CostOfCommunication[3][5] = 18
CostOfCommunication[9][11] = 1
CostOfCommunication[10][11] = 1
'''

# 引入DAG图信息
NumOfProcessor = 3           # Number of processor
TaskNum = 11         # 注意，在DAG_ant 类的初始化参数中，有一个 TaskCount，也需要设为同样的值
TaskList = [0,1,2,3,4,5,6,7,8,9,10]  # 一定要将 TaskList初始化

CostOfTask = []      # 每个任务所需要的处理时间,task从0开始
for it in range(TaskNum):
    CostOfTask.append(0)
CostOfTask[0] = 5
CostOfTask[1] = 3
CostOfTask[2] = 4
CostOfTask[3] = 4
CostOfTask[4] = 2
CostOfTask[5] = 2
CostOfTask[6] = 6
CostOfTask[7] = 5
CostOfTask[8] = 6
CostOfTask[9] = 2
CostOfTask[10]= 4

CostOfCommunication = []  # 任务之间通信时间，没有通信默认为TIME_MAX_LIMIT
for row in range(TaskNum):
    CostOfCommunicationRow = []
    for col in range(TaskNum):
        CostOfCommunicationRow.append(TIME_MAX_LIMIT)
    CostOfCommunication.append(CostOfCommunicationRow)
CostOfCommunication[0][1] = 2
CostOfCommunication[0][2] = 3
CostOfCommunication[0][3] = 4
CostOfCommunication[0][4] = 4

CostOfCommunication[1][5] = 2
CostOfCommunication[1][6] = 4

CostOfCommunication[2][6] = 5

CostOfCommunication[3][7] = 3

CostOfCommunication[4][7] = 4

CostOfCommunication[5][8] = 2
CostOfCommunication[6][8] = 2
CostOfCommunication[6][9] = 3
CostOfCommunication[7][9] = 3
CostOfCommunication[8][9] = 1

CostOfCommunication[8][10] = 5

CostOfCommunication[9][10] = 1


#-------------------------------------------------------------------主程序-------------------------------------------
# 对task_start_time和task_processor_select两个数组赋初始值0
task_start_time = []
for i in range(0, TaskNum):
    task_start_time.append(0)
task_processor_select = []
for i in range(0, TaskNum):
    task_processor_select.append(0)

# sls函数,用来计算对应scheduleList所需时间
def sls(ct,
        cc,
        schedule_list,
        task_start_time,  # 每个任务开始执行的时间
        task_processor_select  # 每个任务选择的处理器
        ):
    for i in range(0, TaskNum):
        current_task = schedule_list[i]  # 从schedule_list里依次抽取任务座位current_task进行调度

        # 把任务遍历所有的处理器，选出得到最早任务开始时间的那个座位best_processor_for_current_task
        best_processor_for_current_task = get_best_processor_for_current_task(ct,
                                                                              cc,
                                                                              schedule_list,
                                                                              task_start_time,
                                                                              task_processor_select,
                                                                              current_task
                                                                              )
        # 得出best_processor_for_current_task后，就可以把current_task放到这个处理器上，调度得到对应task_start_time[current_task] \
        # 和task_processor_select[current_task]
        schedule_current_task_on_processor(ct,
                                           cc,
                                           schedule_list,
                                           task_start_time,
                                           task_processor_select,
                                           current_task,
                                           best_processor_for_current_task
                                           )
    # 遍历每一个任务，计算每个任务结束的时间，选择那个最晚的，就是整个任务调度的时间
    schedule_time = 0
    for task in range(0, TaskNum):
        if (task_start_time[task] + ct[task] > schedule_time):
            schedule_time = task_start_time[task] + ct[task]
        else:
            schedule_time = schedule_time

    return (schedule_time)

def get_best_processor_for_current_task(ct,
                                        cc,
                                        schedule_list,
                                        task_start_time,
                                        task_processor_select,
                                        current_task
                                        ):
    # 把current_task遍历每一个处理器，选择能使任务最早开始的那个处理器
    min_task_start_time_on_best_processor = TIME_MAX_LIMIT
    for processor in range(1, NumOfProcessor+1):
        # 使用current_task_start_time_on_profossor 函数来计算current_task在当前处理器下的最早开始时间
        task_start_time_on_current_procssor = current_task_start_time_on_profossor(ct,
                                                                                   cc,
                                                                                   schedule_list,
                                                                                   task_start_time,
                                                                                   task_processor_select,
                                                                                   current_task,
                                                                                   processor
                                                                                   )
        # 如果得出的时间早于min_task_start_time_on_best_processor，则表示该处理器有更好效果，更新best_processor
        if (task_start_time_on_current_procssor < min_task_start_time_on_best_processor):
            min_task_start_time_on_best_processor = task_start_time_on_current_procssor
            best_processor = processor

    return (best_processor)

def current_task_start_time_on_profossor(ct,
                                         cc,
                                         schedule_list,
                                         task_start_time,
                                         task_processor_select,
                                         current_task,
                                         processor
                                         ):
    max_task_finish_time_on_processor = 0
    for task in range(TaskNum):
        if ((task_processor_select[task] == processor) &
            ((task_start_time[task] + ct[task]) > max_task_finish_time_on_processor)
        ):
            max_task_finish_time_on_processor = (task_start_time[task] + ct[task])

    max_pred_communication_finish_time = 0
    for task in range(TaskNum):
        if ((cc[task][current_task] < TIME_MAX_LIMIT) &
                (task_processor_select[task] != processor)
            ):
            if (task_start_time[task] + ct[task] + cc[task][current_task] > max_pred_communication_finish_time):
                max_pred_communication_finish_time = task_start_time[task] + ct[task] + cc[task][current_task]

    if (max_pred_communication_finish_time > max_task_finish_time_on_processor):
        return (max_pred_communication_finish_time)
    else:
        return (max_task_finish_time_on_processor)



def schedule_current_task_on_processor(ct,
                                       cc,
                                       schedule_list,
                                       task_start_time,
                                       task_processor_select,
                                       current_task,
                                       processor
                                       ):
    # 得到任务开始时间

    task_start_time[current_task] = current_task_start_time_on_profossor(ct,
                                                                         cc,
                                                                         schedule_list,
                                                                         task_start_time,
                                                                         task_processor_select,
                                                                         current_task,
                                                                         processor
                                                                         )
    # 得到任务选择的处理器
    task_processor_select[current_task] = processor

# 自由节点函数
def updata_free_point(cost_of_communication, choosed_point, all_point):
    free_point = []
    rest_point = list(set(choosed_point) ^ set(all_point))  # 取all_point和choosed_point的差集，选择那些还没有被选择的任务
    for i in choosed_point:
        for j in rest_point:
            if (cost_of_communication[i][j] != TIME_MAX_LIMIT):  # 选出与choosed_point有通信的可选任务
                free_value = 1
                for k in rest_point:  # 排除前驱没有干净的任务
                    if (cost_of_communication[k][j] != TIME_MAX_LIMIT):
                        free_value = 0
                        break
                if (free_value == 1):
                    free_point.append(j)  # 添加该任务到free
    return (free_point)

#------------------------------------------------蚁群算法框架---------------------------------------------------------

class DAG_ANT:
    #def __init__(self, TaskCount=12, AntCount=12, Q=20, Alpha=2.6, Beta=6, Rou=0.5, Generation=500):
    def __init__(self, TaskCount=11, AntCount=11, Q=20, Alpha=2.6, Beta=6, Rou=0.5, Generation=200):
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
                InfoListRow.append(90)               #此处可调节，是初始信息素的值
                InfoChangeListRow.append(0)
            InfoList.append(InfoListRow)  # 初始化信息素列表，赋予初始值 100
            InfoChangeList.append(InfoChangeListRow)  # 初始化信息素改变列表，赋予初始值 0

    def PutAnts(self):
        #AntList.clear()
        del AntList[:]
        for it in range(self.AntCount):
            CurrentTask = 0
            ant = ANT(CurrentTask)
            AntList.append(ant)

    def Search(self):  # 关键代码
        for it in range(self.Generation):
            self.PutAnts()
            for Ant in AntList:
                for count in range(self.TaskCount):
                    Ant.MoveToNextTask(self.Alpha, self.Beta)
                Ant.UpdateScheduleLen()
            TmpLen = AntList[0].CurrLen  # 此处的CurrLen对应的是该schedule list 对应的调度长度
            TmpScheduleList = AntList[0].TabuTaskList  # TabuTaskList 就是蚂蚁对应的schedule list
            for Ant in AntList[1:]:
                if Ant.CurrLen < TmpLen:
                    TmpLen = Ant.CurrLen
                    TmpScheduleList = Ant.TabuTaskList
            if TmpLen < self.Shortest:
                self.Shortest = TmpLen
                BestScheduleList = TmpScheduleList
            print(it, self.Shortest, BestScheduleList)
            self.UpdateInfo()  # 更行信息素

    def UpdateInfo(self):
        for Ant in AntList:
            for task in Ant.TabuTaskList[0:-1]:
                idx = Ant.TabuTaskList.index(task)
                NextTask = Ant.TabuTaskList[idx + 1]
                InfoChangeList[task][NextTask] += self.Q / Ant.CurrLen
                # InfoChangeList[task][NextTask] += self.Q / Ant.CurrLen     这是关于顺序是否对称的问题，因为任务调度图不是对称的，此处默认不对称
        for row in range(self.TaskCount):
            for col in range(self.TaskCount):
                InfoList[row][col] = (1 - self.Rou) * InfoList[row][col] + InfoChangeList[row][col]
                InfoChangeList[row][col] = 0

class ANT:
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
            return (0)
        SumProability = 0.0
        self.TaskSelectProabilityList = []
        # -------------------------------------------    创新点就在此处     如何将DAG图中的距离引入算法 --------------------------------------------
        for Task in self.FreeTaskList:  # 此处需要思考，两个不通信的任务之间距离如何判定，创新点就在这
            if (CostOfCommunication[self.CurrentTask][Task] != TIME_MAX_LIMIT):
                SumProability = SumProability + (pow(InfoList[self.CurrentTask][Task], Alpha) *  # 此处需要改写
                                                 pow(1.0 / CostOfCommunication[self.CurrentTask][Task],
                                                     Beta))  # 有通信时，距离为通信世界
            else:
                SumProability = SumProability + (pow(InfoList[self.CurrentTask][Task], Alpha) *
                                                 pow(1.0 / CONST_DISTANCE,
                                                     Beta))  # 对于没有通信的两个任务，他们之间的距离统一为CONST_DISTANCE
            Proability = SumProability
            self.TaskSelectProabilityList.append((Task, Proability))
        Threshold = SumProability * random.random()
        for (Task, Proability) in self.TaskSelectProabilityList:
            if Proability >= Threshold:
                return (Task)
        return (0)

    def MoveToNextTask(self, Alpha, Beta):
        NextTask = self.SelectNextTask(Alpha, Beta)
        if NextTask > 0:
            self.AddTask(NextTask)

    def UpdateScheduleLen(self):
        self.CurrLen = sls(CostOfTask, CostOfCommunication, self.TabuTaskList, task_start_time,
                           task_processor_select)  # 引入调度长度
        global task_start_time
        global task_processor_select

        #print(task_start_time)
        task_start_time = []
        for i in range(0, TaskNum):
            task_start_time.append(0)
        task_processor_select = []
        for i in range(0, TaskNum):
            task_processor_select.append(0)
        
        #print(self.TabuTaskList)
        #print(self.CurrLen)

    def AddTask(self, Task):  # 这个函数的目的是更新对应的任务列表
        if Task < 0:
            return
        self.CurrentTask = Task
        self.TabuTaskList.append(Task)
        self.FreeTaskList = updata_free_point(CostOfCommunication, self.TabuTaskList,
                                              TaskList)  # 此处是关键，  当添加任务Task后，FreeTaskList应该更新，   如何更新，更新为多少，这需要加函数  自由节点。py
#print(self.FreeTaskList)


if __name__ == '__main__':
    TheDAG_ANT = DAG_ANT()
    TheDAG_ANT.Search()
