"""
银行卡中,原有存款:123.45元,向卡中存储5000元,余额是多少？又取走1000.45元,余额是多少？,每天存储125元,存储21天,余额是多少？每天花70元,可以花多少天？
"""
ck = 123.45           # ck --- 存储
yue1 = ck + 5000
print('余额1是:', yue1)

yue2 = yue1 - 1000.450
print('余额2是:', yue2)

yue3 = 125 * 21 + yue2
print('余额3是:', yue3)

day = yue3 // 70
print('可以花', day, '天')