team = []
for i in range(4) :
    team.append(input())
table = []
total_goal = []
for i in range(4) :
    table.append(list(map(int,input().split())))
    total_goal.append(sum(table[i]))
rev_total_goal = []
for i in range(4) :
    tmp = 0
    for j in range(4) :
        tmp = tmp + table[j][i]
    rev_total_goal.append(tmp)
score = [0]*4

for i in range(4) :
    for j in range(4) :
        if i == j :
            continue
        goal = table[i][j]
        rev_goal = table[j][i]
        # print(goal,rev_goal)
        if goal > rev_goal :
            score[i] = score[i] + 3
        elif goal == rev_goal :
            score[i] = score[i] + 1

team_info = []
for i in range(4) :
    team_info.append({
        "name":team[i],
        "score":score[i],
        "goal":total_goal[i],
        "rev_goal":rev_total_goal[i]
    })

team_info.sort(key = lambda i: i['score'],reverse=True)
for _ in range(10) :
    for i in range(4-1) :
        if team_info[i]['score'] == team_info[i+1]['score'] :
            if team_info[i]['goal'] - team_info[i]['rev_goal'] == team_info[i+1]['goal'] - team_info[i+1]['rev_goal'] :
                if team_info[i]['goal'] < team_info[i]['goal'] :
                    team_info[i],team_info[i+1] = team_info[i],team_info[i+1]
            else :
                if team_info[i]['goal'] - team_info[i]['rev_goal'] < team_info[i+1]['goal'] - team_info[i+1]['rev_goal'] :
                    team_info[i],team_info[i+1] = team_info[i],team_info[i+1]
            
for i in range(4) :
    print(team_info[i]['name'],team_info[i]['score'])