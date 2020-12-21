def solution(skill, skill_trees):
    answer = len(skill_trees)
    for each_tree in skill_trees:
        top = 0
        for s in each_tree:
            if s in skill:
                if skill[top] != s:
                    answer -= 1
                    break
                top += 1
    return answer