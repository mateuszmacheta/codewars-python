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

    def make_move(self):
        # no passengeres
        if not self.passengers:
            floor_to_go = self.find_nearest_passenger()

    def find_nearest_passenger(self):
        # go up and down at the same time
        pass

    def theLift(self):
        return []
    

tests = [[ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
            [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
            [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
            [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]
    
for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    print(lift.theLift(), answer)