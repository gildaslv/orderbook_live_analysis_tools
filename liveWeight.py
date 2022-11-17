import ccxt.pro
import asyncio
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

async def main():
    plt.ion()
    fig = plt.figure()
    exchange = ccxt.pro.binance({'enableRateLimit': True})
    while True:
        orderbook = await exchange.watch_order_book('ETHUSDT')
        asks=pd.DataFrame(orderbook['asks'])
        bids=pd.DataFrame(orderbook['bids'])
        bids=bids.iloc[:600,:]
        asks=asks.iloc[:600,:]
        bids.columns=['price','quantity']
        bids['price']=round(bids['price'])
        bids=bids.groupby('price').sum()
        asks.columns=['price','quantity']
        asks['price']=round(asks['price'])
        asks=asks.groupby('price').sum()
        plt.clf()
        sns.ecdfplot(x="price", weights="quantity",stat='count', complementary=True,data=bids)
        sns.ecdfplot(x="price", weights="quantity",stat='count', data=asks)
        fig.canvas.draw()
        fig.canvas.flush_events()

asyncio.get_event_loop().run_until_complete(main())