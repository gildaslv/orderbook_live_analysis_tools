import ccxt.pro
import asyncio

async def main():
    import matplotlib.pyplot as plt
    import numpy as np
    
    # generating random data values
    x=np.linspace(1,100,100)
    y=np.linspace(.1,.9,100)
    y2=np.linspace(.1,.9,100)
    y3=np.linspace(.1,.9,100)
    y4=np.linspace(1250,1300,100)
    
    # enable interactive mode
    plt.ion()
    
    # creating subplot and figure
    fig=plt.figure()
    ax=fig.add_subplot(221)
    line1,=ax.plot(x,y,label='40')
    line2,=ax.plot(x,y2,label='250')
    line3,=ax.plot(x,y3,label='500')
    ax.legend(loc='upper left')
    ax2=fig.add_subplot(222)
    line4,=ax2.plot(x, y4)
    
    ax.set_xlabel('time')
    ax2.set_xlabel('time')
    ax.set_ylabel('50 last orderbook cells')
    ax2.set_ylabel('bid price')
    exchange = ccxt.pro.binance({'enableRateLimit': True})
    while True:
        orderbook = await exchange.watch_order_book('ETHUSDT')
        # print(orderbook['asks'][0], orderbook['bids'][0])
        bid=sum(x[1]for x in orderbook['bids'][:40])
        ask=sum(x[1]for x in orderbook['asks'][:40])
        y=np.append(y,bid/(bid+ask))
        y=y[-100:]
        bid=sum(x[1]for x in orderbook['bids'][:250])
        ask=sum(x[1]for x in orderbook['asks'][:250])
        y2=np.append(y2,bid/(bid+ask))
        y2=y2[-100:]
        bid=sum(x[1]for x in orderbook['bids'][:500])
        ask=sum(x[1]for x in orderbook['asks'][:500])
        y3=np.append(y3,bid/(bid+ask))
        y3=y3[-100:]
        y4=np.append(y4,orderbook['bids'][0][0])
        y4=y4[-100:]
        # updating the value of x and y
        line1.set_ydata(y)
        line2.set_ydata(y2)
        line3.set_ydata(y3)
        line4.set_ydata(y4)
        # re-drawing the figure
        fig.canvas.draw()
        # to flush the GUI events
        fig.canvas.flush_events()

asyncio.get_event_loop().run_until_complete(main())