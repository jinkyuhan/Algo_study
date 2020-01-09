import sys

N=int(input())
list=[]
ans=[]
for rope_weights in range(N):
    w=int(input())
    list.append(w)

list.sort()
list_len=len(list)
list_max=list(list_len-1)
ans.append(list_max)

while list_len>1 :
    list_max=list[list_len-1]
    list_min=list[0]
    MAX=list_max
    MIN=list_min * list_len  
    
    if MAX>=MIN:
        ans.append(MAX)

    elif MIN>MAX:
        ans.append(MIN)

    list.pop(0)
    list_len-=1
        # 4print(ans)
    

print(max(ans))





# # 가장 작은 인자 뽑아내기 위해 len 사용
# len_list=len(list)
# print(len_list)

# print(list[len_list-1])