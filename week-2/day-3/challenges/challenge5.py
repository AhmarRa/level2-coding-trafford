# Challenge 5

# Create a variable called time, a variable called place_of_work
# and a variable called town_of_home.
# Create an if statement that prints where someone is at times
# of the day.
# E.g. if the time is 7 I’m at home, at 8 I’m commuting, at 9 I’m at
# work.

time = 19
place_of_work = "Leeds"
town_of_home = "Manchester"

if 0 <= time <=7:
        print(f'At {time}am, im at home, in {town_of_home}')
elif time == 8:
        print(f'At {time}am, im commuting to work, to {place_of_work}')
elif 9 <= time <= 11:
        print(f'At {time}am, im at work in {place_of_work}')
elif 12 <= time <= 17:
        print(f'At {time}pm, im at work in {place_of_work}')
elif time == 18:
        print(f'At {time}pm, im commuting home, to {town_of_home}')
else:
        print(f'At {time}pm, im somewhere in {town_of_home}')