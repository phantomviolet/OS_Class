class PROCESS_CLASS:
    def __init__(self, A_Alloc, A_Max, B_Alloc, B_Max, C_Alloc, C_Max):
        self.A_Max = A_Max
        self.B_Max = B_Max
        self.C_Max = C_Max
        self.A_Alloc = A_Alloc
        self.B_Alloc = B_Alloc
        self.C_Alloc = C_Alloc
        self.State = True
