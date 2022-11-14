import ccxt.pro
import asyncio
import time

async def main():
    import matplotlib.pyplot as plt
    import numpy as np
    import time
    
    # generating random data values
    x = np.linspace(1, 100, 100)
    y = np.linspace(.493,.507,100)
    y2 = np.linspace(1200,1300,100)
    
    # enable interactive mode
    plt.ion()
    
    # creating subplot and figure
    fig = plt.figure()
    ax = fig.add_subplot(221)
    line1, = ax.plot(x, y)
    ax2 = fig.add_subplot(223)
    line2, = ax2.plot(x, y2)
    
    # setting labels
    plt.xlabel("time")
    exchange = ccxt.pro.binance({'enableRateLimit': True})
    while True:
        orderbook = await exchange.watch_order_book('ETHUSDT')
        # print(orderbook['asks'][0], orderbook['bids'][0])
        bid=sum(orderbook['bids'][:500][1])
        y=np.append(y,bid/(bid+sum(orderbook['asks'][:500][1])))
        y=y[-100:]
        y2=np.append(y2,orderbook['bids'][0][0])
        y2=y2[-100:]
        # updating the value of x and y
        line1.set_ydata(y)
        line2.set_ydata(y2)
        # re-drawing the figure
        fig.canvas.draw()
        # to flush the GUI events
        fig.canvas.flush_events()

asyncio.get_event_loop().run_until_complete(main())