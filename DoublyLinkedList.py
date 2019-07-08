"""
Variables:
    -IN_Queue: DLL
    -Out_Queue: DLL

"""
class Node(object): 
	def __init__(self, val): 
		self.value = val 
		self.next = None 
		self.prev = None
              
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

class DoublyLinkedList(object): 
	def __init__(self): 
		self.head = None
		self.tail = None

	def add_node(self, val): 
		new_node = Node(val)
		#If no head, set new node as head
		if self.head == None: 
			self.head = new_node
			self.tail = new_node
		else: 
			current_node = self.head
			#if next not none (tail) continue traversing
			while current_node.next != None: 
				current_node = current_node.next
			#if tail, add to end
			current_node.next = new_node 
			#set prev pointer to current node
			new_node.prev = current_node
			#set new tail to new node
			self.tail = new_node

	#Traverse forward
	def traverse_forward(self): 
		if self.head != None: 
			current_node = self.head 
			#If next node is not tail
			while current_node.next != None: 
				#Set current as next and traverse forward
				print "Traverse forward current", current_node.value
				current_node = current_node.next
				print "Traverse forward current", current_node.value
		else: 
			print "No nodes"
			return False
	
	#Traverse backwards 
	def traverse_back(self):
		if self.tail != None: 
			#Set current node to the tail (tail is set when new node added)
			current_node = self.tail 
			#Check to see if at the head, traverse backwards and print
			while current_node.prev != None: 
				print "Traverse backwards current", current_node.value
				current_node = current_node.prev
			print "Traverse backwards current", current_node.value
		else: 
			print "No nodes"
			return False

	def print_as_list(self): 
		#Create empty list
		value_list = []
		if self.head != None: 
			current_node = self.head 
			#Start at head and check if next is not tail
			while current_node.next != None: 
				#Add current node to list and traverse forward
				value_list.append(current_node.value)
				current_node = current_node.next 
			value_list.append(current_node.value)
			print value_list
		else: 
			print "No nodes"
			return False

	def remove_node_from_end(self): 
		if self.head != None: 
			current_node = self.head 
			while current_node.next.next != None: 
				current_node = current_node.next
			current_node.next.prev = None
			current_node.next = None
			self.tail = current_node

	def remove_node(self, val): 
		if self.head != None:
			current_node = self.head
			#If val is the head
			if self.head.value == val:
				self.head.next.prev = None
				self.head = self.head.next
			#If val is the tail
			elif self.tail.value == val:
				self.tail.prev.next = None
				self.tail = self.tail.prev
			else:
				while current_node.next.value != val:
					current_node = current_node.next
					#If val is not in list
					if current_node.next.value != val:
						print "Value not in list"
						return False
				#Set next next node's prev pointer to current node
				current_node.next.next.prev = current_node
				#Set next node to current's next next pointer
				current_node.next = current_node.next.next

	def insert_node_after(self, val, insert_val): 
		if self.head != None: 
			#Create new node
			current_node = self.head 
			new_node = Node(insert_val)
			#If val is first item in list, insert after 
			if self.head.value == val: 
				self.head.next.prev = new_node
				new_node.prev = self.head
				new_node.next = self.head.next
				self.head.next = new_node
			#If tail is val, create new tail
			elif self.tail.value == val: 
				self.tail.next = new_node
				new_node.prev = self.tail
				self.tail = new_node
			else: 
				#If neither head nor tail, traverse through
				while current_node.value != val: 
					current_node = current_node.next 
					#If val is not in list, give error message
					if current_node.value != val: 
						print "Value not in list"
						return False
				#Set new node's next to current node's next 
				new_node.next = current_node.next
				#Insert new node next to current node
				current_node.next = new_node
				#Set new node next prev's pointer to new node
				new_node.next.prev = new_node
				#Set new node's prev pointer to current node 
				new_node.prev = current_node

    #check if lane is safe: (1)lane is empty at that time (2) does not cut the line in its lane
    def check_availibility(self, time, tolerance, lane):
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
    




    def find_open_left(self,time,tolerance, lane):
        """
        curr = find_closest(time)
        
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
            if[(room between curr and curr.next) and (curr.next.lane !=lane)]
                inbetween_time = (curr.time + curr.next.time)/2
                inbetween_time_tolerance = [(curr.time - curr.next.time)-(2*tolerance)]/2
                return (inbetween_time and inbetween_time_tolerance)
            curr = curr.next
        return tail # return last thing in list
        """
    
    
    #checks if proposed acceleration plan is realistic and (1)fits car and intersection requiremnts
    def within_criteria(self, time, time_tolerance, lane, CarCriteria ):

        """
        
        delta_time <--time  (elapsed time)
        
        --if left:
        required_acceleration_min = [(2*dX)/Vo*(T+time_tolerance)]/(T+time_tolerance)^2
        //required_acceleration_max = [(2*dX)/Vo*(T-time_tolerance)]/(T-time_tolerance)^2
        
       
        
        --if right:
        //required_acceleration_max = [(2*dX)/Vo*(T+time_tolerance)]/(T+time_tolerance)^2  ??
        required_acceleration_min = [(2*dX)/Vo*(T-time_tolerance)]/(T-time_tolerance)^2 ??
      
       max_velocity = Vo + required_acceleration_min * (delta_time)
        
        does (required_acceleration_min < CarCriteria.maxAccel) and (max_velocity < CarCriteria.max_velocity)
            return True
        """
            

    #calulates energy required to accel/decel car to needed state (used for comparing left and right)
    def calculate_energy_needed():
        """
        return joules
        """
    
    #(1)find placement for car (2) reserve time (3) sends data to car
    def IN_request_handler(Vin, carSpeed, lane, CarCriteria, IntersectionCriteria):    
        """
        fate_time = IntersectionCriteria.distance_to_light/ carSpeed
        check_availibility(fate_time, IntersectionCriteria.tolerance, lane)
        
        if availible:
            Queue.add(Vin,lane,fate_time)
        else:
            open_left = find_open_left(fate_time,IntersectionCriteria.tolerance,lane)
            open_right = find_open_right(fate_time,IntersectionCriteria.tolerance,lane)
            
            if(open_left and open_right exist):
                if(left_energy > right_energy):
                    Queue.add(Vin,lane,open_left.time)
                    send data to car
                else:
                    Queue.add(Vin,lane,open_right.time)
                    send data to car
            elif(open_left exist):
                Queue.add(Vin,lane,open_left.time)
                send data to car
            
           else:  --increased time(worst case end of queue)
                if(open_right != tail):
                    Queue.add(Vin,lane,open_right.time)
                    send data to car
                else:
                    Queue.add(Vin,lane,open_right.time + IntersectionCriteria.tolerance)
                    send data to car
        """
    
    #ensures safe passage out of intersection (1) 100m (2) wont bump/skip lane
    def OUT_request_handler(Vin, carSpeed,lane,CarCriteria,IntersectionCriteria):
        """
        is it safe to restore speed limit?
        
        yes:
            car decel/accel to speedlimit
        
        no:
            create accel/decel plan that is safe (1)car/intersection criteria (2) no skipping lane
        
        
        
        """
        
    
        