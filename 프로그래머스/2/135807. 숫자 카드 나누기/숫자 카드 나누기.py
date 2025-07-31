def get_common_division(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_gcd_of_list(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = get_common_division(gcd, num)
    return gcd

def is_not_divisible(gcd, arr):
    return all(x % gcd != 0 for x in arr)

def solution(arrayA, arrayB):
    answer = 0

    gcdA = get_gcd_of_list(arrayA)
    gcdB = get_gcd_of_list(arrayB)
    # print(f"a: {gcdA}")
    # print(f"b: {gcdB}")

    candidates = []
    if is_not_divisible(gcdA, arrayB):
        candidates.append(gcdA)
    if is_not_divisible(gcdB, arrayA):
        candidates.append(gcdB)

    if candidates:
        return max(candidates)
    else:
        return 0