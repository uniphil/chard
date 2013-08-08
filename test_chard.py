import unittest
import chard


class TestBlah(unittest.TestCase):

    def test_empty(self):
        docs = ({},)
        schema = chard.get_schema(docs)
        self.assertEqual(schema[0], 1.0)

    def test_multi_empty(self):
        docs = ({} for n in range(10))
        schema = chard.get_schema(docs)
        self.assertEqual(schema[0], 1.0)

    def test_simple(self):
        doc1 = {'a': 1}
        doc2 = {'a': 'b'}
        schema = chard.get_schema((doc1, doc1, doc1, doc2))
        self.assertEqual(schema[0], 0.75)
        self.assertEqual(schema[1]['a'], int)
