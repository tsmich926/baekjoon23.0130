#피라미드 모양 별출력
""" N = int(input())
for i in range(N+1):
    print('*' * i) """


#역피라미드 모양 별출력
""" N = int(input())
for k in range(N,0,-1):
    print('*' * k) """


# N = int(input())
# for i in range(N):
#     print('' * i)
    # for N in range(i):
    #     print('*' * N)
# for k in range(1,N,-1):
#     print('*')

N = int(input())
for k in range(N,0,-1):
    print('' * k)
for i in range(N+1):
    print('*' * i) 


N = int(input())
for k in range(N,0,-1):
    print('' * k)
for i in range(N+1):
    print(N )
    print('*' * i) 
