"""
LAB3
CPE 202
John Wright
"""
import unittest
from queues import QueueArray, QueueLinked

class TestCase(unittest.TestCase):

   def test_QueueArray(self):
      queue = QueueArray(4)
      for i in range(4):
         queue.enqueue(i)
      self.assertFalse(queue.is_empty())
      self.assertTrue(queue.is_full())
      for i in range(4):
         v = queue.dequeue()
         self.assertEqual(v,i)
      self.assertTrue(queue.is_empty())
      self.assertFalse(queue.is_full())


   def test_QueueLinked(self):
      queue = QueueLinked(4)
      for i in range(4):
         queue.enqueue(i)
      self.assertFalse(queue.is_empty())
      self.assertTrue(queue.is_full())
      for i in range(4):
         v = queue.dequeue()
         self.assertEqual(v, i)
      self.assertTrue(queue.is_empty())
      self.assertFalse(queue.is_full())

if __name__ == '__main__':
   # execute main() function
   unittest.main()
