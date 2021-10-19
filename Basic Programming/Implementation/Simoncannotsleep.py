#MINUTE HAND - 3600 seconds - 60*60
#1 minute = 360/60 = 6 degree
#1 second = 6/60 = 0.1 degree

#HOUR HAND - 43200 seconds - 60*60*12
#1 hour = 360/12 = 30 degree
#1 minute = 30/60 = 0.5 degree
#1 second = 0.5/60 = 0.00833

input_hour, input_mint = map(int, input().split(":"))
input_seconds= (input_hour*60*60) + (input_mint*60)
i=0
count=0
while(i<input_seconds+1):
    hour_hand = i*0.008333333333333333
    minute_hand = (i*0.1)%360
    if round(hour_hand,1)==round(minute_hand,1):
        count=count+1
        i=i+2 #To skip very nearby overlapping seconds
    else:
        i=i+1

    #Reset the clock if it exceeds the 12 hours
    if i>43200:
        input_seconds=input_seconds-43200 
        i=0

print(count)