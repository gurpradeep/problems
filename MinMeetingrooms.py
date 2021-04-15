import heapq 

def min_meeting_rooms(meeting_times):
    
    if not meeting_times:
        return 0

    free_rooms = []
    meeting_times.sort(key = lambda x: x[0])
    heapq.heappush(free_rooms, meeting_times[0][1])
    
    for i in meeting_times[1:]:

        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, i[1])

    return len(free_rooms)

# Driver code
meeting_times = [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]
print(min_meeting_rooms(meeting_times))