test_data = [[1, 2, 3], [3, 3, 5], [8, 9, 4], [2, 8, 4]]

def pinball(lst):
    tries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    already = []
    for i in lst:
        if i not in already:
            del tries[i]
            already.append(i)
        else:
            continue
    return already

# print(pinball(test_data))

def pinball_game(test_data, nr_holes = 10):
    result = set()
    for game_result in test_data:
        result = result.union(set(game_result))
        print("x")
    holes_set = set(range(1, nr_holes + 1))
    print(holes_set)
    result = holes_set.difference(result)
    print(result)
pinball_game(test_data)

