#@vikrantkhedkar SBCO20173
#assignment 2
def modulo_hashing(hash_table, key, data):
    hash_key = key % len(hash_table)
    if hash_table[hash_key]:
        chaining(hash_table, hash_key, data)  

    else:
        hash_table[hash_key].append(data)

def chaining(hash_table, hash_key, data):
    hash_table[hash_key].append(data)
 
def find(hash_table,key,index):
    hash_key=key%len(hash_table)
    if hash_table[hash_key]:
        if hash_table[hash_key][0]==data[index]:
            print(hash_table[hash_key][0])
            print(hash_table)
        else:
            for i in range(len(hash_table[hash_key])):
                if hash_table[hash_key][i]==data[index]:
                    print("Found for  Key:",key)
                    print("Value:",hash_table[hash_key][i])
                    print(hash_table)
    else:
        print("Not found")
def deletedata(hash_table,k,index):
    
    hash_key=k%len(hash_table)
    if hash_table[hash_key]:
        if hash_table[hash_key][0]==data[index]:
           hash_table[hash_key].remove( hash_table[hash_key][0])
           print('deleted')
           key.remove(key[index])
           data.remove(data[index])
        else:
            for i in range(len(hash_table[hash_key])):
                if hash_table[hash_key][i]==data[index]:
                    hash_table[hash_key].remove(hash_table[hash_key][i])
                    print('deleted')
                    key.remove(key[index])
                    data.remove(data[index])
                    print(hash_table)
            
    else:
        print("Not found")
    

key=[_ for _ in range(10)]
data=[_ for _ in range(10)]
hash_table = [[] for _ in range(10)]
n=int(input("Enter 1 to Enter data\nEnter 2 to search \nEnter 3 to delete \nEnter 4 to display \nEnter 0 to exit"))
while n!=0:
    if n==1:
        i=int(input("Enter number of elements"))
        for j in range(i):
            d=input(("Enter data"))
            data[j]=d
            k=int(input("Enter key"))
            key[j]=k
            modulo_hashing(hash_table,k,d)            
           
    if n==2:
        k=int(input("Enter key"))    
        try:  
            index= key.index(k)
            find(hash_table,k,index)
        except:
            print('does not exist')
        finally:
            pass

    if n==3:
        k=int(input("Enter key"))
        index=0
        try:
            index= key.index(k)
            deletedata(hash_table,k,index)
        except:
            print('does not exist')
    if n==4:
        print(hash_table)
        
    if n==0:
        exit()
    n=int(input("Enter 1 to Enter data\nEnter 2 to search \nEnter 3 to delete \nEnter 4 to display\nEnter 0 to exit"))


    



