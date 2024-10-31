import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker for gold futures
gold_ticker = 'GC=F'

# Download historical data for gold
data = yf.download(gold_ticker, period="5y")  # Adjust the period as needed

# Extract the adjusted closing price
gold_price = data['Adj Close']

# Plot the gold price fluctuations
plt.figure(figsize=(14, 7))
plt.plot(gold_price.index, gold_price, label='Gold Price', color='gold')

plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price (USD)')
plt.title('Fluctuations of Gold Price in the U.S. Market')
plt.legend()
plt.grid(True)
plt.show()
