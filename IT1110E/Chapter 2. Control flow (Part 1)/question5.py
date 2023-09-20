t = float(input())
hours = float(input())

if t == 1: #car
    if hours <= 3:
        print('%.2f' % (hours*0.70))
    else:
        print('%.2f' % (3*0.70 + (hours - 3)*2.50))
elif t == 2: #bus
    if hours <= 3:
        print('%.2f' % (hours*1.50))
    else:
        print('%.2f' % (3*1.50 + (hours - 3)*2.00))
elif t == 3: #truck
    if hours <= 2:
        print('%.2f' % (hours*1.50))
    else:
        print('%.2f' % (2*2.50 + (hours - 2)*3.25))