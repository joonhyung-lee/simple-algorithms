def solution(sizes):
    sizes = [sorted(size, reverse=True) for size in sizes]
    max_w = max(size[0] for size in sizes)
    max_h = max(size[1] for size in sizes)
    return max_w * max_h