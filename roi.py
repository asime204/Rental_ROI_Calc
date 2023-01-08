# Automated Rental Property Calculator

class RentalProperty:
    def __init__(self, mortgage, rental_income, amenities_income, taxes, insurance, utilities, hoa, lawn, vacancy, repairs, capex, property_management, down_payment, closing_costs, rehab_budget, misc):
        self.mortgage = mortgage
        self.rental_income = rental_income
        self.amenities_income = amenities_income
        self.taxes = taxes
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawn = lawn
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.property_management = property_management
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc = misc

# function 1 - Income
# rental income
# laundry/storage/misc
# total income = sum of all incomes
    def income(self):
        return self.rental_income + self.amenities_income + self.utilities

# function 2 - Expenses
# taxes
# insurance
# ulitilies - water/electric/sewer/garbage/gas
# HOA
# Lawn/Snow
# Vacancy
# Repairs
# capex(fund for replacements)
# property management
# Mortgage
# total expenses = sum of all expenses
    def expenses(self):
        return self.taxes + self.insurance + self.hoa + self.lawn + self.vacancy + self.repairs + self.capex + self.property_management + self.mortgage

# funtion 3 - Cash Flow
# total income - total expenses = total monthly cash
    def cash_flow(self):
        return self.income() - self.expenses()

# function 4 - Cash on Cash ROI - return of cash flow
# down paymanet
# closing cost
# rehab budget
# misc/other
# total investment
    def roi(self):
        annual_cash_flow = (self.cash_flow() * 12)
        total_investment = self.down_payment + self.closing_costs + self.rehab_budget + self.misc
        return (annual_cash_flow / total_investment)

# total monthly cash X 12 months = annual cashflow
# cash on cash = annual cash/total investment

# ROI should return = cash on cash percentage

rental_income = float(input("Enter rental income: "))
amenities_income = float(input("Enter income from amenities (laundry/storage/misc): "))
utilities = float(
    input("Enter total costs for tenent (water/electric/sewer/garbage/gas): "))
taxes = float(input("Enter taxes charged: "))
insurance = float(input("Enter insurance charged: "))
hoa = float(input("Enter HOA cost: "))
lawn = float(input("Enter lawn cost: "))
vacancy = float(input("Enter vacancy cost: "))
repairs = float(input("Enter repairs cost: "))
capex = float(input("Enter capex funds (replacements): "))
property_management = float(input("Enter property management cost: "))
mortgage = float(input("Enter monthly mortgage: "))
down_payment = float(input("Enter down payment: "))
closing_costs = float(input("Enter closing costs: "))
rehab_budget =float(input("Enter rehab budget: "))
misc = float(input("Enter misc/other: "))

property = RentalProperty(mortgage, rental_income, amenities_income, taxes, insurance, utilities, hoa,
                          lawn, vacancy, repairs, capex, property_management, down_payment, closing_costs, rehab_budget, misc)
roi = property.roi()
roi_percent = float(roi * 100)


print(f"Total income: {property.income()}")
print(f"Total expenses: {property.expenses()}")
print(f"Total cash flow: {property.cash_flow()}")
print(f"ROI: {property.roi()}")
print(f"ROI Annual Percentage: {roi_percent}%")