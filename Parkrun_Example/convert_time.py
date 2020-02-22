time1 = "1:30:34"
time2="1:34:00"
time3= "23:45:00"
time4="22:34"
time5="1:00:00:00"

def convert_time(time):
    """Split the time in a list  of HOUR:MINUTES:SECONDS:HUNDREDTH"""
    split_time=time.split(":")
    # if the 0th item in the list is "1" then it's one hour
    if split_time[0] == "1":
        # replace the "1" by 3600 (of type int)
        split_time[0]=3600
        # the second value is in minutes. convert to int and multiply by 60
        split_time[1]=int(split_time[1])*60
        # the third value is seconds. just convert to int
        split_time[2]=int(split_time[2])
        # if there is a fourth value, delete it, it's hundredth'
        if len(split_time)>3:
            split_time.pop()

    else:
        split_time[0]=int(split_time[0])*60
        split_time[1]=int(split_time[1])
        # if there is a third value, delete it, it's hundredth'
        if len(split_time)>2:
            split_time.pop()

    # add all values in the list
    print(sum(split_time))

convert_time(time1)
convert_time(time2)
convert_time(time3)
convert_time(time4)
convert_time(time5)


