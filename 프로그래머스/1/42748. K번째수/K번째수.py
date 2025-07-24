def solution(array, commands):
    answer = []
    arr = []

    for c in commands:
        print(c)
        arr = array[c[0]-1:c[1]]
        arr.sort()
        print(arr)
        answer.append(arr[c[2]-1])
        print(answer)
    return answer