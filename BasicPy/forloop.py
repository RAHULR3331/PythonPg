# # Sum of the 2 matrixes[]

# r=int(input("Enter the size of row"))
# c=int(input("Enter the size of colonm"))
# x=[]
# val=[2]
# for i in range(0,r):
#     for j in range(0,c):
#         val.append(int(input("Enter the %d * %d th elememt"%(i,j))))
#         x.append(val)
#         val=[]

# print("Second matrix")

# y=[]
# for i in range (0,r):
#     for j in range (0,c):
#         val.append(int(input("Enter the %d * %d th elememt"%(i,j))))
#         y.append(val)
#         val=[]

# sum=[]
# # for i in range(0,r):
# #     val = []
# #     for j in range(0,c):
# #         # val.append(x[i][j]+y[i][j])
# #         val.append(x[i][j] + y[i][j])
# #         sum.append(val)


# # print(sum)

# for i in range(r):
#     val = []
#     for j in range(c):
#         val.append(x[i][j] + y[i][j])
#     sum.append(val)

# print(sum)
# -------------------------------------------------------------------------------------------------------------
r = int(input("Enter the size of row: "))
c = int(input("Enter the size of column: "))

x = []
val = []

for i in range(r):
    for j in range(c):
        val.append(int(input("Enter the %d * %d th element: " % (i, j))))
    x.append(val)
    val = []

print("Second matrix")

y = []

for i in range(r):
    val = []
    for j in range(c):
        val.append(int(input("Enter the %d * %d th element: " % (i, j))))
    y.append(val)

print("Sum matrix:")

sum = []

for i in range(r):
    val = []
    for j in range(c):
        val.append(x[i][j] + y[i][j])
    sum.append(val)

print(sum)
