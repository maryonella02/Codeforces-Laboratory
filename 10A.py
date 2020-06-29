"""Power Consumption Calculation
We have n periods of time when someones work at the laptop from start time and end time.
And p1 power consumption fo active mode, p2 power consumption for eco mode, p3 power consumption for sleep mode.
 And t1 is time after someone left laptop but it is still active.
 and t2 time is time period when sleep mode is on, so time interval between eco mode is on and sleep mode is on."""
n, p1, p2, p3, t1, t2 = map(int, input().split()) # take the input
ans = 0
previous = -1 # will be the value of last end value from periods

while n > 0: # for n periods of time
    n -= 1
    start, end = map(int, input().split()) # take the time period
    ans += (end - start) * p1 # this was an active period so we multiply to p1 and add to answer
    if previous != -1: # here we find if we have  one more n period
        x = start - previous # find time when no one worked at the laptop
        if x > t1: # if x is bigger this means that t1 time laptop was active
            ans += t1 * p1 # and we add this time to answer
            x -= t1 # here we find the remaining time
            if x > t2: #if remaining time is bigger than t2, this means that laptop go to eco mode
                ans += t2 * p2 # add power laptop spend on eco mode to answer
                x -= t2# from remaining time we exclude the previous period t2
                ans += x * p3 # the remaining time is multiplied to power laptop spend in sleep mode, because here is no time limit
            else: # if remaining time is smaller than t2, this means that x is period of time that need to be multiplied to p2
                ans += x * p2 # this is computed and added to answer
        else:# if x is smaller than t1 period, this means that x includes in time laptop is still active, but nobody works at him
            ans += x * p1 # so x is multiply to active power spending p1
    previous = end # set previous to end , to start in future iteration the needed operations if we have one more n time period
print(ans) # print the final asnwer