def snail(snail_map):
    result = []
    turn = 1

    while len(snail_map) > 0:
        if turn == 1:
            for index in range(len(snail_map)):
                if index == 0:
                    result.extend(snail_map[index])
                elif index == len(snail_map) - 1:
                    result.extend(snail_map[index][::-1])
                else:
                    result.append(snail_map[index][-1])

            del snail_map[0]
            if len(snail_map) > 0:
                del snail_map[-1]
            for item in snail_map:
                del item[-1]
            turn = -1
        else:
            for index in range(len(snail_map)-1, -1, -1):
                result.append(snail_map[index][0])

            for item in snail_map:
                del item[0]
            turn = 1
 
    return result

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array1 = [[1,2,3,1],
          [4,5,6,4],
          [7,8,9,7],
          [7,8,9,7]]

snail(array)
# [1,2,3,6,9,8,7,4,5]

snail(array1)
# [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8]



