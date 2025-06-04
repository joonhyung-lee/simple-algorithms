def solution(data, ext, val_ext, sort_by):
    filtered_data = []
    idx_map = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    # Filter
    for item in data:
        if item[idx_map[ext]] < val_ext:
            filtered_data.append(item)

    # Bubble sort
    n = len(filtered_data)
    for i in range(n):
        for j in range(0, n-i-1):
            # compare each otehr
            current_value = filtered_data[j][idx_map[sort_by]]
            next_value = filtered_data[j+1][idx_map[sort_by]]
            
            if current_value > next_value:
                filtered_data[j], filtered_data[j+1] = filtered_data[j+1], filtered_data[j]
    
    return filtered_data

if __name__ == "__main__":
    data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
    ext = "date"
    val_ext = 20300501
    sort_by = "remain"

    result = solution(data, ext, val_ext, sort_by)
    print(result)