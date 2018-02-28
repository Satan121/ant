
####################---------------------------#######################
#     2017-11-20
#     luole
#
####################---------------------------#######################

# 配置任务数和处理器数
NT = 3  # Number of task
NP = 2  # Number of processor
TIME_MAX_LIMIT = 10000  # 最大时间限制，若cc[i][j] = TIME_MAX_LIMIT 则代表i，j任务之间没有通信

# 配置DAG图信息
ct = [2, 7, 4]  # cost of task，该数组定义了处理每个任务的时间
cc = [[TIME_MAX_LIMIT for i in range(NT)] for i in range(NT)]  # cost of communication，定义两个任务之间通信的时间消耗
cc[0][1] = 5
cc[0][2] = 1

schedule_list = [0, 2, 1]  # 根据tl，bl算出任务的调度顺序，注意  task 的编号是0,1,2,3

# 对task_start_time和task_processor_select两个数组赋初始值0
task_start_time = []
for i in range(0, NT):
    task_start_time.append(0)
task_processor_select = []
for i in range(0, NT):
    task_processor_select.append(0)


# sls函数
def sls(ct,
        cc,
        schedule_list,
        task_start_time,  # 每个任务开始执行的时间
        task_processor_select  # 每个任务选择的处理器
        ):
    for i in range(0, NT):
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
    for task in range(0, NT):
        if (task_start_time[task] + ct[task] > schedule_time):
            schedule_time = task_start_time[task] + ct[task]
        else:
            schedule_time = schedule_time

    return (schedule_time)


def get_best_processor_for_current_task(ct,
                                        cc,
                                        schedule_time,
                                        task_start_time,
                                        task_processor_select,
                                        current_task
                                        ):
    # 把current_task遍历每一个处理器，选择能使任务最早开始的那个处理器
    min_task_start_time_on_best_processor = TIME_MAX_LIMIT
    for processor in range(1, NP + 1):
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
    max_start_time_on_processor = 0
    # 遍历所有任务
    for task in range(0, NT):
        # 如果该任务也在这个processor上执行，且任务结束时间比现在的max_start_time_on_processor晚，则更新max_start_time_on_processor
        if ((task_processor_select[task] == processor) &
                (task != current_task) &
                (task_start_time[task] + ct[task] > max_start_time_on_processor)
            ):
            max_start_time_on_processor = task_start_time[task] + ct[task]
        # 如果该任务不在此processor上执行，但是任务是current_task的前驱任务，且该任务与current_task通信结束时间晚于max_start_time_on_processor，则跟新max_start_time_on_processor
        elif ((task_processor_select[task] != processor) &
                  (task != current_task) &
                  (cc[task][current_task] != TIME_MAX_LIMIT) &
                  (task_start_time[task] + ct[task] + cc[task][current_task] > max_start_time_on_processor)
              ):
            max_start_time_on_processor = task_start_time[task] + ct[task] + cc[task][current_task]
        else:
            max_start_time_on_processor = max_start_time_on_processor

    return (max_start_time_on_processor)


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


time = sls(ct,
           cc,
           schedule_list,
           task_start_time,
           task_processor_select
           )
print(task_processor_select)
print("the DAG schedule time is : ", time)


