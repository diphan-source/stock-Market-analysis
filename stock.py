import pandas as pd
import yfinance as yf
import plotly.io as pio
import plotly.graph_objects as go 
pio.templates.default = "plotly_white"

# define the ticker for Apple and Google
Apple_ticker = "AAPL"
Google_ticker = "GOOGL"

# define the date range for the last quarter
start_date = "2023-07-01"
end_date = "2023-11-30"

# fetch historical stock price data using yFinance
apple_data = yf.download(Apple_ticker, start=start_date, end=end_date)
google_data = yf.download(Google_ticker, start=start_date, end=end_date)

#calculate the daily return for each stock
apple_data["Daily Return"] = apple_data["Adj Close"].pct_change()
google_data["Daily Return"] = google_data["Adj Close"].pct_change()

# visualize the daily returns
fig = go.Figure()
fig.add_trace(go.Scatter(x=apple_data.index, y=apple_data["Daily Return"], name=Apple_ticker))
fig.add_trace(go.Scatter(x=google_data.index, y=google_data["Daily Return"], name=Google_ticker))
fig.update_layout(title="Daily Returns", xaxis_title="Date", yaxis_title="Daily Return")
# fig.show()

# save the figure as html file
fig.write_html("daily_returns.html")