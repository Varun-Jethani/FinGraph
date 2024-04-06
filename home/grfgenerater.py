#Libraries for ploting
import plotly.graph_objects as go
import yfinance as yf
import datetime

def generate_graph(ticker):
    
    start_date = "2024-01-01"
    ed=datetime.date.today()
    yf.pdr_override()
    df = yf.download(ticker, start=start_date, end=ed)
    tick = yf.Ticker(ticker)
    

    fig=go.Figure(data=[go.Candlestick(x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'])])
    info = tick.info
    fig.update_layout(
    template= "plotly_dark",
    title=f"{info['shortName']} Stock ",
    xaxis_title="Date",
    font=dict(
        family="Trebuchet MS, monospace",
        size=18,
        color="White"
    )
)
    html=fig.to_html(full_html= False, include_plotlyjs='cdn')
    
    
    return html



