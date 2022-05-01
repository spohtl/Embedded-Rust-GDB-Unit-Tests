import gdb
import unittest

def gdb_execute_wrapper(s_method_to_call, s_parameters):
    return gdb.execute("print " + s_method_to_call+"(" + s_parameters + ")",to_string=True).split(" = ")[1].strip()

class SimpleUnitTests(unittest.TestCase):

    def setUp(self):
        gdb.execute("b main")
        gdb.execute("c")

    def tearDown(self):
        gdb.execute("d")
        gdb.execute("b Reset")
        gdb.execute("j Reset")

    def test_5_is_prime(self):
        s_return_value = gdb_execute_wrapper("is_prime","5")
        self.assertEqual(s_return_value, 'true')

    def test_1_is_not_prime(self):
        s_return_value = gdb_execute_wrapper("is_prime","1")
        self.assertEqual(s_return_value, 'false')

gdb.execute("target remote :3333")

try:
    unittest.main()
except:
    gdb.execute("monitor q")
    gdb.execute("q")

gdb.execute("monitor q")
gdb.execute("q")