# 프로그래머스: Summer/Winter Coding(~2018) 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = {}
        for i in skill:
            if i in skill_tree:
                idx[i] = skill_tree.index(i)
            else:
                idx[i] = int(1e9)
        if list(idx.values()) == sorted(list(idx.values())):
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))