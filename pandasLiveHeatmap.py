import ccxt.pro
import asyncio
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

async def main():
    plt.ion()
    fig=plt.figure()
    exchange = ccxt.pro.binance({'enableRateLimit': True})
    while True:
        orderbook = await exchange.watch_order_book('ETHUSDT')
        asks=pd.DataFrame(orderbook['asks'])
        bids=pd.DataFrame(orderbook['bids'])
        bids=bids.iloc[:600,:]
        asks=asks.iloc[:600,:]
        df=bids.append(asks)
        df.columns=['price','amount']
        df['price']=round(df['price'])
        df=df.groupby('price').sum()
        plt.clf()
        df=df.iloc[::-1]
        sns.heatmap(df,cmap='YlGnBu')
        fig.canvas.draw()
        fig.canvas.flush_events()

asyncio.get_event_loop().run_until_complete(main())
