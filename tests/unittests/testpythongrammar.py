import unittest


class TestPythonGrammar(unittest.TestCase):
    
    def test_python_set_get_delete(self):
        d = {}
        d['foo'] = 'bar'
        self.assertIn('foo', d)
        self.assertEquals(d['foo'], 'bar')
        del d['foo']
        self.assertNotIn('foo', d)
