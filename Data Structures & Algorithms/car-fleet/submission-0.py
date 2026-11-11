class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car cannot pass another car; only can catch up and drive the same speed
        # so we need to see if the 2 cars can catch up to one another; 
        # base on its speed and distance

        # main question how do we check if the car are able to catch up?

        # (take the target - its index position) / 3
        # (10 - 1) / 3 = 3 hrs
        # (10 - 4) / 2 = 3 hrs

        # car fleet can't be empty
        # how do we check if the other car can catch up? 
        # (by checking if the second car speed is greater than the previous car speed)


        # (10 - 4) / 2 = 3 
        # (10 - 1) / 2 = 4.5 hrs
        # (10 - 0) / 1 = 10 hrs
        # (10 - 7) / 1 = 3
        # 1, 0 slower than first car 
        # 4, 7 same speed
        
        # create like 2 empty list 
        # to store the arrays 
        # than extract those 2 and 

        # Sort cars from closest to the target to farthest.
        # Calculate each car’s arrival time.
        # If its time is less than or equal to the fleet ahead’s time, it catches that fleet. Otherwise, it forms a new fleet.
        combined_list = []
        for pos, spd in zip(position, speed):
            combined_list.append((pos, spd))
        
        combined_list.sort(reverse=True)

        fleets = 0
        fleet_time = 0

        for pair in combined_list:
            time = (target - pair[0]) / pair[1]

            if time > fleet_time:
                fleets += 1
                fleet_time = time

        return fleets




