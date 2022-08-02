# Python program of pattern-4
# By : Pranav Visavadia

n=5

print("Using for loop: ")
for i in range(1,n+1):
    if i%2==0:
        for j in range(1,i+1):
            if j%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
    else:
        for j in range(1,i+1):
            if j%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
    print("\n")

print("Using while loop: ")
i=1
while i<=n:
    if i%2==0:
        j=1
        while j<=i:
            if j%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
            j+=1
    else:
        j=1
        while j<=i:
            if j%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
            j+=1
    print("\n")
    i+=1

        
            
            