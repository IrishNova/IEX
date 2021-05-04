import requests
import pandas as pd
# import cpi as cp

token = "" #place token here

tkr = input("Please enter stock symbol: ").upper()
z = int(input("Enter number of Quarters: "))



'''Balance Sheet'''
api_url = f'https://cloud.iexapis.com/stable/stock/{tkr}/balance-sheet/{z}?token={token}&period=quarter'
bal_data = requests.get(api_url).json()
bal_data = bal_T


'''Cash Flow'''
cf__url = f'https://cloud.iexapis.com/stable/stock/{tkr}/cash-flow/{z}?token={token}&period=quarter'
cf_data = requests.get(cf__url).json()
cf_data = cf_T


'''Income Statement'''
inc_url = f'https://cloud.iexapis.com/stable/stock/{tkr}/income/{z}?token={token}&period=quarter'
inc_data = requests.get(inc_url).json()
inc_data = inc_T


'''5 Year Price history'''
two_yr_url = f'https://cloud.iexapis.com/stable/stock/{tkr}/chart/5y?token={token}'
price_data_5y = requests.get(two_yr_url).json()
ddd = pd.DataFrame(data=price_T)
price_d_5y = ddd.set_index('date')


'''6. Close Only'''
cl_o = f'https://cloud.iexapis.com/stable/stock/{tkr}/chartCloseOnly/max?token={token}'
woww = requests.get(cl_o).json()




'''7. Ten Years of annual Income Statements'''
ttt = f'https://cloud.iexapis.com/stable/stock/{tkr}/income/11?token={token}&period=annual'
ten_year_income = requests.get(ttt).json()
ten_year_income = ten_inc_T



'''8. Annual CPI for 2010 to 2020'''
# cpi_data = []
# for i in range(11):
#     date = 2010 + i
#     temp = cp.get(date)
#     cpi_data.append(temp)
# cpi_data = cpi


'''9. Todays Price'''
ppp = f'https://cloud.iexapis.com/stable/stock/{tkr}/price/?token={token}'
price = requests.get(ppp).json()


'''10. Key Stats'''
qm1 = f'https://cloud.iexapis.com/stable/stock/{tkr}/stats/?token={token}'
key_stats = requests.get(qm1).json()


'''11. General Data'''
gd = f'https://cloud.iexapis.com/stable/stock/{tkr}/company/?token={token}'
general_data = requests.get(gd).json()



'''12. Peer Group'''
pg = f'https://cloud.iexapis.com/stable/stock/{tkr}/peers/?token={token}'
peer_group = requests.get(pg).json()
peer_group.append(tkr)


