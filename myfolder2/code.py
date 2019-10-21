# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df.fico>700].index)/len(df.index)
p_b = len(df[df.purpose=='debt_consolidation'].index)/len(df.index)
# print(len(df[df.purpose=='debt_consolation'].index))
df1 = df[df.purpose=='debt_consolidation']


p_a_b = len(df[(df.fico>700) & (df.purpose=='debt_consolation')].index)/len(df.index)*(1/p_b)

result = p_a_b == p_a

print(result)




# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes'].index)/len(df.index)
prob_cs = len(df[df['credit.policy'] == 'Yes'].index)/len(df.index)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(df[(df['paid.back.loan'] == 'Yes') & (df['credit.policy'] == 'Yes')].index)/len(df.index)*(1/prob_lp)

# print(prob_pd_cs)

bayes = prob_pd_cs*prob_lp/prob_cs
print(bayes)




# code ends here


# --------------
# code starts here
plt.bar(df.purpose.value_counts().index,df.purpose.value_counts())
plt.xticks(rotation = '45')

plt.show()


df1 = df[df['paid.back.loan'] == 'No']
plt.bar(df1.purpose.value_counts().index, df1.purpose.value_counts())

plt.xticks(rotation = '45')
plt.show()

# code ends here


# --------------
# code starts here
inst_median = df.installment.median()
inst_mean = df.installment.mean()

plt.hist(df.installment)
plt.show()

plt.hist(df['log.annual.inc'])
plt.show()




# code ends here


