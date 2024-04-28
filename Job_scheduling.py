
def jobScheduling(jobs, max):
    n = len(jobs)
    sorter = lambda job : int(job[1])

    jobs = sorted(jobs, key=sorter, reverse=True)

    scheduled = []
    profit = 0
    for i in range(max+1):
        scheduled.append(None)
    for job in jobs:
        for i in range(job[2],0,-1):
            if not scheduled[i]:
                scheduled[i] = job
                profit+=job[1]
                break
    for i in scheduled:
        if i:
            print(i," ")
    print(profit)



jobs = []
n = int(input("Enter the number of jobs : "))
max = 0
for i in range(n):
    job = list(map(int, input("Enter id, profit, deadline : ").split()))
    if max<job[2]:
        max = job[2]
    jobs.append(job)

jobScheduling(jobs, max)