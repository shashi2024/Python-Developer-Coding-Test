def sort_dict_by_values(d: dict) -> dict:
    items = list(d.items())
    

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]:
                items[i], items[j] = items[j], items[i]
    
    sorted_dict = {k: v for k, v in items}
    return sorted_dict

print(sort_dict_by_values({"a": 3, "b": 1, "c": 2}))  
