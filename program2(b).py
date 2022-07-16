x = int(input("enter no of pebbles :"))

print("There are %d no of heaps in total" %(x))


lst = []
if x % 2 == 0 :
  var = x + 2
  for i in range(x -1) :
     lst.append(var)
     var += 2
  print("The no of pebbles in heap 1 are %d"%(x))
  for i in range(x -1):
     print("The no of pebbles in heap %d are :"%(i+2))
     print(lst[i])
else :
  var = x + 2
  for i in range(x - 1) :
     lst.append(var)
     var += 2
  print("The no of pebbles in heap 1 are %d"%(x))
  for i in range(x - 1) :
     print("The no of pebbles in heap %d are :"%(i+2)) 
     print(lst[i])
  
       
