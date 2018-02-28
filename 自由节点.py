def updata_free_point(cost_of_communication, choosed_point, all_point, free_point):
    rest_point = list(set(choosed_point)^set(all_point))   #取all_point和choosed_point的差集，选择那些还没有被选择的任务
    for i in choosed_point:             
        for j in rest_point:
            if(cost_of_communication[i][j] != 0):          #选出与choosed_point有通信的可选任务
                free_value = 1
                for k in rest_point:                       #排除前驱没有干净的任务
                    if(cost_of_communication[k][j] != 0):
                            free_value = 0   
                            break
                if(free_value ==1):
                    free_value.appen(j)                    #添加该任务到free


                        

#   choosed_point 就是 self.tabuTaskList ,  all_point 就是所有的Task  
