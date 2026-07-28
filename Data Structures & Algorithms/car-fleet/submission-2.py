class Solution:
    # https://neetcode.io/problems/car-fleet/question?list=neetcode150
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        lead_vehicle_arrival_time = None
        # Sort cars based on distance remaining
        cars = list(zip(map(lambda p: target - p, position), speed))
        cars.sort(key=lambda c: c[0])
        for car in cars:
            arrival_time = car[0] / car[1] #distance remaining / speed
            # If car arrives later than lead vehicle, it becomes lead vehicle in new fleet
            if not lead_vehicle_arrival_time or arrival_time > lead_vehicle_arrival_time:
                lead_vehicle_arrival_time = arrival_time
                res += 1
        return res