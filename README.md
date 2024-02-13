# Random-Points-Distributor

This code is a points distributor function designed to allocate a total number of points randomly among a certain number of users while ensuring that the total distributed points are within a certain margin of error from the desired total points.

Breakdown of what the code does:

1. It defines a function `points_distributor` which takes two arguments: `num_users` (the number of users) and `total_points` (the total points to be distributed).

2. It initializes `min_pts_per_user` and `max_pts_per_user`, which represent the minimum and maximum points that can be allocated to each user.

3. It creates an array `user_points` to store the points allocated to each user, initialized with minimum points for each user.

4. It iterates over each user, selecting a random user and allocating a random number of points within the defined range.

5. After distributing points, it checks if the total distributed points are within a margin of error (±2 points) from the desired total points. If not, it adjusts the points for a randomly selected user to bring the total closer to the desired total.

6. Finally, it returns the array of points allocated to each user.

7. It then prints the points allocated to each user and the total distributed points.
