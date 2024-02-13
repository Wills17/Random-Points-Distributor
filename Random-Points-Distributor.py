# Random Points Distributor

import random

def points_distributor(num_users, total_points):
    """Minimum and Maximum points per user"""
    min_pts_per_user = 0.1
    max_pts_per_user = 10.0

    # Array section to store points for each user
    user_points = [min_pts_per_user] * num_users

    # Distribute points randomly
    for i in range(num_users):
        # Random index to distribute points
        select_user = random.randint(0, num_users - 1)

        # Generate a random amount of points between min and max
        pts_to_distribute = random.uniform(min_pts_per_user, max_pts_per_user)

        # Distribute points to the selected user
        user_points[select_user] += pts_to_distribute

    # Check the total points distributed
    total_distributed = sum(user_points)

    # Section to cross-check if the total is outside the allowed error margin, adjust the points
    if total_distributed < total_points - 2 or total_distributed > total_points + 2:
        # Choose a random user
        user_index = random.randint(0, num_users - 1)

        # Calculate the difference between the current points and the total points
        difference = total_distributed - total_points

        # Adjust the points for the selected user
        user_points[user_index] -= difference

        # Recalculate the total
        total_distributed = sum(user_points)

    return user_points

# Define both "total users" and "total points"
num_users = 150
total_points = 300
result = points_distributor(num_users, total_points)

# Print result
for i, points in enumerate(result):
    print("User", i + 1, ":", points)

# Check the total distributed points
print("Total Distributed Points:", sum(result))


# Code by Wills_Python
