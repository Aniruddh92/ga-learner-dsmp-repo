# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)

loan_status = data.Loan_Status.value_counts()
# loan_status.Y
plt.bar(loan_status.Y, loan_status.N)
plt.show()

#Code starts here


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()


data.groupby(['Property_Area', 'Loan_Status']).size().unstack().plot(kind='bar', width=0.25)

# plt.bar(property_and_loan)
# plt.xlabel = 'Property Area'
# plt.ylabel = 'Loan Status'
plt.xticks(rotation='45')

plt.show()



# --------------
#Code starts here

education_and_loan = data.groupby(['Education', 'Loan_Status'])
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()

data.groupby(['Education', 'Loan_Status']).size().unstack().plot(kind='bar', width=0.25,stacked=True)

plt.xlabel= "Education Status"
plt.ylabel = 'Loan Status'
plt.xticks(rotation='45')
plt.show()



# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
data.LoanAmount.plot(kind='density', label = 'Graduate')
plt.show
data.LoanAmount.plot(kind='density', label = 'Not Graduate')
plt.show()
















#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)

ax_1.scatter(data.ApplicantIncome, data.LoanAmount)
ax_1.title = 'Applicant Income'

ax_2.scatter(data.CoapplicantIncome, data.LoanAmount)
ax_2.title = 'Coapplicant Income'

data['TotalIncome'] = data.ApplicantIncome + data.CoapplicantIncome


ax_3.scatter(data.TotalIncome, data.LoanAmount)
ax_3.title = 'Total Income'

plt.show()


