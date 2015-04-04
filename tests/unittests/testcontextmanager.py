import os
import unittest
import tempfile
import contextmanager


class TestLPNYCContextManager(unittest.TestCase):
    
    def test_contextmanager_context_suppress_fails(self):
        with contextmanager.ContextSuppressFails() as cm:
            raise RuntimeError('this error will be suppressed')
        
    def test_contextmanager_context_reraises(self):
        with self.assertRaises(RuntimeError):
            with contextmanager.ContextPassesFails() as cm:
                raise RuntimeError('this error expected')


class TestBuiltinContextManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.integer, cls.tmpfilepath = tempfile.mkstemp()

    def test_that_builtin_open_fails(self):
        fileobj = open(self.tmpfilepath, 'r')
        try:
            with self.assertRaises(IOError):
                fileobj.write('this should raise an error')
        finally:
            fileobj.close()
    
    def test_open_context_manager(self):
        try:
            with open(self.tmpfilepath, 'r') as fileobj:
            # about same as fileobj = open(self.tmpfilepath); with fileobj: 
                fileobj.write('this should also raise an IOError')
                tested = None # this line shouldn't execute if error
        except IOError:
            pass
        with self.assertRaises(NameError):
            tested
        self.assertTrue(fileobj.closed)     
        
    @classmethod
    def tearDownClass(cls):
        os.remove(cls.tmpfilepath)


if __name__ == '__main__':
    unittest.main(verbosity=2)
