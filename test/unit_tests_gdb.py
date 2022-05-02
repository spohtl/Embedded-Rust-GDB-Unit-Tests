import gdb
import unittest

def gdb_execute_wrapper(s_method_to_call, s_parameters):
    # simple wrapper to call a method using gdb and return its return value. Probably doesn't work if the return object is more than a simple value
    return gdb.execute("print " + s_method_to_call+"(" + s_parameters + ")",to_string=True).split(" = ")[1].strip()

def gdb_execute_quiet(s_execute_command):
    # attempt to make gdb just be a little bit more quiet for once. Limited effect.
    s_result = gdb.execute(s_execute_command, to_string=True)

class SimpleUnitTests(unittest.TestCase):

    def setUp(self):
        gdb_execute_quiet("b main") # stop at main() before every test, to ensure everything is properly initialized
        gdb_execute_quiet("c")

    def tearDown(self):
        gdb_execute_quiet("d")
        gdb_execute_quiet("b Reset")
        gdb_execute_quiet("j Reset") # reset the target after every test, to ensure a clean state for the next test

    def test_5_is_prime(self):
        s_return_value = gdb_execute_wrapper("is_prime","5")
        self.assertEqual(s_return_value, 'true')

    def test_1_is_not_prime(self):
        s_return_value = gdb_execute_wrapper("is_prime","1")
        self.assertEqual(s_return_value, 'false')

gdb_execute_quiet("target remote :3333")

try:
    unittest.main()
except:
    gdb_execute_quiet("monitor q")
    sys.exit(1) # to indicate to GotHub Actions that a CI step failed

gdb_execute_quiet("monitor q") # exit QEMU just in case it gets stuck in some loop
gdb_execute_quiet("q")
