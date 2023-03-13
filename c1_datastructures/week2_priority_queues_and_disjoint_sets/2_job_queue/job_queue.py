# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = list(map(list,list(enumerate([0]*n_workers))))
    for job in jobs:
        result.append(AssignedJob(next_free_time[0][0],next_free_time[0][1]))
        next_free_time[0][1] += job
        siftdown(0,next_free_time,n_workers-1)
    return result


    '''
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result
    '''

def siftdown(i,next_free_time,size):
    mini = i
    # LHS sift
    left = (2 * i) + 1
    if left <= size and next_free_time[left][1] < next_free_time[mini][1]:
        mini = left
    elif left <= size and next_free_time[left][1] == next_free_time[mini][1] and next_free_time[left][0] < next_free_time[mini][0]:
        mini = left
    # RHS sift
    right = (2*i) + 2
    if right <= size and next_free_time[right][1] < next_free_time[mini][1]:
        mini = right
    elif right <= size and next_free_time[right][1] == next_free_time[mini][1] and next_free_time[right][0] < next_free_time[mini][0]:
        mini = right

    if mini != i:
        next_free_time[i],next_free_time[mini] = next_free_time[mini],next_free_time[i]
        siftdown(mini,next_free_time,size)
    


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
