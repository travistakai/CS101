# tests for Programming Assignment 3, CMPS101 Winter16 
# Copy this file to the folder where "discrete_event.py" is located
# ie. ucscid/assign3/hw3test.py

#Update 1 : Times are float now.
#Update 2 : Added tuple casting

import os.path
import unittest
import numpy as np

#Import student implementation
from discrete_event import ArrayPQ as HeapPQ
#If you import original discrete_event.py it will fail
#because the original implementation initializes collision times to zero


#Original class with collision times initialized at infinity
#Results to be compared with student implementation
class ArrayPQ:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.horizontal_wall_collision_times = np.full([num_balls],float('inf'))
        self.vertical_wall_collision_times = np.full([num_balls],float('inf'))
        self.ball_collision_times = np.full([num_balls,num_balls],float('inf'))
        self.num_collisions = np.zeros(num_balls)
        return
        
    def insert(self, i, j, value, num_collisions_i, num_collisions_j):
        if i == -1:
            self.vertical_wall_collision_times[j] = value
            self.num_collisions[j] = num_collisions_j
        elif j == -1:
            self.horizontal_wall_collision_times[i] = value
            self.num_collisions[i] = num_collisions_i
        else:
            self.ball_collision_times[i][j] = value
            self.num_collisions[j] = num_collisions_j
            self.num_collisions[i] = num_collisions_i

    def get_next(self):
        min_i = -1
        min_j = -1
        tij = float('inf')
        for i in np.arange(self.num_balls):
            for j in np.arange(i, self.num_balls):
                if self.ball_collision_times[i][j] < tij:
                    tij = self.ball_collision_times[i][j]
                    min_i = i
                    min_j = j
        tix = np.min(self.horizontal_wall_collision_times)
        tiy = np.min(self.vertical_wall_collision_times)
        if tix <= tij and tix <= tiy:
            return np.argmin(self.horizontal_wall_collision_times), -1, np.min(self.horizontal_wall_collision_times), self.num_collisions[np.argmin(self.horizontal_wall_collision_times)], -1
        elif tiy < tij and tiy < tix:
            min_i = -1
            min_j = np.argmin(self.vertical_wall_collision_times)
            return -1, np.argmin(self.vertical_wall_collision_times), np.min(self.vertical_wall_collision_times), -1, self.num_collisions[np.argmin(self.vertical_wall_collision_times)]
        else:
            return min_i, min_j, tij, self.num_collisions[min_i], self.num_collisions[min_j]
            
            

class MyTest(unittest.TestCase):
    def test(self):
        for n in range(10,100,10):
            A=ArrayPQ(n)            
            H=HeapPQ(n)
            
            for i in range(1,n-4,2):
                #insert ball collisions in decreasing order
                A.insert(i-1,i,float(n-i),0,0)
                H.insert(i-1,i,float(n-i),0,0)
                
                #check if they are stored in a heapified way.                
                self.assertEqual(tuple(A.get_next()),(i-1,i,float(n-i),0,0))
                self.assertEqual(tuple(H.get_next()),(i-1,i,float(n-i),0,0))

                #try to confuse, insert something that is not min.
                A.insert(3,4,100.0,0,0)
                H.insert(3,4,100.0,0,0)
                
                #check if that does not register as min (latest min still should be the same)
                self.assertEqual(tuple(A.get_next()),(i-1,i,float(n-i),0,0))
                self.assertEqual(tuple(H.get_next()),(i-1,i,float(n-i),0,0))                                               
                    
            #insert wall collisions, check if it works
            A.insert(-1,7,3.0,0,0)
            H.insert(-1,7,3.0,0,0)
                        
            #don't check for num-collisions for wall collisions
            self.assertEqual(tuple(A.get_next())[0:3],(-1,7,3.0))
            self.assertEqual(tuple(H.get_next())[0:3],(-1,7,3.0))         
            
            #try for other wall
            A.insert(8,-1,1.0,0,0)
            H.insert(8,-1,1.0,0,0)
            self.assertEqual(tuple(A.get_next())[0:3],(8,-1,1.0))
            self.assertEqual(tuple(H.get_next())[0:3],(8,-1,1.0))             
            
            #try to confuse wall, insert something that is not min.
            A.insert(-1,2,100.0,0,0)
            A.insert(3,-1,100.0,0,0)
            H.insert(-1,2,100.0,0,0)
            H.insert(3,-1,100.0,0,0)

            #check if that does not register as min (last min should still be the same)
            self.assertEqual(tuple(A.get_next())[0:3],(8,-1,1.0))
            self.assertEqual(tuple(H.get_next())[0:3],(8,-1,1.0))             
            
            
if __name__ == '__main__':

    #Assignment 3 file checks
    filesok=True
    if not os.path.isfile("README.txt") and not os.path.isfile("README"):
        filesok=False        
        print("\nCANTFIND: README. If you have a readme file but still getting this error, check if it is upper case.\n")
    if not os.path.isfile("changes.txt"):
        filesok=False        
        print("\nCANTFIND: changes.txt. Make sure you create a text file explaining the changes you made.\n")
    if not os.path.isfile("observations.txt"):
        filesok=False        
        print("\nCANTFIND: observations.txt. Make sure you comment on whether you observed any significant benefits of switching from an Array to a Heap based Priority Queue.\n")
    if filesok:
        print("\nSeems like you have all your files placed correctly!\n")

    unittest.main(exit=False)
