#Vikrant SBCO20173
# modulo_hashing


def modulo_hashing(hash_table, key, data, choice):
    hash_key = key % len(hash_table)
    if hash_table[hash_key]:
        if choice == 1:
            chaining(hash_table, hash_key, data)
        elif choice == 0:
            linear_probing(hash_table, hash_key, data)

    else:
        hash_table[hash_key].append(data)

# display


def display(key):
        hash_key = key % len(hash_table)
        print(hash_table[hash_key])
    


    

# chain linking


def chaining(hash_table, hash_key, data):
    hash_table[hash_key].append(data)

# linear probing


def linear_probing(hash_table, hash_key, data):
    print('linear probing')
    hash_key = hash_key+1
    count = 1
    for i in range(len(hash_table)):

        if hash_key < len(hash_table):
            if hash_table[hash_key]:
                hash_key = hash_key+1
                count = count+1

            else:
                hash_table[hash_key] = data
                print('steps required',count)
                break

        else:
            hash_key = 0


# driver code 
#  
#using linear probing
hash_table = [[] for _ in range(10)]
key = 1010101019
data = "Vikrant"
modulo_hashing(hash_table, key, data, 0)
key = 2020202099
data = "Leo"
modulo_hashing(hash_table, key, data, 0)
display(1010101019)
print(hash_table)

#using chain linking
hash_table = [[] for _ in range(10)]
key = 1010101019
data = "Vikrant"
modulo_hashing(hash_table, key, data, 1)
key = 2020202099
data = "Leo"
modulo_hashing(hash_table, key, data, 1)
display(2020202099)
print(hash_table)

    
