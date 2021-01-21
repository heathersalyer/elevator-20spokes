class Elevator: 

    def __init__ (self, floors, current_floor, direction):
        self.floors = floors
        self.current_floor = current_floor
        self.direction = direction
        self.descend = []
        self.ascend = []

    # a user should be able to view the current floor 
    def elevator_location(self):
        print(f'The elevator is located on floor {self.current_floor}.')

    def going_up(self):
        if self.direction == 'up':
            self.current_floor += 1

    def going_down(self):
        if self.direction == 'down':
            self.current_floor -= 1

    def elevator_in_motion(self, *args):
        if len(args) == 0:
            self.direction = 'waiting'
            return self.direction
        print(f'The elevator is waiting for input on floor {self.current_floor}.')   
        
    
        for input in args:
            # if input is > floor and input not in ascend array append to array and sort 
            if input > self.current_floor and input not in self.ascend:
                self.ascend.append(input)
                self.ascend.sort()
            # if input < floor and input not in descend array append to array and sort 
            elif input < self.current_floor and input not in self.descend:
                self.descend.append(input)
                self.descend.sort(reverse = True)

        print(self.ascend)
        print(self.descend)

        if self.direction == 'up':
            for floor in self.ascend[:]:
                # conduct while loop going up until input is reached
                while floor != self.current_floor:
                    self.going_up()
                    print(self.current_floor)
                # When input is reached open and close doors and remove floor from ascend list. 
                self.open_door()
                self.ascend.pop(0)
                self.close_door()
            self.direction == 'down'

        if self.direction == 'down':
            for floor in self.descend[:]:

                # conduct while loop and count down until input is reached 
                while floor != self.current_floor:
                    self.going_down()  
                    print(self.current_floor)
                # When input is reached open doors, remove the number from the descend list, and continue to descend.
                self.open_door()
                self.descend.pop(0)
                self.close_door()
            

    # message that elevator is at desired floor 
    def open_door(self):
        print('Door is opening')

    def close_door(self):
        print('Door is closing')  

elevator = Elevator(20, 7, 'up')
print(elevator.elevator_location())
print(elevator.elevator_in_motion(12,14,17,4,3,2))
