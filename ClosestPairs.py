
"""

This program will find the closest pair of points in a set of n points.
Two algorithms will be implemented here:
    1) A brute force approach determines the distance between
       every pair of points first and then find the points
       with the closest distance.
    2) An enhanced algorithm
       - Sorts all points according to coordinates;
       - Divides all points in two halves;
       - Recursively finds the smallest distances in both subarrays;
       - Take the minimum of two smallest distances;
       - Create an array strip[] that stores all points which are at
         most d distance away from the middle line dividing the two sets;
       - Find the smallest distance in strip[];
       - Find the points with the closest distance.

 The time complexity of brute force algorithm is O(n^2).
 The time complexity of enhanced algorithm algorithm is O(n * log(n)).

 @author RabbitCaesar

"""

import numpy as np
import timeit

# Input random generator
# Use this to create different testing inputs
def input_random_generator(n):
    arrP = []
    for i in range (n):
        temp = []
        for j in range (2):
            temp.append(np.random.randint(1,50))
        arrP.append(temp)
    return arrP

# Calculate Euclidean distance between 2 points
def get_distance(point1, point2):
    return np.round(np.sqrt((point1[0] - point2[0]) ** 2
                            + (point1[1] - point2[1]) ** 2), 2)

# Brute force O(n^2)
def brute_force(arr, n):
    min_dist, pair = float('inf'), []
    # Iterate through all the possible pairs
    # Calculate distance and compare to find min
    for i in range(n - 1):
        for j in range(i + 1, len(arr)):
            dist = get_distance(arr[i], arr[j])
            if min_dist > dist:
                min_dist = dist
                pair = [arr[i], arr[j]]
    return [min_dist, pair]


# Sort points vertically or horizontally. For example, points
# (4,3), (6,2), (1,7) will be sorted to (6,2), (4,3), (1,7) vertically
def sort_points(array, index=0):
    return sorted(array, key=lambda x: x[index])


# Find the closest pair of points in the strip.
# Return the min distance between the closest pair.
def get_strip_min_dist(points, n, min_dist=float('inf')):
    # it's proven that the max iteration of this loop is 6
    for i in range(min(6, n - 1), n):
        for j in range(max(0, i - 6), i):
            dist = get_distance(points[i], points[j])
            if min_dist > dist: min_dist = dist
    return min_dist


# Recursively find the distance between the closest pair
def closest_pair_raw(points_h_sorted, points_v_sorted, n):
    # Base case: if there are only 2 or 3 points, then use brute force
    if n <= 3:
        return brute_force(points_h_sorted, n)[0]

    # Recursion part
    mid = n // 2
    # Left section
    dist_left = closest_pair_raw(points_h_sorted
                                 , points_v_sorted[:mid], mid)
    # Right section
    dist_right = closest_pair_raw(points_v_sorted
                                  , points_v_sorted[mid:], n - mid)
    min_dist = min(dist_left, dist_right)

    # Points in the strip
    strip = []
    for point in points_h_sorted:
        if abs(point[0] - points_h_sorted[mid][0]) < min_dist:
            strip.append(point)

    # Get the distance between closest pair in strip
    min_dist_strip = get_strip_min_dist(strip, len(strip), min_dist)

    return min(min_dist, min_dist_strip)

# Return final distance between closest pair
def closest_pair_of_points(points, n):
    points_h_sorted = sort_points(points, index=0)
    points_v_sorted = sort_points(points, index=1)

    return (closest_pair_raw(points_h_sorted, points_v_sorted, n))


"""
Driver executes DTM
"""
if __name__ == '__main__':

    # Manual Test case 1:
    #points = [(32, 24), (34, 70), (77, 61), (37, 99), (26, 47), (16, 53)]

    # Manual Test case 2:
    # points = [[82, 31], [67, 11], [80, 7], [25, 22], [84, 23]
    #         , [21, 2], [24, 74], [21, 53], [28, 85], [12, 7]]

    # Manual Test case 3:
    # points  =[[94, 38], [35, 48], [18, 59], [33, 95], [57, 80]
    #         , [34, 5], [71, 42], [42, 41], [75, 40], [81, 52]
    #         , [99, 21], [74, 59], [83, 70], [17, 72], [22, 50]
    #         , [51, 16], [12, 80], [57, 96], [7, 14], [5, 2]]

    # Random generator can be used to initialize input points
    points = input_random_generator(100)

    """
    Brute Force Approach O(n^2)
    Set timmer to log the runtime 
    """
    start = timeit.default_timer()

    brute_force_result = brute_force(points, len(points))

    stop = timeit.default_timer()
    time_b = stop - start

    """
    Enhanced Approach O(nlog(n))
    Set timmer to log the runtime 
    """
    start = timeit.default_timer()

    nlogn_result = closest_pair_of_points(points, len(points))

    stop = timeit.default_timer()
    time_e = stop - start

    """
    Display final results
    """
    comp = np.round(time_b/time_e ,2)
    pointA = str(brute_force_result[1][0])
    pointB = str(brute_force_result[1][1])

    print('\nInputs:\n' + str(points))
    print('\nClosest Pair Is: ' + pointA + ' and ' + pointB)

    print('\nBrute Force Approach O(n^2):\nMin Distance: '
          + str(brute_force_result[0]) + '\nRuntime: '
          , time_b)
    print('\nEnhanced Approach O(nlog(n)):\nMin Distabce: '
          + str(nlogn_result) + '\nRuntime: '
          , time_e)
    print('\nRuntime Comparison:\nEnhanced Approach is'
          , comp, 'times faster than Brute Force.')
