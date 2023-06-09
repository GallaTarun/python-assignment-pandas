import pandas as pd

market_prices_df = pd.read_excel('./market-prices-dairy-products(1).xlsx', sheet_name='market-prices-dairy-products')

print(f"Printing diary products price for France = {market_prices_df[market_prices_df['Category']=='Dairy Products'][market_prices_df['Country']=='FR']['MP Market Price'].mean()}")