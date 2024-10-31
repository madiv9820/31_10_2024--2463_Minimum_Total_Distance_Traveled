from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: ([1,-1], [[-2,1],[2,1]], 2),
            2: ([0,4,6], [[2,2],[6,2]], 4),
            3: ([9,11,99,101], [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]], 6),
            4: ([789300819,-600989788,529140594,-592135328,-840831288,209726656,-671200998], 
                [[-865262624,6],[-717666169,0],[725929046,2],[449443632,3],[-912630111,0],
                 [270903707,3],[-769206598,2],[-299780916,4],[-159433745,5],[-467185764,3],
                 [849991650,7],[-292158515,6],[940410553,6],[258278787,0],[83034539,2],
                 [54441577,3],[-235385712,2],[75791769,3]],
                582755368)
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

    @timeout(0.5)
    def test_Case3(self):
        robot, factory, output = self.testCases[3]
        result = self.obj.minimumTotalDistance(robot = robot, factory = factory)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case4(self):
        robot, factory, output = self.testCases[4]
        result = self.obj.minimumTotalDistance(robot = robot, factory = factory)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()