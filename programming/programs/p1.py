speed=int(input('enter the speed'))
dof=bool(input('enter true if it is u r b_day else leave empty'))
inc=0
if dof:
    inc=5
if speed<60+inc:
    print('50')
elif speed<80+inc:
    print('500')
else:
    print('5000')