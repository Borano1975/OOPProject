import unittest
import main
from Classes import Lease
from Classes import AirBNB


class Test(unittest.TestCase):
    def setUp(self):

        self.lease_1 = Lease("House 1", "Street 1", 59023, 33, 0)
        self.lease_2 = Lease("House 2", "Street 2", 75114, 27, 0)
        self.airbnb_1 = AirBNB("House 1", "Street 1", 52045, 39, 663)
        self.airbnb_2 = AirBNB("House 2", "Street 2", 68007, 42, 751)
        self.house1_getquota = ((float(59023) * 0.05) - (float(59023 / 33)))
        self.house2_getquota = ((float(75114) * 0.05) - (float(75114 / 27)))
        self.house3_getquota = (float(52045 * 0.0025 * 30)) - (float(52045 / 39)) - float(663)
        self.house4_getquota = (float(68007 * 0.0025 * 30)) - (float(68007 / 42)) - float(751)
        self.total_earnings = {0: self.house1_getquota,
                               1: self.house2_getquota,
                               2: self.house3_getquota,
                               3: self.house4_getquota}
        self.myLease = {0: self.lease_1, 1: self.lease_2}
        self.myAirBNB = {0: self.airbnb_1, 1: self.airbnb_2}

        self.total_earnings_addition = int(self.house1_getquota + self.house2_getquota + self.house3_getquota + self.house4_getquota)

    def test_house_generation(self):
        self.assertRegex(main.houseGeneration(1), '^([A-Za-z0-9 ]+),([A-Za-z0-9 ]+),([0-9 ]+),([0-9 ]+),([0-9 ]+)$')

    def test_find_total_earnings(self):
        self.assertEqual(main.findTotalEarnings(self.total_earnings), self.total_earnings_addition)

    def test_get_earnings(self):

        self.assertEqual(main.getEarnings(self.myLease, self.myAirBNB), self.total_earnings)

    def test_find_highest_earning(self):
        self.assertEqual(main.findHighestEarning(self.total_earnings), int(self.house4_getquota))

    def test_find_lowest_earning(self):
        self.assertEqual(main.findLowestEarning(self.total_earnings), int(self.house1_getquota))


if __name__ == '__main__': #I have used this for ease of execution.
    unittest.main()
