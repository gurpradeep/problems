def merge_meetings(meeting_times):
        meeting_times.sort()

        merged = []
        for meeting in meeting_times:
            if not merged or merged[-1][1] < meeting[0]:
                merged.append(meeting)
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])
        return merged

# Driver code
meeting_times = [[1, 4], [2, 5], [6, 8], [7, 9], [10, 13]]
print(merge_meetings(meeting_times))
meeting_times = [[4, 7], [1, 3], [8, 10], [2, 3], [6, 8]]
print(merge_meetings(meeting_times))