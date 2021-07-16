def max_sum(list_2D):
    max_sum_r=0
    max_sum_c=0
    max_index_r=-1
    max_index_c=-1

    for i in range(n):
        sum_r=0
        for j in range(m):
            sum_r=sum_r+list_2D[i][j]
        if sum_r>max_sum_r:
            max_sum_r=sum_r
            max_index_r=i


    for j in range(m):
        sum_c=0
        for i in range(n):
            sum_c= sum_c+list_2D[i][j]
        if sum_c> max_sum_c:
            max_sum_c=sum_c
            max_index_c=j


    if max_sum_r>=max_sum_c:
        print("row",max_index_r,max_sum_r)
    else:
        print("column",max_index_c,max_sum_c)

t=int(input())
while(t>0):
    str=input().split()
    n=int(str[0])
    m=int(str[1])
    if n==0 and m==0:
        print("row 0 -2147483648")
        exit()
    list_2D=[[int(j) for j in input().split()] for i in range(n)]
    (max_sum(list_2D))
    t=t-1
