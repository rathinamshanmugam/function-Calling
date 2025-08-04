import yfinance as yf

def get_stock_price(ticker):
    t = yf.Ticker(ticker)
    price = t.history(period="1d")["Close"].iloc[-1]
    return {"ticker": ticker, "price": round(price, 2)}
