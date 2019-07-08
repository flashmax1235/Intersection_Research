class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class CarCriteria:
    """
    max speed
    max accel
    max deccel
    """
    
class IntersectionCriteria:
    """
    distance_to_light = 100m
	lane_length = 3m
	intersection_side_length = 2* lane_length
	max_speed = 60m/s
	min_speed = 45m/s
	tolerance_time = intersection_side_length/[(max_Speed + min_speed)/2] (0.12s)  ---only 1 car in an intersaection at a time
    """


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found  
             
    #check if lane is safe: (1)lane is empty at that time (2) does not cut the line in its lane
    def find_tolerance(self, key, tolerance, lane):
        """
        current = head
        --check if time is open and wont colide
        while current
            if [(abs(current.time - time) < tolerance)  or [(lane = self.lane) and (current.time > time) ]]
               return false
       return true
        """
      
     #TODO
    def find_closest(self,time):
        """
        curr = self.head
        close = none
        while (curr!=trailer):
            if(curr.time............
            curr = curr.next
        return curr  # Will be None if not found
        """
    

    #find open space to left: (1) size greater than tolerance*2 (2) no line skipping   
    def find_open_left(self,time,tolerance, lane):
        """
        curr = find_closest()
        
        while (curr!= header):
            if[(room between curr and curr.prev) and (curr.lane !=lane)]
                inbetween_time = (curr.time + curr.prev.time)/2
                inbetween_time_tolerance = [(curr.time - curr.prev.time)-(2*tolerance)]/2
                return inbetween_time and inbetween_time_tolerance
            curr = curr.prev
        return none  # Will be None if not found
        """   

    #TODO find open space to right: (1) size greater than tolerance*2 (2) no line skipping
    def find_open_right(self,time,tolerance, lane):
    
        """
        curr = find_closest()
        
        while (curr!= header):
            if[(room between curr and curr.prev) and (curr.next.lane !=lane)]
                inbetween_time = (curr.time + curr.prev.time)/2
                inbetween_time_tolerance = [(curr.time - curr.prev.time)-(2*tolerance)]/2
                return inbetween_time and inbetween_time_tolerance
            curr = curr.prev
        return none  # Will be None if not found
        """
    
        
    def within_criteria(self, time, time_tolerance, lane, CarCriteria ):
        """
        --if left:
        required_acceleration_max = [(2*dX)/Vo*(T+time_tolerance)]/(T+time_tolerance)^2
        required_acceleration_min = [(2*dX)/Vo*(T-time_tolerance)]/(T-time_tolerance)^2
        
        max_velocity = ..
        
        if right:
        required_acceleration_min = [(2*dX)/Vo*(T+time_tolerance)]/(T+time_tolerance)^2
        required_acceleration_max = [(2*dX)/Vo*(T-time_tolerance)]/(T-time_tolerance)^2
        max_velocity = ..
        
        does (required_acceleration_min < CarCriteria.maxAccel) and (max_velocity < CarCriteria.max_velocity)
        """
            
            
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None