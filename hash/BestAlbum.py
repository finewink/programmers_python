
def solution(genres, plays):
    answer = []
    
    map = {}
    for i in range(len(genres)) : 
        if not map.get(genres[i]) or map.get(genres[i]) == None:
            map[genres[i]]= {'total' : 0, 'list' : list()}
        map[genres[i]]['total'] = map[genres[i]]['total'] + plays[i]
        map[genres[i]]['list'].append(i)

    for item in sorted(map.keys(), key=lambda k : map[k]['total'], reverse=True) : 
       songlist = sorted(map[item]['list'], key = lambda k : plays[k], reverse = True)
       answer.append(songlist.pop(0))
       if songlist : 
           answer.append(songlist.pop(0))

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print (solution(genres, plays))