n = int(input())
teams = [input().strip() for i in range(n)]
stats = {t: [0,0,0] for t in teams}
for i in range(n*(n-1)//2):
    line = input().split()
    t1, t2 = line[0].split('-')
    g1, g2 = map(int,line[1].split(':'))
    stats[t1][0] += 3*(g1>g2)+(g1==g2)
    stats[t2][0] += 3*(g2>g1)+(g1==g2)
    stats[t1][1] += g1-g2
    stats[t2][1] += g2-g1
    stats[t1][2] += g1
    stats[t2][2] += g2
top = sorted(teams,key=lambda t:(-stats[t][0],-stats[t][1],-stats[t][2]))[:n//2]
print(*sorted(top),sep='\n')
