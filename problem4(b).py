def monotonic_direction(a):
    n = len(a)
    if all(a[i]<=a[i+1] for i in range(n-1)) :
            return "Increasing"
    if  all(a[i]>=a[i+1] for i in range(n-1)) :
            return "Decreasing"

a = [2,3,4,5,6]
x = monotonic_direction(a)
if x :
   print("Given sequence of numbers is monotonically",monotonic_direction(a))
else :
	print("It is not monotonic")

    
