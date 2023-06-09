import pandas as pd

market_prices_df = pd.read_excel('./market-prices-dairy-products(1).xlsx', sheet_name='market-prices-dairy-products')

france_dairy_products = market_prices_df[market_prices_df['Category']=='Dairy Products'][market_prices_df['Country']=='FR']
print("\n---------------------")
print("1) Printing diary products price for France : ")
print(france_dairy_products)

productDesc_MP = france_dairy_products[['Product desc', 'MP Market Price']]
print("\n---------------------")
print("2) Printing Product desc and MP Market price for all France Dairy Product records :")
print(productDesc_MP)

print("\n---------------------")
rounded_productDesc_MP = productDesc_MP
rounded_productDesc_MP.loc[:, 'MP Market Price'] = rounded_productDesc_MP['MP Market Price'].round(2)
print("3) Rounding off MP Market Price column values :")
print(rounded_productDesc_MP)

print("\n---------------------")
print("4) Pivot table for MP Market Price per Product desc : ")
pivot_table = market_prices_df.pivot_table(values='MP Market Price', index='Product desc', columns=[] ,aggfunc=lambda x: round(x.mean(), 2))
print(pivot_table)

print("\n---------------------")
pivot_table.to_excel("pivot_table.xlsx")
print("5) Pivot table exported to pivot_table.xlsx")