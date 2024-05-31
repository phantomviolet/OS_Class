import threading

turn = 0
flag = [False, False]

def function_i():
    while True:
        flag[0] = True
        turn = 1

        while (flag[1] and turn == 1):
            print("thread i is starting")

        flag[0] = False

def function_j():
    while True:
        flag[1] = True
        turn = 0

        while(flag[0] and turn == 0):

            print("thread j is starting")

        
        flag[1] = False



thread_i = threading.Thread(target=function_i)
thread_j = threading.Thread(target=function_j)

thread_i.start()
thread_j.start()

thread_i.join()
thread_j.join()
