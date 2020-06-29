"""Chat Server's Outgoing Traffic
Here we had to find the traffic of an chat. Knowing that the length of message is send
is multiplied to number of participants. The output should return the whole traffic."""

"""f = open("input.txt", "r") #initialy I wanted to read input from text, because there was specified so
if f.mode == 'r':  # but codeforces compiler doesn't want this
    contents = f.readlines() #so i modified the input without modifying the program
   """



contents = [] # created list
participants = 0 # and counter for number of participant and sum
sum = 0

while True:
    try:
        s = input()
        contents.append(s) # here I try to append to list every newline input
    except:
        break


for content in contents:
    if content[0] == "+": # here program find if participants enter
        participants += 1
    elif content[0] == "-": # or leave chat
        participants -= 1 # and counter this in participants
    else:
        flash = ":" # here program detects if message exists
        message = content.partition(flash)[2] # take the message after :
        message = message.rstrip('\n')
        traffic = len(message) # take the length of message
        traffic *= participants # multiply to number of participants at the moment
        sum += traffic # and after that sum all traffic for all messages
print(sum)

