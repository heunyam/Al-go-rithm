LINSES = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]


def solution(lines):
    start_times = []
    end_times = []
    moments = []
    answer = 0

    for line in lines:
        time = line.split(' ')[1].split(':')

        end_time = int(int(time[0]) * 3600000 + int(time[1]) * 60000 + float(time[2]) * 1000)
        start_time = int(end_time - float(line.split(' ')[2][:-1]) * 1000 + 1)

        start_times.append(start_time)
        end_times.append(end_time)
        moments.append(start_time)
        moments.append(end_time)

    for start in moments:
        count = 0
        for i in range(len(start_times)):
            end = start + 999

            if end >= end_times[i] >= start:
                count += 1
            elif end_times[i] >= end >= start_times[i]:
                count += 1

        if count > answer:
            answer = count

    return answer


print(solution(LINSES))
