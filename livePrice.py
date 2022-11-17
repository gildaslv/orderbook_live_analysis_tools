import ccxt.pro
import asyncio
import matplotlib.pyplot as plt
import numpy as np

async def main():
    plt.ion()
    exchange = ccxt.pro.binance({'enableRateLimit': True})
    fig=plt.figure()
    price=np.zeros(200)
    while True:
        orderbook = await exchange.watch_order_book('ETHUSDT')
        price=np.append(price,orderbook['bids'][0][0])
        price=price[-200:]
        price[-200]=orderbook['bids'][0][0]-3
        price[-199]=orderbook['bids'][0][0]+3
        plt.clf()
        plt.plot(price)
        fig.canvas.draw()
        fig.canvas.flush_events()

asyncio.get_event_loop().run_until_complete(main())