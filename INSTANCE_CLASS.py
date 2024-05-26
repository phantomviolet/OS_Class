class INSTANCE_CLASS:
    def __init__(self, A_Instance, B_Instance, C_Instance):
        self.A_Instance = A_Instance
        self.B_Instance = B_Instance
        self.C_Instance = C_Instance
        
    def set_instance(self):
        self.A_Instance, self.B_Instance, self.C_Instance = map(int, input().split())