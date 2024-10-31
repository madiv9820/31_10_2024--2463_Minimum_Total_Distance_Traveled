from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: ([1,-1], [[-2,1],[2,1]], 2),
            2: ([0,4,6], [[2,2],[6,2]], 4)
        }
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        robot, factory, output = self.testCases[1]
        result = self.obj.minimumTotalDistance(robot = robot, factory = factory)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        robot, factory, output = self.testCases[2]
        result = self.obj.minimumTotalDistance(robot = robot, factory = factory)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()