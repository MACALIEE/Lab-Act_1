import matplotlib.pyplot as plt

years = [1988, 1989, 1990, 1991, 1992, 1993, 1994]
sales = [127, 130, 136, 145, 158, 178, 211]

plt.plot(years, sales, ls='-', color='g', marker='o')

plt.xlabel('Year')
plt.ylabel('Sales ($M)')
plt.title('Yearly Sales from 1988 to 1994')

plt.show()