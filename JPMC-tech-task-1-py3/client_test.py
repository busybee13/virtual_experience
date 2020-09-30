import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    outputs= [
      ('ABC', 120.48, 121.2, (120.48+121.2)/2),
      ('DEF', 117.87, 121.68, (117.87+121.68)/2)
    ]
    for quote, output in zip(quotes, outputs):
        self.assertEqual(getDataPoint(quote), output)
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    outputs= [
      ('ABC', 120.48, 119.2, (120.48+ 119.2)/2),
      ('DEF', 117.87, 121.68, (117.87+121.68)/2)
    ]
    for quote, output in zip(quotes, outputs):
        self.assertEqual(getDataPoint(quote), output)

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_calculatePriceEdgeValues(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 0.1, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'GHI'}
    ]
    """ ------------ Add the assertion below ------------ """
    outputs= [
      ('ABC', 0, 119.2, (0+ 119.2)/2),
      ('DEF', 117.87, 0, (117.87+0)/2),
      ('GHI', -117.87, 0.1, (-117.87+0.1)/2)
    ]
    for quote, output in zip(quotes, outputs):
        self.assertEqual(getDataPoint(quote), output)

if __name__ == '__main__':
    unittest.main()
