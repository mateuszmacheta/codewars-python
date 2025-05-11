# 3kyu The Lift
# https://www.codewars.com/kata/58905bfa1decb981da00009e

class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(floor) for floor in queues]
        self.capacity = capacity
        self.floor = 0
        self.TOP_FLOOR = 6
        self.move = 1
        self.passengers = []
        self.history = []

    def make_move(self):
        self.leave_and_enter_lift()
        if not self.passengers:
            floor_to_go = self.find_nearest_passenger()

    def find_nearest_passenger(self):
        pass

    def leave_and_enter_lift(self):
        # leaving if passenger reached their floor
        for e in self.passengers:
            if e == self.floor:
                print(f'Passenger {e} leaves the lift at floor {self.floor}')
                self.passengers.remove(e)

        # checking if passengers want to go
        for e in self.queues[self.floor]:
            if self.move == 1:
                if e > self.floor:
                    self.passengers.append(self.queues[self.floor].pop())
        pass

    def theLift(self):
        i = 0
        while any(self.queues): # there are still passengers:
            i += 1
            print(f'Making move {i:02}')
            self.make_move()
        return self.history
    

tests = [[ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
            [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
            [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
            [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]
    
for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    print(lift.theLift(), answer)