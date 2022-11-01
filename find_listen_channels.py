import csv

listen_today = open('listen_today.csv', 'r')
l_today = csv.reader(listen_today)

l_today = list(l_today)
ll = list((i[0] for i in l_today))
listen_channels = open('l_chan .csv', 'r')
l_channels = csv.reader(listen_channels)
with open('res.csv', 'w') as file:
    f=csv.writer(file)
    cnt = 0
    for l_c in l_channels:
        flag = 0
        ch = l_c[0].lstrip('https://t.me/')
        # print(ch)
        if ch in ll:
            l_c[1] = '27 окт'
    
        f.writerow(l_c)

listen_channels.close()
listen_today.close()

print(cnt)
print()
def t():
    print('t')
    return 1
