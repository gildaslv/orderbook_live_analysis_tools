import ccxt.pro
import asyncio
import matplotlib.pyplot as plt
import numpy as np

async def main():
    plt.ion()
    fig=plt.figure()
    exchange = ccxt.pro.binance({'enableRateLimit': True})
    while True:
        orderbook = await exchange.watch_order_book('ETHUSDT')
        arr=np.vstack([orderbook['bids'][:600],orderbook['asks'][:600]])
        prices=np.around(arr[:,0])
        amounts=arr[:,1]
        pricesScale=np.unique(prices)
        final=np.array([(i,amounts[prices==i].sum())for i in pricesScale])
        prices=final[:,0]
        am=final[:,1]
        am=np.c_[am,am][::-1]
        plt.clf()
        plt.imshow(am,aspect='auto')
        size=round(orderbook['asks'][0][0])
        size=np.where(prices[::-1]==size)
        plt.hlines([size],*plt.xlim(),colors='red')
        yt=np.arange(len(prices))[::-1]
        plt.yticks(yt,labels=prices)
        plt.colorbar()
        fig.canvas.draw()
        fig.canvas.flush_events()

asyncio.get_event_loop().run_until_complete(main())