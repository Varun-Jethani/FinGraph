#Libraries for ploting
import plotly.graph_objects as go
import yfinance as yf
import plotly.express as px
import plotly.io as pio
import datetime


def generate_graph(ticker):
    
    start_date = "2023-01-01"
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
    # yaxis_title=f"Price({info['currency']})",
    font=dict(
        family="Trebuchet MS, monospace",
        size=18,
        color="White"
    )
)
    html=fig.to_html(full_html= False, include_plotlyjs='cdn')
    
    #fig.write_html("graph.html",auto_open=True)
    return html



generate_graph("GOOGL")