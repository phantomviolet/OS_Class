def cmp_A_Ins_and_Max(A_Instance, A_Alloc, A_Max):
    State_A = (A_Instance + A_Alloc >= A_Max)
    return State_A
def cmp_B_Ins_and_Max(B_Instance, B_Alloc, B_Max):
    State_B = (B_Instance + B_Alloc >= B_Max)
    return State_B
def cmp_C_Ins_and_Max(C_Instance, C_Alloc, C_Max):
    State_C = (C_Instance + C_Alloc >= C_Max)
    return State_C