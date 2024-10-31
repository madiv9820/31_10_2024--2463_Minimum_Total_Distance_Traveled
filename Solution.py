from typing import List
import sys

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # This function calculates the minimum total distance robots need to travel
        # to factories, given that each factory has a limited number of robots it can accommodate.
        
        def find_Distance(robot_Index):
            # Base case: If all robots have been assigned, return 0 distance
            if robot_Index == len(robot):
                return 0
            
            # Initialize the minimum distance to a large number
            min_Distance = sys.maxsize
            
            # Iterate through each factory to assign a robot
            for index in range(len(factory)):
                # Check if the factory has available capacity
                if factory[index][1] > 0:
                    # Temporarily assign a robot to the factory by decrementing its capacity
                    factory[index][1] -= 1
                    
                    # Calculate the distance for the current assignment and the remaining robots
                    current_Distance = abs(factory[index][0] - robot[robot_Index]) + find_Distance(robot_Index + 1)
                    
                    # Update the minimum distance if the current distance is lower
                    min_Distance = min(min_Distance, current_Distance)
                    
                    # Backtrack: Restore the factory's capacity for the next iteration
                    factory[index][1] += 1
            
            return min_Distance
        
        # Start the recursive process from the first robot
        return find_Distance(0)