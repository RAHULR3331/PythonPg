def print_number_pyramid(num):
    for i in range(1,num+1):       
        for j in range(num-i):
            print(" ",end=" ")        
        for j in range(1,i+1):
            print(j,end=" ")       
        for j in range(i-1,0,-1):
            print(j,end=" ")       
        print()
num = int(input("Enter the number of num for the pyramid: "))
print_number_pyramid(num)
