# Rental_ROI_Calc
Automated Rental Property Calculator

This program calculates the return on investment (ROI) for a rental property based on various income and expense factors. It allows users to input their own data and see the resulting ROI as a percentage.

DESIGN AND IMPLEMENTATION

To design and implement this program, I followed these steps:

I created a class called RentalProperty to represent a rental property.
I defined the __init__ method to initialize the attributes of a RentalProperty object (e.g. total price, rental income, taxes, etc.).
I defined four methods in the RentalProperty class: income, expenses, cash_flow, and roi. These methods calculate the total income, total expenses, total cash flow, and ROI for the property, respectively.
I created an instance of the RentalProperty class and prompted the user to input the necessary data.
I called the appropriate method to calculate the ROI for the property and displayed the result to the user.

ADDITIONAL FEATURES

I also added the ability to input and calculate the income from laundry/storage/misc sources, as well as the cost of utilities, HOA fees, lawn care, vacancy, repairs, capex, property management, and closing costs. These additional data points provide a more accurate representation of the income and expenses for the property.

RUNNING THE PROGRAM

To run this program, you will need Python 3 installed on your machine. No additional dependencies are required.

To use the program, simply enter the requested data when prompted and the ROI will be calculated and displayed as a percentage.