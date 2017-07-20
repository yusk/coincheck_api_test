from pprint import pprint
from coincheck import market
import time
import matplotlib.pyplot as plt

asks = []
m1 = market.Market()
i = 0
while True:
    res = m1.ticker()
    pprint(res)
    asks.append(res['ask'])
    if i > 10:
        break
    i += 1
    time.sleep(1)
plt.plot(asks)
plt.show()
