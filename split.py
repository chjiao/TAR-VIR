# Input Hint
filename = input("Input filename: ")
k = int(input("how many files you want to split to: "))

# Load the original file
f = open(filename)
file = f.readlines()


length = len(file)                   # Total length of the file
length_seq = length//2               # Total number of seq(reads)
length_seq_num = length_seq//int(k)  # Number of reads in each splitted file

# Splitting the file
for i in range(k-1):
    temp = file[i*length_seq_num*2:i*length_seq_num*2+length_seq_num*2]
    f = open("virus"+str(i+1)+".fa", 'w')
    for L in temp:
        f.write(L)
    f.close()

# For the Last splitted file, save all the remained reads
temp = file[(k-1)*length_seq_num:]
f = open("virus"+str(k)+".fa", 'w')
for L in temp:
    f.write(L)
f.close()