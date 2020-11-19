import unittest
from Classes import Property
from Classes import Lease
from Classes import AirBNB


class TestProperty(unittest.TestCase):
    def setUp(self):
        self.property_1 = Property("House 1", "Street 1", 62638, 96)
        self.property_2 = Property("House 2", "Street 2", 56697, 37)

    def test_getMortgage(self):
        self.assertEqual(self.property_1.getMortgage(), 62638/96)
        self.assertEqual(self.property_1.getMortgage(), self.property_1.price/self.property_1.loanMonths)
        self.assertEqual(self.property_2.getMortgage(), 56697/37)
        self.assertEqual(self.property_2.getMortgage(), self.property_2.price / self.property_2.loanMonths)

class TestLeaseAirBNB(unittest.TestCase):
    def setUp(self):
        self.lease_1 = Lease("House 1", "Street 1", 59023, 33, 0)
        self.lease_2 = Lease("House 2", "Street 2", 75114, 27, 0)
        self.airbnb_1 = AirBNB("House 1", "Street 1", 52045, 39, 663)
        self.airbnb_2 = AirBNB("House 2", "Street 2", 68007, 42, 751)

    def test_getMortgage(self):
        self.assertEqual(self.lease_1.getMortgage(), 59023/33)
        self.assertEqual(self.lease_1.getMortgage(), self.lease_1.price / self.lease_1.loanMonths)
        self.assertEqual(self.lease_2.getMortgage(), 75114/27)
        self.assertEqual(self.lease_2.getMortgage(), self.lease_2.price / self.lease_2.loanMonths)

    def test_getQuota(self):
        lease_quota_1 = (float(self.lease_1.getPrice())*0.05) - (float(self.lease_1.getMortgage()))
        self.assertEqual(self.lease_1.getQuota(), ((float(59023) * 0.05) - (float(59023 / 33))))
        self.assertEqual(self.lease_1.getQuota(), lease_quota_1)

        lease_quota_2 = (float(self.lease_2.getPrice()) * 0.05) - (float(self.lease_2.getMortgage()))
        self.assertEqual(self.lease_2.getQuota(), ((float(75114) * 0.05) - (float(75114 / 27))))
        self.assertEqual(self.lease_2.getQuota(), lease_quota_2)

        airbnb_quota_1 = (float(self.airbnb_1.getPrice()*0.0025*30))-(float(self.airbnb_1.getMortgage()))-float(self.airbnb_1.getMonthlyCare())
        self.assertEqual(self.airbnb_1.getQuota(), (float(52045 * 0.0025 * 30)) - (float(52045 / 39)) - float(663))
        self.assertEqual(self.airbnb_1.getQuota(), airbnb_quota_1)

        airbnb_quota_2 = (float(self.airbnb_2.getPrice() * 0.0025 * 30)) - (float(self.airbnb_2.getMortgage())) - float(self.airbnb_2.getMonthlyCare())
        self.assertEqual(self.airbnb_2.getQuota(), (float(68007 * 0.0025 * 30)) - (float(68007 / 42)) - float(751))
        self.assertEqual(self.airbnb_2.getQuota(), airbnb_quota_2)

if __name__ == '__main__': #I have used this for ease of execution.
    unittest.main()
