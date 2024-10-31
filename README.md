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
