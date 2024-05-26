import PROCESS_CLASS
import INSTANCE_CLASS
import bkr_function


My_Process = [
    PROCESS_CLASS.PROCESS_CLASS(0, 1, 0, 7, 5, 3),
    PROCESS_CLASS.PROCESS_CLASS(2, 0, 0, 3, 2, 2),
    PROCESS_CLASS.PROCESS_CLASS(3, 0, 2, 9, 0, 2),
    PROCESS_CLASS.PROCESS_CLASS(2, 1, 1, 2, 2, 2),
    PROCESS_CLASS.PROCESS_CLASS(0, 0, 2, 4, 3, 3)
]
Inter_Instance = INSTANCE_CLASS.INSTANCE_CLASS(10, 5, 7)



i = 0
while True:
    if (My_Process[i].State) and bkr_function.cmp_A_Ins_and_Max(Inter_Instance.A_Instance, My_Process[i].A_Alloc, My_Process[i].A_Max) and (Inter_Instance.B_Instance + My_Process[i].B_Alloc >= My_Process[i].B_Max):
        if (bkr_function.cmp_B_Ins_and_Max(Inter_Instance.B_Instance, My_Process[i].B_Alloc, My_Process[i].B_Max)):
            if(bkr_function.cmp_C_Ins_and_Max(Inter_Instance.C_Instance, My_Process[i].C_Alloc, My_Process[i].C_Max)):
                My_Process[i].State = False
                Inter_Instance.A_Instance += My_Process[i].A_Alloc
                Inter_Instance.B_Instance += My_Process[i].B_Alloc
                Inter_Instance.C_Instance += My_Process[i].C_Alloc
                print("Process %d" %i)
                i = 0
    else:
        i += 1
        
