'''
Group:
Alex Waweru
Joshua Kasirye'''


inputfile = open('Input.txt', 'r')

no_of_servers = int(inputfile.readline())
unique_tasks = int(inputfile.readline())
task_comps = {}

for i in range(unique_tasks):
    aline = inputfile.readline()
    string = aline.split()
    key = string[0]
    value = string[1]
    task_comps[key] = int(value)

tasks = inputfile.read()
list_of_tasks = tasks.split()
inputfile.close()

server1 = []
server2 = []
server3 = []
server4 = []
server5 = []
server6 = []

taskAs = []; taskBs = []; taskCs = []; taskDs = []; taskEs = []
taskFs = []; taskGs = []; taskHs = []; taskIs = []; taskJs = []

list_of_sorted_tasks = []
for i in range (len(list_of_tasks)):
    if list_of_tasks[i]=='A':
        taskAs.append(list_of_tasks[i])
    if list_of_tasks[i]=='B':
        taskBs.append(list_of_tasks[i])
    if list_of_tasks[i]=='C':
        taskCs.append(list_of_tasks[i])
    if list_of_tasks[i]=='D':
        taskDs.append(list_of_tasks[i])
    if list_of_tasks[i]=='E':
        taskEs.append(list_of_tasks[i])
    if list_of_tasks[i]=='F':
        taskFs.append(list_of_tasks[i])
    if list_of_tasks[i]=='G':
        taskGs.append(list_of_tasks[i])
    if list_of_tasks[i]=='H':
        taskHs.append(list_of_tasks[i])
    if list_of_tasks[i]=='I':
        taskIs.append(list_of_tasks[i])
    if list_of_tasks[i]=='J':
        taskJs.append(list_of_tasks[i])

list_of_sorted_tasks.append(taskAs); list_of_sorted_tasks.append(taskBs);
list_of_sorted_tasks.append(taskCs); list_of_sorted_tasks.append(taskDs);
list_of_sorted_tasks.append(taskEs); list_of_sorted_tasks.append(taskFs);
list_of_sorted_tasks.append(taskGs); list_of_sorted_tasks.append(taskHs);
list_of_sorted_tasks.append(taskIs); list_of_sorted_tasks.append(taskJs); 

comps = []
no_of_tasks = []
for i in range(unique_tasks):
    icomps = len(list_of_sorted_tasks[i])*task_comps[list_of_sorted_tasks[i][0]]
    comps.append(icomps)
    no_of_tasks.append(len(list_of_sorted_tasks[i]))

sumcomps = sum(comps)
each_server_time = sumcomps// no_of_servers

for i in range(unique_tasks):
    while len(list_of_sorted_tasks[i]) > 6:
        server1.append(list_of_sorted_tasks[i].pop())
        server2.append(list_of_sorted_tasks[i].pop())
        server3.append(list_of_sorted_tasks[i].pop())
        server4.append(list_of_sorted_tasks[i].pop())
        server5.append(list_of_sorted_tasks[i].pop())
        server6.append(list_of_sorted_tasks[i].pop())

for i in range(unique_tasks):
    while len(list_of_sorted_tasks[i]) > 0:
        if len(list_of_sorted_tasks[i]) > 0:
            server1.append(list_of_sorted_tasks[i].pop())
        if len(list_of_sorted_tasks[i]) > 0:
            server2.append(list_of_sorted_tasks[i].pop())
        if len(list_of_sorted_tasks[i]) > 0:
            server3.append(list_of_sorted_tasks[i].pop())
        if len(list_of_sorted_tasks[i]) > 0:
            server4.append(list_of_sorted_tasks[i].pop())
        if len(list_of_sorted_tasks[i]) > 0:
            server5.append(list_of_sorted_tasks[i].pop())
        if len(list_of_sorted_tasks[i]) > 0:
            server6.append(list_of_sorted_tasks[i].pop())

servers = []
servers.append(server1); servers.append(server2);servers.append(server3)
servers.append(server4); servers.append(server5);servers.append(server6)


def compute(servers, task_comps):
    computations = []
    listi = []

    for i in range(len(servers)):
        compute1 = 0
        for k in range(len(servers[i])):
            item = servers[i].pop()
            val = task_comps[item]
            compute1 = compute1 + val
            
        print('server', i+1, " ",compute1)
        computations.append(compute1)

    print('computations = ', max(computations) )

compute(servers, task_comps)

        
        
        












































        
    







            

            
    
        
    
