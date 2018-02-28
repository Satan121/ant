def GetBL(task):
    focus_Judge = 1
    for it in range(TaskCount):
        if CostOfCommunication[task][it] > 0:
            focus_Judge = 0
    if focus_Judge = 1:
        return CostOfTask[task]
    else:
        bl_max = 0
        for it in range(TaskCount):
            if CostOfCommunication[task][it]>0:
                bl_tmp = GetBL(it) + CostOfCommunication[task][it] + CostOfTask[task]
                if bl_tmp>bl_max:
                    bl_max = bl_tmp
        return bl_max
                




































