class Solution:
    # https://neetcode.io/problems/car-fleet/question?list=neetcode150
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # cars cant pass
        # a fleet is a set of cars such that they arrive at destination together
        # a lone car is a fleet
        # position and speed are parallel arrays
        # [4,1,0,7] = sample position
        # [2,2,1,1] = sample speed
        # 10 = target
        # [3, 4.5, 10, 3] = time to target
        res = 0
        lead_vehicle_arrival_time = None
        # The vehicles are not given in a sorted order.
        #    target - position how much distance is remaining for the cars
        cars = list(zip(map(lambda p: target - p, position), speed))
        cars.sort(key=lambda c: c[0])
        for car in cars:
            arrival_time = car[0] / car[1] #distance remaining / speed
            # If the current vehicle arrives slower than the lead vehicle
            # A new fleet is started
            if not lead_vehicle_arrival_time or arrival_time > lead_vehicle_arrival_time:
                lead_vehicle_arrival_time = arrival_time
                res += 1
        return res