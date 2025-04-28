 l=[]
    mark=set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sub_list=[name,score]
        mark.add(score)
        l.append(sub_list)
    l1=list(mark)
    l1.sort()
    sec_lowest=l1[1]
    names=[name for name,score in l if score==sec_lowest]
    names.sort()
    for i in names:
        print(i)
  
