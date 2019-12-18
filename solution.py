import numpy as np
import mazeworld
data=np.array([['#','#','#','#','#','#'],['#','S',' ','#','E','#'],['#','#',' ','#',' ','#'],['#','#',' ',' ',' ','#'],['#','#','#','#','#','#']])
def direction_set(data):
    """
        函数功能，找到data中未被走过的地方，并同时记录该地方能够走的地方
    """
    dir_set = {}
    v, h= np.where(np.array(data) == ' ')
    for i, j in zip(v, h):
        key = str(i) + str(j)
        if data[i, j + 1] == ' ':  # 该地方东邻块是否能走
            dir_set[key] = [(i, j + 1)]
        if data[i + 1, j] == ' ':  # 该地方南邻块是否能走
            if key in dir_set:
                dir_set[key] += [(i + 1, j)]
            else:
                dir_set[key] = [(i + 1, j)]
        # data[i, j-1]
        if data[i, j - 1] == ' ':  # 该地方西邻块是否能走
            if key in dir_set:
                dir_set[key] += [(i, j - 1)]
            else:
                dir_set[key] = [(i, j - 1)]
        # data[i-1, j]
        if data[i - 1, j] == ' ':  # 该地方北邻块是否能走
            if key in dir_set:
                dir_set[key] += [(i - 1, j)]
            else:
                dir_set[key] = [(i - 1, j)]
    return dir_set


step = []  # 记录走的状态
key_old = 'S'  # 起始位置
print(data, '\n')

while True:
    # print(data)
    direct_set = direction_set(data)
    if key_old == 'E':  # 当到达出口的位置，就不用继续往别处走
        print(data) # 打印出路线，其中走过的位置都用-8标示出来了
        print([i for i, j in step])
        break
    if key_old in direct_set:
        step += [(key_old, direct_set[key_old])]
        data[int(key_old[0]), int(key_old[1])] = 'x'
        coors = direct_set[key_old][0]
        key_old = str(coors[0]) + str(coors[1])
    else:
        for i in range(len(step)):
            huish = step.pop()
            key = huish[0]
            values = huish[1]
            if len(values) == 1:
                data[int(key[0]), int(key[1])] = 1
                # print(data)
            else:
                key_old = str(values[1][0]) + str(values[1][1])
                step += [(key, values[1:])]
                # print(data)
                break
