from converter.tests import *

import unittest

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('tests', pattern='*tests.py')
    unittest.TextTestRunner().run(all_tests)
