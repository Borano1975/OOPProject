import abc
class Property:
    def __init__(self, name, location, price, loanMonths):
        self.name = name
        self.location = location
        self.price = price
        self.loanMonths = loanMonths
        self.mortgage = self.price / self.loanMonths

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setLoanMonths(self, loanMonths):
        self.loanMonths = loanMonths

    def getLoanMonths(self):
        return self.loanMonths

    def setMortgage(self):
        self.mortgage = self.price / self.mortgage

    def getMortgage(self):
        return self.price / self.mortgage

    @abc.abstractmethod
    def getQuota(self):
        return

class Lease(Property):
    def __init__(self, name, location, price, loanMonths, monthlyCare):
        super().__init__(name, location, price, loanMonths)
        self.monthlyCare = monthlyCare

    def getQuota(self):
        return (float(self.price)*0.05)-(float(self.mortgage))

class AirBNB(Property):
    def __init__(self, name, location, price, loanMonths, monthlyCare):
        super().__init__(name, location, price, loanMonths)
        self.monthlyCare = monthlyCare

    def getMonthlyCare(self):
        return self.monthlyCare

    def getQuota(self):
        return (float(self.price*0.0025*30))-(float(self.mortgage))-float(self.monthlyCare)
