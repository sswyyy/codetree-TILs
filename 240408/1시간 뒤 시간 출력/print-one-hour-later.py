hm = input()
list_hm = hm.split(':')
list_hm[0] = int(list_hm[0])
list_hm[1] = int(list_hm[1])
list_hm[0]+=1
print('%d:%d'%(list_hm[0],list_hm[1]))