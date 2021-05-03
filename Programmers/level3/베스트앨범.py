def solution(genres, plays):
    answer = []
    music = {}
    music_cnt = {}
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = [[i, plays[i]]]
            music_cnt[genres[i]] = plays[i]
        else:
            music[genres[i]].append([i, plays[i]])
            music_cnt[genres[i]] += plays[i]

    for k, v in music.items():
        v.sort(key=lambda x: (-x[1], x[0]))
    music_cnt = sorted(music_cnt.items(), key=lambda x: -x[1])

    for key, value in music_cnt:
        if len(music[key]) >= 2:
            answer.extend(list(map(lambda x: x[0], music[key][:2])))
        else:
            answer.append(music[key][0][0])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))    # [4, 1, 3, 0]
print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))   # [0, 1, 2, 4]
print(solution(["A", "A", "B", "A", "B", "B"], [5, 5, 6, 5, 7, 7])) # [4, 5, 0, 1]
print(solution(["classic", "pop", "classic", "classic", "jazz", "pop", "Rock", "jazz"], [500, 600, 150, 800, 1100, 2500, 100, 1000]))   # [5, 1, 4, 7, 3, 0, 6]
