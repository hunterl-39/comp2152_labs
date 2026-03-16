#=============================================#
#   Author: Hunter Lusk
#   Assignment: #1
#=============================================#

# String data type
gym_member = "Alex Alliton"

# Float data type
preferred_weight_kg = 20.5

# Integer data type
highest_reps = 25

# Boolean data type
membership_active = True


# Dictionary data type: keys are strings (friend names),
# values are tuples of three integers (workout minutes)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 50),
    "Taylor": (25, 30, 60)
}


# d. Calculate total workout minutes and add new key-value pairs
friends = list(workout_stats.keys())

for friend in friends:
    minutes = workout_stats[friend]
    
    total = 0
    for minute in minutes:
        total = total + minute
    
    workout_stats[friend + "_Total"] = total


# e. Create a 2D (nested) list
# A nested list (2D list) stores lists inside another list
workout_list = []

for friend in workout_stats:
    if "_Total" not in friend:
        minutes_tuple = workout_stats[friend]
        minutes_list = list(minutes_tuple)
        workout_list.append(minutes_list)


# f. Slice the workout_list

# Extract yoga and running minutes for all friends
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[0:2])   # first two activities


# Extract weightlifting minutes for the last two friends
print("Weightlifting minutes for last two friends:")
last_two_friends = workout_list[-2:]

for row in last_two_friends:
    print(row[2])    # third activity


# g. Check if any friend's total workout minutes >= 120
for key in workout_stats:
    if "_Total" in key:
        if workout_stats[key] >= 120:
            name = key.replace("_Total", "")
            print("Great job staying active,", name + "!")


# h. Allow user input
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats and "_Total" not in friend_name:
    
    minutes = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    
    print(friend_name + "'s Workout Minutes:")
    print("Yoga:", minutes[0], "minutes")
    print("Running:", minutes[1], "minutes")
    print("Weightlifting:", minutes[2], "minutes")
    print("Total:", total, "minutes")

else:
    print("Friend", friend_name, "not found in the records.")


# i. Print friend with highest and lowest total workout minutes
highest_total = None
lowest_total = None
highest_name = ""
lowest_name = ""

for key in workout_stats:
    if "_Total" in key:
        total = workout_stats[key]
        name = key.replace("_Total", "")
        
        if highest_total is None or total > highest_total:
            highest_total = total
            highest_name = name
        
        if lowest_total is None or total < lowest_total:
            lowest_total = total
            lowest_name = name


print("Friend with highest total workout minutes:", highest_name)
print("Friend with lowest total workout minutes:", lowest_name)