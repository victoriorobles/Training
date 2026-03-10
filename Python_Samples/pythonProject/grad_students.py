if __name__ == '__main__':

    l_scores = list()
    l_names = list()
    second = 0
    first = 0

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     l_scores.append(score)
    #     l_names.append(name)
    l_names =["Harry","Berry", "Tina", "Akriti", "Harsh"]
    l_scores=[37.21,37.21,37.2,41,39]

    # unique = list(sorted(set(l_scores)))
    second = list(sorted(set(l_scores)))[1]
    print(l_names)
    print(f"second")

    total = dict()
    #total = dict(zip(l_scores,list(l_names)))

    for score, name in zip(l_scores,l_names):
        if score not in total:
            total[score]=[]
        total[score].append(name)
    print(f"second: {second}")
    print(total)
    for item in sorted(total[second]):
        print("".join(item))
