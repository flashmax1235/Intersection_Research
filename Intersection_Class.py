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
        self.proposedTime = 0
        self.set = 0


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

    def addReservation3(self, res):
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
                self.tail.prev = new_node
            self.size = self.size = 1
        else:
            print "When there is no room"
            cursor = self.look_right_initial(res) # makes sure nothing in LANE is coming post-expectedTime
            if(cursor == None): # nothing to worry about on the right
                print "no issues regarding lane to the right"
                left = self.find_open_left(res)
                right = self.find_open_right(res)

                goal = self.calcEnergyNeeded(left,right)

            elif(cursor == self.tail.prev.nextt):  #if last enetry is same lane   TODO:FIX bug regrding tail being incorrect
                    print "same lane at end of list"
                    #reservation must be at end of the list
                    res.proposedTime = self.tail.prev.nextt.expectedTime + 0.2
                    #within criteria?
            else:
                print cursor.toString()
                left = self.find_open_left(cursor)
                right = self.find_open_right(cursor)
                if(left != None):
                    print "Option on left: " + str(left.toString())
                else:
                    print "Option on left: none"
                if (right != None):
                    print "Option on right: " + str(right.toString())
                else:
                    print "Option on right: none"





    def calcEnergyNeeded(self):
        #compare required energy, return
        print "energy"

    def withinCriteria(self,res):
        print "check critera"

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
                if (abs(n.expectedTime - res.expectedTime) < self.inter_tolerance_time) or ((n.expectedTime  > res.expectedTime) and (n.lane == res.lane)): #(1) colision in lane  (2) line skip   TODO:specify whitch criteria it failed at
                    print abs(n.expectedTime - res.expectedTime)
                    print "no room"
                    return False
                n = n.nextt
            if n is self.tail:
                print("appears to be room")
                return True

    # find open space to left: (1) size greater than tolerance*2 (2) no line skipping
    # returns head. if nothing found
    def find_open_left(self, res):
        current_node = self.find_closest(res)

        print current_node.toString()

        while(current_node.prev != None):
            if (abs(current_node.expectedTime - current_node.prev.expectedTime) > 2*self.inter_tolerance_time) and  (current_node.nextt.lane != res.lane): # (1) enough space  lane  (2) line skip
                return current_node  # returns right node x---(x)
            current_node = current_node.prev
        return None

    # find open space to left: (1) size greater than tolerance*2 (2) no line skipping
    # returns head. if nothing found
    def find_open_right(self, res):
        current_node = self.find_closest(res)

        print current_node.toString()

        while(current_node.nextt != None):
            if abs(current_node.expectedTime - current_node.nextt.expectedTime) > 2*self.inter_tolerance_time:  # (1) enough space  lane
                return current_node   # returns right node x---(x)
            current_node = current_node.prev
        return None

    # searches all reservation to the right of closest, cannon be in the same lane, must go after
    # if none found, look_open_left is correct, if same lane found, can only look to the right from that point
    def look_right_initial(self,res):
        current_node = self.find_closest(res)
        last_same_lane = None
        while current_node != self.tail:
            if(current_node.lane == res.lane):
                last_same_lane = current_node
            current_node =  current_node.nextt
        return last_same_lane



temp = time.time()



inter = Intersection()



new_node = Reservation(1, 10, 0, time.time(), 1)
inter.addReservation2(new_node)
time.sleep(.4);

new_node = Reservation(2, 10, 0, time.time(), 2)
inter.addReservation2(new_node)
time.sleep(0.15)


new_node = Reservation(3, 10, 0, time.time(), 5)
inter.addReservation2(new_node)
time.sleep(.13);

new_node = Reservation(4, 10, 0, time.time(), 9)
inter.addReservation2(new_node)
time.sleep(0.42)

new_node = Reservation(6, 10, 0, time.time(), 2)
inter.addReservation2(new_node)
time.sleep(0.15)

new_node = Reservation(7, 10, 0, time.time(), 7)
inter.addReservation2(new_node)
time.sleep(0.1)

#test
new_node = Reservation(8, 15, 0, time.time(), 7)
inter.addReservation3(new_node)
print new_node.expectedTime
print inter.look_right_initial(new_node).toString()




print "\n\n\ntotoal calc time: "+ str(time.time() - temp)
inter.print_as_list()



