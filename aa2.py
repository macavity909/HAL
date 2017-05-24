import matplotlib.pyplot as plt 
gaussian_numbers = [1,1,1,1,3,3,3,3,3,4,4,4,4,4,4,4,4,3,3,3,3,6,6,6,5,5,5,5,5,5,5,5,1,1,2,2,2,2,1,1]
f = open('test.txt', 'r')
#gaussian_numbers = f.readlines()


#print (gaussian_numbers)
#plt.hist(gaussian_numbers,bins=6)



 
asd = f.read().split('b')
asd.pop()
print(asd)
ss = []
cnt = 0;
for i in asd:
    if cnt>0:
        qq = i.strip('\'')
        ss.append( float(qq) )
    cnt = cnt+1
    
print(ss)
plt.hist(ss,bins=20)
plt.title("Gaussian ")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


#qq = asd[4].strip('\'')
#print (int(qq)+5)

    


