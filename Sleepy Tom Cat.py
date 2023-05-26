weekend=int(input())

days_play=365-weekend
owner_play_time=days_play*63+weekend*127
time_for_play=abs(30000-owner_play_time)
Hours=time_for_play//60
minutes=time_for_play%60
if 30000<owner_play_time:
    print('Tom will run away')
    print(f'{Hours} hours and {minutes} minutes more for play')

else:
   print('Tom sleeps well')
   print(f'{Hours} hours and {minutes} minutes less for play')