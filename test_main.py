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


    def test_house_generation(self):
        self.assertRegex(main.houseGeneration(1), '^([A-Za-z0-9 ]+),([A-Za-z0-9 ]+),([0-9 ]+),([0-9 ]+),([0-9 ]+)$')

    def test_get_earnings(self):
        myLease = {self.lease_1, self.lease_2}
        myAirBNB = {self.airbnb_1, self.airbnb_2}
        house1_getquota = ((float(59023) * 0.05) - (float(59023 / 33)))
        house2_getquota = ((float(75114) * 0.05) - (float(75114 / 27)))
        house3_getquota = (float(52045 * 0.0025 * 30)) - (float(52045 / 39)) - float(663)
        house4_getquota = (float(68007 * 0.0025 * 30)) - (float(68007 / 42)) - float(751)
        #i tried adding them one by one
        manual_earnings = {}
        manual_earnings[0] = house1_getquota
        manual_earnings[1] = house2_getquota
        manual_earnings[2] = house3_getquota
        manual_earnings[3] = house4_getquota
        #i tried adding them all at once
        #manual_earnings = {house1_getquota, house2_getquota, house3_getquota, house4_getquota}
        boolean = main.getEarnings(myLease, myAirBNB) == manual_earnings
        self.assertTrue(boolean)
        #i tried assertEqual, assertTrue, but it keeps giving the same error.



"""
    def test_find_total_earnings(self):
        self.fail()

    def test_find_highest_earning(self):
        self.fail()

    def test_find_lowest_earning(self):
        self.fail()
"""


if __name__ == '__main__': #I have used this for ease of execution.
    unittest.main()
