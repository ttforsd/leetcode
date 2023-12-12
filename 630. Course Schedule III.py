import heapq

def solver(courses): 
    courses.sort(key=lambda c: c[1])
    time = 0 
    study = [] 
    res = 0 
    for duration, date in courses: 
        duration = -duration 
        time -= duration 
        heapq.heappush(study, duration)
        while len(study) != 0 and time > date: 
            time += heapq.heappop(study)
        res = max(res, len(study))
    return res


courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]

courses = [[914,9927],[333,712],[163,5455],[835,5040],[905,8433],[417,8249],[921,9553],[913,7394],[303,7525],[582,8658],[86,957],[40,9152],[600,6941],[466,5775],[718,8485],[34,3903],[380,9996],[316,7755]]


courses = [[1,2],[2,3]]

courses = [[5,5],[4,6],[2,6]]

courses = [[9,14],[7,12],[1,11],[4,7]]

print(len(courses))
print(solver(courses))
