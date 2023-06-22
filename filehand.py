# f = open("sample.txt",'x')
# f.close()

# with open("sample.txt",'w') as f:
#     f.write("hello world")

with open("sample.txt",'a') as f:
    f.write("\n welcome to euphoria")

with open("sample.txt",'r') as f:
  for l in f.readlines(): print(l,end=" ")