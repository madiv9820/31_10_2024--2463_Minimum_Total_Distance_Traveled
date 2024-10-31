- ## Brute Force (Using Recursion)
    - ### Intuition
        - The problem requires us to assign a number of robots to factories such that the total distance traveled by the robots is minimized. Each factory has a limited capacity, meaning that not all robots can be assigned to any single factory. The key intuition is to explore all possible assignments of robots to factories while keeping track of the distances, ensuring we consider the constraints on factory capacities.

    - ### Approach
        1. **Recursive Function**: We use a recursive function `find_Distance` that takes the current robot's index as an argument.
        2. **Base Case**: If all robots are assigned (i.e., the index equals the length of the robot list), we return a distance of 0.
        3. **Loop through Factories**: For each factory, if there is available capacity, we:
            - Assign a robot to that factory (reduce its capacity).
            - Calculate the distance for this assignment and make a recursive call for the next robot.
            - Backtrack by restoring the factory's capacity after exploring this path.
        4. **Track Minimum Distance**: We maintain a variable to track the minimum distance encountered during the recursive calls.

        This approach allows us to exhaustively explore all valid assignments and find the one that minimizes the total distance.

    - ### Time Complexity
        - The time complexity of this approach is \(O(m<sup>n</sup>)\), where \(n\) is the number of robots and \(m\) is the number of factories. In the worst case, we may explore all combinations of robot assignments across all factories.

    - ### Space Complexity
        - The space complexity is \(O(n)\) due to the recursion stack used by the recursive function. Each recursive call adds a layer to the call stack, with a maximum depth equal to the number of robots.

    - ### Code
        ```python3 []
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
        ```