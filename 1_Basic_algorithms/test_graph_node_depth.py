import unittest
from graph_node_depth import *

class MyFirstTests(unittest.TestCase):

    testData = [
        {'graph': [[0,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]], 'parent': 0, 'node': 4, 'result': 3},
        {'graph': [[0,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]], 'parent': 0, 'node': 3, 'result': 2},
        {'graph': [[0,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]], 'parent': 0, 'node': 2, 'result': 1},
        {'graph': [[0,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]], 'parent': 0, 'node': 1, 'result': 1},
        {'graph': [[0,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]], 'parent': 2, 'node': 4, 'result': 2},
        {'graph': [[0,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]], 'parent': 2, 'node': 3, 'result': 1},
        {'graph': [[0,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]], 'parent': 1, 'node': 4, 'result': -1}
    ]

    def test_node_depth(self):
        for test in self.testData:
            print('Graph:')
            for i in test['graph']:
                print(','.join(map(str, i)))
            print('Parent node index: ', test['parent'])
            print('Desired node index: ', test['node'])
            print('Expected result: ', test['result'])
            print('____')    
            self.assertEqual(get_depth(test['graph'], test['parent'], test['node']), test['result'])

if __name__ == '__main__':
    unittest.main()