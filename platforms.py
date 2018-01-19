
""" Minimum Number of Platforms Required for a Railway/Bus Station
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms
required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)
"""

arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]

def numero_plataformas(arr, dep):

    arr.sort()
    dep.sort()

    plataformas = 1
    total = 1

    i = 0
    j = 0

    while i < len(arr) and j < len(dep):

        if arr[i] < dep[j]:

            plataformas += 1

            if plataformas > total:
                print("Nueva plataforma: arr->" + str(arr[i]) + "dep->" + str(dep[j]))
                total = plataformas
            i += 1
        else:
            plataformas -= 1
            j += 1
    return total

print(numero_plataformas(arr, dep))