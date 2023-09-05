class Income():

    def __init__(self):
        self.incomeTotal = 0
        self.rentalIncome = 0
        self.laundry = 0
        self.storage = 0
        self.misc = 0
        
    def setRentalIncome(self):
        income = input("Enter your rental income.")
        self.rentalIncome = float(income)

    def setLaundryIncome(self):
        income = input("Enter your laundry income.")
        self.laundry = float(income)

    def setStorageIncome(self):
        income = input("Enter your storage income.")
        self.storage = float(income)
    
    def setMiscIncome(self):
        income = input("Enter your miscellaneous income.")
        self.misc = float(income)

    def calculateIncome(self):
        print("Lets calculate your income.")
        self.setRentalIncome()
        self.setLaundryIncome()
        self.setStorageIncome()
        self.setMiscIncome()
        for values in vars(self).values():
            self.incomeTotal += values

    def getIncome(self):
        return self.incomeTotal
    
class Expenses():

    def __init__(self):
        self.totalExpenses = 0
        self.tax = 0
        self.insurance = 0
        self.utilities = 0
        self.hoa = 0
        self.lawn = 0
        self.vacancy = 0
        self.repairs = 0
        self.capEx = 0
        self.propManage = 0
        self.mortgage = 0
        
    def setTaxExpense(self):
        expense = input("Enter tax expenses")
        self.tax = float(expense)

    def setInsuranceExpense(self):
        expense = input("Enter insurance expenses")
        self.insurance = float(expense)

    def setUtilityExpense(self):
        expenses = input("Enter utility expenses")
        self.utilities = float(expenses)

    def setHoaExpense(self):
        expenses = input("Enter HOA expenses")
        self.utilities = float(expenses)

    def setLawnExpense(self):
        expenses = input("Enter lawn expenses")
        self.lawn = float(expenses)

    def setVacancyExpense(self):
        expenses = input("Enter vacancy expenses")
        self.vacancy = float(expenses)

    def setRepairsExpense(self):
        expenses = input("Enter repair expenses")
        self.repairs = float(expenses)

    def setCapExpense(self):
        expenses = input("Enter Capital expenses")
        self.capEx = float(expenses)

    def setManageExpense(self):
        expenses = input("Enter property management expenses")
        self.utilities = float(expenses)

    def setMortgageExpense(self):
        expenses = input("Enter mortgage expenses")
        self.mortgage = float(expenses)
    
    def calculateExpenses(self):
        print("Now, lets calculate your expenses.")
        self.setTaxExpense()
        self.setInsuranceExpense()
        self.setMortgageExpense()
        self.setRepairsExpense()
        self.setUtilityExpense()
        self.setVacancyExpense()
        self.setCapExpense()
        self.setHoaExpense()
        self.setLawnExpense()
        self.setManageExpense()
        for values in vars(self).values():
            self.totalExpenses += values

    def getExpenses(self):
        return self.totalExpenses
    

    
class CashFlow():

    def __init__(self, income, expenses):
        self.cashFlow = income-expenses
    
    def getFlow(self):
        return self.cashFlow
    
    def getAnnualFlow(self):
        return self.cashFlow*12
    
class ROI():

    def __init__(self):
        self.cocROI = 0
        self.investment = 0
        self.downPay = 0
        self.closingCosts = 0
        self.rehab = 0
        self.misc = 0

    def setDownPay(self):
        money = input("Enter your down payment.")
        self.downPay = float(money)

    def setClosingCosts(self):
        money = input("Enter your closing costs payment.")
        self.closingCosts = float(money)

    def setRehab(self):
        money = input("Enter your rehab payment.")
        self.rehab = float(money)
    
    def setMisc(self):
        money = input("Enter your miscellaneous payment.")
        self.misc = float(money)

    def calcROI(self):
        income = Income()
        income.calculateIncome()
        expenses = Expenses()
        expenses.calculateExpenses()
        cashFlow = CashFlow(income.getIncome(), expenses.getExpenses())
        
        print("Finally, lets calculate your cash on cash ROI")

        self.setDownPay()
        self.setClosingCosts()
        self.setRehab()
        self.setMisc()

        for values in vars(self).values():
            self.investment += values
    
        self.cocROI = round((cashFlow.getAnnualFlow()/self.investment)*100,2)
    
    def getCoCROI(self):
        print(f"Here is your cash on cash ROI: {self.cocROI}%")
    
roi = ROI()
roi.calcROI()
roi.getCoCROI()
