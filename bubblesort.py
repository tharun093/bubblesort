list=[1,4,5,7,8,9,4]
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j+1],list[j]=list[j],list[j+1]


sort(list)
print(list)