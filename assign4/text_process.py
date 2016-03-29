import string

######## Begin code which needs to be modified ##########
import numpy as np
    

class MyChainDict(object):
    def __init__(self):
        #inititalization of two numpy arrays, one for keys, one for values
        self.mychaindict = np.zeros(1000000,dtype = np.ndarray)
        self.mykeychain = np.zeros(1000000,dtype = np.ndarray)
        #size of table
        self.tableSize = self.mychaindict.size
        #number of elements added
        self.size = 0
        return

    def insert(self,key, value):
        #gets the hash
        h = self.getHash(key)
        if self.mychaindict[h] == 0:
            #if the slot is empty, create repective lists and enter respective values
            self.mykeychain[h] = list()
            self.mychaindict[h] = list()
            self.mychaindict[h].insert(0,value)
            self.mykeychain[h].insert(0,key)
        #if the slot is not empty    
        else:
            #if the key is already in the hash table, find its value and overwrite it
            if self.mykeychain[h].count(key) > 0:
                index = self.mykeychain[h].index(key)
                self.mychaindict[h][index] = value
            #else just insert
            else:      
                self.mykeychain[h].insert(0,key)
                self.mychaindict[h].insert(0,value)
        #increase size
        self.size+=1

    #hash function. We use the inbuild python one
    def getHash(self,key):
        return (hash(key)%self.tableSize)

    #only needs to check our keychain hash table
    def contains(self,key):
        h = self.getHash(key)
        if(self.mykeychain[h]==0):
            return False
        else:
            num = len(self.mykeychain[h])
            for i in range(0,num):
                if(self.mykeychain[h][i]==key):
                    return True
            return False

    #grabs the index of the key in its hash table and returns the value at the index 
    #of the values hash table
    def value(self,key):
        h = self.getHash(key)
        index = self.mykeychain[h].index(key)   
        return self.mychaindict[h][index]   
        
    #finds the index of the key. Deletes the key, deletes the value at the index
    #of the valeu hash table
    def delete(self,key):
        h = self.getHash(key)
        if self.mykeychain[h] != 0:
            index = self.mykeychain[h].index(key)
            self.mykeychain[h].remove(key)
            self.mychaindict[h].remove(self.mychaindict[h][index])
        return
        
    #builds a list of the tuplel pairs by iterating through the entire array
    def get_key_values(self):
        total = list()    
        for i in range(-1,self.tableSize-1): 
            if(self.mykeychain[i]!=0):
                length = len(self.mychaindict[i])
                for j in range(length-1,-1,-1):
                     v2 = self.mykeychain[i][j]
                     v1 = self.mychaindict[i][j]
                     a = (v2,v1)
                     total.insert(0,a)
        return total
             
    #prints the both hash tables in order
    def dump(self):
        for i in range(0,self.tableSize):
            num = (len(self.mychaindict[i]))
            for j in range(0,num):
                print(self.mychaindict[i][j])
                print(self.mykeychain[i][j])
 
   
#linear implementation of hash table           
class MyOpenLinearDict(object):
    def __init__(self):
        #builds the same two hash tables
        self.myopendict = np.zeros(10, dtype=np.ndarray)
        self.myopenkey = np.zeros(10, dtype=np.ndarray)
        self.tableSize = self.myopendict.size
        self.keySize = self.tableSize
        self.size = 0
        return

    #hashing function
    def getHash(self, key):
        return (hash(key)%self.tableSize)
    
    #our insert function
    def insert(self, key, value):
        #if the load factor reaches halfway we rehash the tables
        if self.size == (self.tableSize)/2:
            self.resize()
        h = self.getHash(key)
        #if the slot is empty, substantiate a list and input
        if self.myopendict[h] == 0:
            self.myopenkey[h] = list()
            self.myopendict[h] = list()
            self.myopendict[h].insert(0,value)
            self.myopenkey[h].insert(0,key)
        else:
            #check that by going down the array, the key hasnt already been entered
            while self.myopenkey[h] != 0:
                if self.myopenkey[h][0] == key:
                    self.myopendict[h][0] = value
                    return
                #else increase our hash until an avaiable space is reached
                else:
                    h+=1
                    h = h%self.tableSize
            #substantiate a list and input
            self.myopendict[h] = list()
            self.myopenkey[h] = list()
            self.myopendict[h].insert(0, value)
            self.myopenkey[h].insert(0, key)
        self.size+=1
        
    #linearly go down the table to seach for the key
    def contains(self, key):
        count = 0
        h = self.getHash(key)
        if self.myopenkey[h] == 0:
            return False
        else:
            while self.myopenkey[h] != 0 and count != self.size:
                if self.myopenkey[h][0] == key:
                    return True
                else:
                    count+=1
                    h+=1
                    h = h%self.tableSize
            return False


    #returns the value of the key
    def value(self, key):
        h = self.getHash(key)
        while self.myopenkey[h][0] != key:
            h+=1
            h = h % self.tableSize
        return self.myopendict[h][0]

    #linearly searches for the key, finds the index and removes bothe
    #the key and value at the index
    def delete(self, key):
        h = self.getHash(key)
        if self.contains(key):
            while self.myopenkey[h][0] != key:
                h+=1
                h = h % self.tableSize
            del self.myopendict[h]
            del self.myopenkey[h]
        return

    #returns a list of tuple pairs
    def get_key_values(self):
        total = list()
        for i in range(-1, self.tableSize-1):
            if(self.myopenkey[i] != 0):
                v1 = self.myopendict[i][0]
                v2 = self.myopenkey[i][0]
                tup = (v2, v1)
                total.insert(0,tup)
        return total
        
    #prints the table in order
    def dump(self):
        for i in range(-1,self.tableSize-1):
	   if(self.myopenkey!=0):
              print(self.myopenkey[i][0])
	      print(Self.myopendict[i][0])


    #our rehash function
    def resize(self):
        self.tableSize = self.tableSize*2
        self.size = 0
        rehashvalue = np.zeros(self.tableSize, dtype = np.ndarray)
        rehashkey = np.zeros(self.tableSize, dtype = np.ndarray)
        for i in range(-1, self.myopenkey.size):
            if(self.myopenkey[i] != 0):
                value = self.myopendict[i][0]
                key = self.myopenkey[i][0]                
                h = self.getHash(key)
                if rehashvalue[h] == 0:
                    rehashkey[h] = list()
                    rehashvalue[h] = list()
                    rehashvalue[h].insert(0,value)
                    rehashkey[h].insert(0,key)
                else:
                    while rehashkey[h] != 0:
                        h+=1
                        h = h%self.tableSize
                    rehashvalue[h] = list()
                    rehashkey[h] = list()
                    rehashvalue[h].insert(0, value)
                    rehashkey[h].insert(0, key)
                self.size+=1
        self.myopendict = rehashvalue
        self.myopenkey = rehashkey
        return


#implentation of our quadratic hashig\ng
class MyOpenQuadDict(object):
    def __init__(self):
        self.myopenquad = np.zeros(1000000, dtype=np.ndarray)
        self.myquadkey = np.zeros(1000000, dtype=np.ndarray)
        self.tableSize = self.myopenquad.size
        self.keySize = self.tableSize
        self.size = 0
        return

    def getHash(self, key):
        return (hash(key)%self.tableSize)
    
    def insert(self, key, value):
        #to combat the problems of quadratic hashing
        #rehash if load fatcor is 1/30
        if self.size == (self.tableSize)/10:
            self.resize()
        h = self.getHash(key)
        x = 0
        if self.myopenquad[h] == 0:
            self.myquadkey[h] = list()
            self.myopenquad[h] = list()
            self.myopenquad[h].insert(0,value)
            self.myquadkey[h].insert(0,key)
        else:
            while self.myquadkey[h] != 0:
                if self.myquadkey[h][0] == key:
                    self.myopenquad[h][0] = value
                    return
                else:
                    #hash at h+x^2
                    x+=1
                    h+= ((x)**2)
                    h = h%self.tableSize
            self.myopenquad[h] = list()
            self.myquadkey[h] = list()
            self.myopenquad[h].insert(0, value)
            self.myquadkey[h].insert(0, key)
        self.size+=1
        
    def contains(self, key):
        count = 0
        x = 0
        h = self.getHash(key)
        if self.myquadkey[h] == 0:
            return False
        else:
            while self.myquadkey[h] != 0 and count != self.tableSize:
                if self.myquadkey[h][0] == key:
                    return True
                else:
                    #quadraticaly walks through the hash table
                    count+=1
                    x+=1
                    h+= ((x)**2)
                    h = h%self.tableSize
            return False


    def value(self, key):
        h = self.getHash(key)
        x = 0
        while self.myquadkey[h][0] != key:
            #quadraticaly walks through the hash table
            x+=1
            h+= ((x)**2)
            h = h % self.tableSize
        return self.myopenquad[h][0]


    def delete(self, key):
        x = 0
        h = self.getHash(key)
        if self.contains(key):
            while self.myquadkey[h][0] != key:
                #quadraticaly walks through the hash table
                x+=1
                h+= ((x)**2)
                h = h % self.tableSize
            del self.myopenquad[h]
            del self.myquadkey[h]
        return

    def get_key_values(self):
        total = list()
        for i in range(-1, self.tableSize-1):
            if(self.myquadkey[i] != 0):
                v1 = self.myopenquad[i][0]
                v2 = self.myquadkey[i][0]
                tup = (v2, v1)
                total.insert(0,tup)
        return total
        
    
    #needs to be redone
    def dump(self):
        for i in range(-1,self,tableSize-1):
	    if(self.myopenquad[k]!=0):
	    	print(self.myquadkey[i]][0])
            	print(self.myopenquad[i][0])

		

    def resize(self):
        self.tableSize = self.tableSize*2
        self.size = 0
        x = 0
        rehashvalue = np.zeros(self.tableSize, dtype = np.ndarray)
        rehashkey = np.zeros(self.tableSize, dtype = np.ndarray)
        for i in range(-1, self.myquadkey.size):
            if(self.myquadkey[i] != 0):
                value = self.myopenquad[i][0]
                key = self.myquadkey[i][0]                
                h = self.getHash(key)
                
                if rehashvalue[h] == 0:
                    rehashkey[h] = list()
                    rehashvalue[h] = list()
                    rehashvalue[h].insert(0,value)
                    rehashkey[h].insert(0,key)
                else:
                    while rehashkey[h] != 0:
                        x+=1
                        h+= ((x)**2)
                        h = h%self.tableSize
                    rehashvalue[h] = list()
                    rehashkey[h] = list()
                    rehashvalue[h].insert(0, value)
                    rehashkey[h].insert(0, key)
                self.size+=1
        self.myopenquad = rehashvalue
        self.myquadkey = rehashkey
        return




class YourSet(object):
    def __init__(self):
        self.yourset = np.zeros(100,dtype = np.ndarray)
        self.tableSize = self.yourset.size
        return

    def getHash(self, key):
        return (hash(key)%self.tableSize)

    def insert(self, key):
        h = self.getHash(key)
        if self.yourset[h] == 0:
            self.yourset[h] = list()
            self.yourset[h].insert(0,key)
        else:
            self.yourset[h].insert(0,key)
    
    def contains(self, key):
        h = self.getHash(key)
        if(self.yourset[h]==0):
            return False
        else:
            num = len(self.yourset[h])
            for i in range(0,num):
                if(self.yourset[h][i]==key):
                    return True
            return False

    def dump(self):
        for i in range(0,self.tableSize):
            num = (len(self.yourset[i]))
            for j in range(0,num):
                print(self.yourset[i][j])

######## End code which needs to be modified ##########


# Store the set of stop words in a set object
stop_words_file = "stopwords.txt"
stop_words = YourSet()

with open(stop_words_file) as f:
    for l in f:
        stop_words.insert(l.strip())


# Download file from https://snap.stanford.edu/data/finefoods.txt.gz        
# Remember to gunzip before using
review_file = "foods_test.txt"

review_words = []
for i in range(5):
    review_words.append(MyChainDict())
    
with open(review_file, encoding='LATIN-1') as f:
    lines = f.readlines()
    idx = 0
    num_lines = len(lines) - 2
    while idx < num_lines:
        while not lines[idx].startswith("review/score"):
            idx = idx + 1

        # Jump through hoops to satisfy the Unicode encodings 
        l = lines[idx].encode('ascii', 'ignore').decode('ascii')
        l = l.strip().split(":")[1].strip()

        # Extract rating
        rating = int(float(l))
        while not lines[idx].startswith("review/text"):
            idx = idx + 1
            
        l = lines[idx].encode('ascii', 'ignore').decode('ascii').strip().lower()
        text = l.split(":")[1].strip()
        text = text.translate(str.maketrans("","", string.punctuation))

        # Extract words in the text 
        words = text.split(" ")
        # words = [x.strip(string.punctuation) for x in text.split(" ")]
        for w in words:
            if len(w) and not stop_words.contains(w):
                if review_words[rating - 1].contains(w):
                    count = review_words[rating - 1].value(w) + 1
                else:
                    count = 1
                
                review_words[rating - 1].insert(w, count)

# Print out the top words for each of the five ratings 
for i in range(5):
    freq_words = sorted(review_words[i].get_key_values(), key=lambda tup: tup[1], reverse=True)
    print(i+1, freq_words[0:20])
