# Problem Link : 

u = int(input())
for _ in range(u):
    a = int(input())
    a,b = list(map(int, input().split(" ")))
    a = list(map(int,input().split()))



# Open function to open the file "MyFile1.txt"  
# (same directory) in append mode and 
file1 = open("MyFile.txt","a") 
  
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
file2 = open(r"D:\Text\MyFile2.txt","w+")