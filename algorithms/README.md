##  코딩테스트에서 유용한 Python 함수 모음

## itertools 모듈
### combinations(iterable, r)
기능: 순서 없는 조합

```python
from itertools import combinations
print(list(combinations([1, 2, 3], 2)))
>>> [(1, 2), (1, 3), (2, 3)]
```

### permutations(iterable, r)
기능: 순서 있는 순열

```python
from itertools import permutations
print(list(permutations([1, 2, 3], 2)))
>>> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

### product(iter1, iter2, ...)
기능: 데카르트 곱 (중첩 루프 대체 가능)

```python
from itertools import product
print(list(product([1, 2], ['A', 'B'])))
>>> [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

### combinations_with_replacement(iterable, r)
기능: 중복 조합

```python
from itertools import combinations_with_replacement
print(list(combinations_with_replacement([1, 2], 2)))
>>> [(1, 1), (1, 2), (2, 2)]
```

## collections 모듈
### Counter(iterable)
기능: 빈도수 세기

```python
from collections import Counter
print(Counter('aabbbc'))
>>> Counter({'b': 3, 'a': 2, 'c': 1})
```

### deque
기능: 양방향 큐 (스택, 큐 구현에 적합)

```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
dq.popleft()
print(dq)
>>> deque([1, 2, 3, 4])
```

## heapq 모듈 (우선순위 큐)
### heappush, heappop
기능: 최소 힙 기반의 우선순위 큐

```python
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))
>>> 1
```

## bisect 모듈 (이진탐색)
### bisect_left, bisect_right
기능: 정렬된 리스트에서 탐색 위치 반환

```python
from bisect import bisect_left, bisect_right
arr = [1, 2, 2, 3, 4]
print(bisect_left(arr, 2), bisect_right(arr, 2))
>>> 1 3
```

## math 모듈
### gcd, lcm, factorial
기능: 수학적 계산

```python
import math
print(math.gcd(12, 18))  # 최대공약수
print(math.lcm(12, 18))  # 최소공배수
print(math.factorial(5)) # 5!
>>> 6, 36, 120
```

## functools 모듈
### reduce
기능: 누적 함수 적용 (누적 곱, 합 등)

```python
from functools import reduce
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
>>> 24
```

## map, filter, zip
### map(func, iterable)
기능: 함수를 iterable 모든 요소에 적용

```python
print(list(map(str, [1, 2, 3])))
>>> ['1', '2', '3']
```

### filter(func, iterable)
기능: 조건을 만족하는 요소만 필터링

```python
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
>>> [2, 4]
```

### zip(*iterables)
기능: 동일한 위치의 요소를 튜플로 묶음

```python
a = [1, 2]
b = ['a', 'b']
print(list(zip(a, b)))
>>> [(1, 'a'), (2, 'b')]
```

### enumerate(iterable, start=0)
기능: 반복문에서 인덱스와 값을 동시에 가져오기

```python
arr = ['a', 'b', 'c']
for idx, val in enumerate(arr, start=1):
    print(idx, val)
>>> 1 a  
>>> 2 b  
>>> 3 c
```

### sorted(iterable, key=..., reverse=...)
기능: 커스텀 정렬 기준으로 정렬

```python
arr = [(1, 'b'), (3, 'a'), (2, 'c')]
print(sorted(arr, key=lambda x: x[1]))
>>> [(3, 'a'), (1, 'b'), (2, 'c')]
```

### reversed(iterable)
기능: 역순 반복자 반환

```python
for x in reversed([1, 2, 3]):
    print(x)
>>> 3 2 1
```

### set, frozenset
기능: 중복 제거, 교집합/합집합/차집합 연산에 매우 유리

```python
a = set([1, 2, 3])
b = set([2, 3, 4])
print(a & b)  # 교집합
>>> {2, 3}
```

### all() / any()
기능: 모든 요소가 참인지 / 하나라도 참인지

```python
print(all([1, 2, 3]))      # True
print(any([0, 0]))         # True 
```