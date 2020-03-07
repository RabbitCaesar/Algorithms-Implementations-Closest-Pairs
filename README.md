# Algorithms-Implementations-Closest-Pairs

---------------------------------------------------------------------------------------------------------------------------

IDE - Pycharm 

Python 3.7.2

---------------------------------------------------------------------------------------------------------------------------

This program will find the closest pair of points in a set of n points.

Two algorithms will be implemented here:

    1) A brute force approach determines the distance between every pair of points first and then find the points with the closest distance.
    
    2) An enhanced algorithm

       - Sorts all points according to coordinates;

       - Divides all points in two halves;

       - Recursively finds the smallest distances in both subarrays;

       - Take the minimum of two smallest distances;

       - Create an array strip[] that stores all points which are at most d distance away from the middle line dividing the two sets;

       - Find the smallest distance in strip[];

       - Find the points with the closest distance.

---------------------------------------------------------------------------------------------------------------------------

The time complexity of brute force algorithm is O(n^2).

The time complexity of enhanced algorithm algorithm is O(n * log(n)).

@author RabbitCaesar
