import time
import cmath
import math

#helper functions
def expect(c, b, a):
    if(a == 0):
        a = 0.0000002
    a = a/2
    d = (b ** 2) - (4 * a * c)
    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    #print('The solution are {0} and {1}'.format(sol1, sol2.__abs__()))
    return sol2.__abs__()

class Reservation:

    def toString(self):
        return ("[ Vin: " + str(self.vin) + " ,speed: " + str(self.speed) + " ,accel: " +  str(self.accel) + " ,Entered time: " + str(self.enterTime) + " ,Lane #: " + str(self.lane)  + " ,Expected time #: " + str(self.expectedTime) + "]")


    def __init__(self, VIN, speed, accel, enterTime, lane ):
        self.vin = VIN
        self.speed = speed
        self.accel = accel
        self.enter = 0  #0 if entering -- 1 if exiting
        self.enterTime = enterTime
        self.expectedTime = time.time() +  expect(-100, self.speed, self.accel)
        self.nextt = None
        self.prev = None
        self.lane = lane


class Intersection:  #doubly linkd list
    # car criteria
    car_max_accel = 3
    car_max_decel = -3
    car_max_speed = 50

    # Intersection Criteria
    inter_side_length = 100
    inter_max_speed = 20
    inter_tolerance_time = 0.12  # intersection_side_length/[(max_Speed + min_speed)/2] (0.12s)  ---only 1 car in an in


    def __init__(self):
        self.start = 1
        self.head = Reservation(0 , 0, 0, 0, 0)
        self.tail = Reservation(99999 , 0, 0, 0, 0)
        self.size = 0


    def find_closest(self, res):

        if self.head.nextt is None:
            print("List is empty, returning head")
            return self.head
        else:
            temp = self.head.nextt # closest
            n = self.head.nextt
            while n is not self.tail:  # loop until reached tail
                if (abs(n.expectedTime - res.expectedTime) < (abs(temp.expectedTime - res.expectedTime)) ):
                    temp = n
                n = n.nextt
            if n is self.tail:
                print("searched all, closest is VIN: " + str(temp.vin))
                return temp



    def addReservation(self, VIN, speed, accel, enterTime, lane):
        new_node = Reservation(VIN, speed, accel, enterTime, lane)

        # check if lane is safe: (1)lane is empty at that time (2) does not cut the line in its lane
        if(self.check_avalability_initial(new_node)):
            # If no head, set new node as head
            if self.head.nextt == None:
                self.head.nextt = new_node
                self.head.nextt.nextt = self.tail
                self.tail.prev = new_node
                return
            else:
                current_node = self.head
                # if next not none (tail) continue traversing
                while current_node.nextt != self.tail:
                    current_node = current_node.nextt
                # if tail, add to end
                current_node.nextt = new_node
                # set prev pointer to current node
                new_node.prev = current_node
                # set new tail to new node
                new_node.nextt = self.tail
                self.tail.prev = current_node
            self.size = self.size = 1


    def addReservation2(self,res):
        new_node = res
        if (self.check_avalability_initial(new_node)):
            # If no head, set new node as head
            if self.head.nextt == None:
                self.head.nextt = new_node
                self.head.nextt.nextt = self.tail
                self.tail.prev = new_node
                return
            else:
                current_node = self.head
                # if next not none (tail) continue traversing
                while current_node.nextt != self.tail:
                    current_node = current_node.nextt
                # if tail, add to end
                current_node.nextt = new_node
                # set prev pointer to current node
                new_node.prev = current_node
                # set new tail to new node
                new_node.nextt = self.tail
                self.tail.prev = current_node
            self.size = self.size = 1

    def print_as_list(self):
        # Create empty list
        value_list = []
        if self.head != None:
            current_node = self.head.nextt
            # Start at head and check if next is not tail
            while current_node.nextt != None:
                # Add current node to list and traverse forward
                #value_list.append(current_node.toString())
                print current_node.toString()
                current_node = current_node.nextt
            #print value_list
        else:
            print "No nodes"
            return False

    # check if lane is safe: (1)lane is empty at that time (2) does not cut the line in its lane
    def check_avalability_initial(self, res):
        #print ("\n\n " + str(res.vin))
        #print res.toString()
        current_node = self.head


        #search all nodes TODO:only search near by nodes
        #if empty
        if self.head.nextt is None:
            print("List is empty, adding")
            return True
        #if not empty
        else:
            n = self.head.nextt
            while n is not self.tail:  #loop until reached tail
                if (abs(n.expectedTime - res.expectedTime) < self.inter_tolerance_time) or  ((n.expectedTime  > res.expectedTime) and (n.lane == res.lane)): #(1) colision in lane  (2) line skip
                    print abs(n.expectedTime - res.expectedTime)
                    print "no room"
                    return False
                n = n.nextt
            if n is self.tail:
                print("appears to be room")
                return True




temp = time.time()



inter = Intersection()
inter.addReservation(0001,10,0.0,time.time(), 1)

time.sleep(1)
inter.addReservation(0002, 10.0, 0.0,time.time(), 1)



time.sleep(1)
inter.addReservation(0003, 10.0, 0.0,time.time(), 4)

time.sleep(1)
inter.addReservation(0004, 10.0, 0.0,time.time(), 2)

#check for find closest:
new_node = Reservation(13, 12, 0.5, time.time(), 99)
inter.find_closest(new_node)
print new_node.expectedTime


print "\n\n\ntotoal calc time: "+ str(time.time() - temp)
inter.print_as_list()



