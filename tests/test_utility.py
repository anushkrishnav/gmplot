import unittest
from gmplot.utility import StringIO, _get_options

class StringIOTest(unittest.TestCase):
    def test_enter_exit(self):
        with StringIO() as f:
            f.write('Content')
            self.assertEqual(f.getvalue(), 'Content')

        self.assertTrue(f.closed) 

class UtilityTest(unittest.TestCase):
    def test_get_options(self):
        parameters = {
            'c': 'orange',
            'label': 'Point of interest'
        }

        options = _get_options(parameters, {
            'color': (['color', 'c'], 'red'),
            'title': (['title'],),
            'label': (['label'],),
            'draggable': (['draggable'], False)
        })

        EXPECTED_OUTPUT = {
            'color': '#FFA500',
            'label': 'Point of interest',
            'draggable': False
        }

        self.assertEqual(options, EXPECTED_OUTPUT)
