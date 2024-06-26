#include <stdio.h>
#include <stdbool.h>
#define MAX 5

typedef struct {
    int A_Max;
    int A_Alloc;
    int B_Max;
    int B_Alloc;
    int C_Max;
    int C_Alloc;
    bool State;
} PROCESS;

typedef struct {
    int A_Instance;
    int B_Instance;
    int C_Instance;
}INSTANCE;

INSTANCE Set_Instance();
PROCESS Set_Process();

int main(void) {

    int i;
    PROCESS P[MAX];
    INSTANCE inter_process_instance;

    inter_process_instance = Set_Instance();
    for (i = 0; i < MAX; i++) {
        P[i] = Set_Process();
        inter_process_instance.A_Instance -= P[i].A_Alloc;
        inter_process_instance.B_Instance -= P[i].B_Alloc;
        inter_process_instance.C_Instance -= P[i].C_Alloc;
    }

    i = 0;
    while (true) {
        if (P[i].State && inter_process_instance.A_Instance + P[i].A_Alloc >= P[i].A_Max) {
            //프로세스 시작
            //프로세스 종료 반환 시작
            P[i].State = false;
            inter_process_instance.A_Instance += P[i].A_Alloc;
            inter_process_instance.B_Instance += P[i].B_Alloc;
            inter_process_instance.C_Instance += P[i].C_Alloc;
            printf("Process %d end", i);
            i = 0;
        }
        else {
            i++;
        }
    }




    return 0;
}

INSTANCE Set_Instance() {
    INSTANCE temporary_Instance;
    printf("Instance A : \n");
    scanf("%d", &temporary_Instance.A_Instance);
    printf("Instance B : \n");
    scanf("%d", &temporary_Instance.B_Instance);
    printf("Instance C : \n");
    scanf("%d", &temporary_Instance.C_Instance);

    return temporary_Instance;
}

PROCESS Set_Process() {
    PROCESS temporary_Process;
    printf("Max A : ");
    scanf("%d\n", &temporary_Process.A_Max);
    printf("Max B : ");
    scanf("%d\n", &temporary_Process.B_Max);
    printf("Max C : ");
    scanf("%d\n", &temporary_Process.C_Max);
    
    printf("Allocation A : ");
    scanf("%d\n", &temporary_Process.A_Alloc);
    printf("Allocation B : ");
    scanf("%d\n", &temporary_Process.B_Alloc);
    printf("Allocation C : ");
    scanf("%d\n", &temporary_Process.C_Alloc);
    temporary_Process.State = true;
    return temporary_Process;
}