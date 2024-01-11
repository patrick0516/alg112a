def min_edit_distance(str1, str2, m, n):
    # 如果其中一个字符串為空，返回另一个字符串的長度
    if m == 0:
        return n
    if n == 0:
        return m
    
    # 如果最後一个字符相同，不需要編輯操作
    if str1[m - 1] == str2[n - 1]:
        return min_edit_distance(str1, str2, m - 1, n - 1)
    
    # 如果最後一个字符不同，考慮三種编輯操作，並選擇最小的
    insert_cost = min_edit_distance(str1, str2, m, n - 1)
    delete_cost = min_edit_distance(str1, str2, m - 1, n)
    replace_cost = min_edit_distance(str1, str2, m - 1, n - 1)
    
    return 1 + min(insert_cost, delete_cost, replace_cost)

# exapmle
str1 = "kitten"
str2 = "sitting"
result = min_edit_distance(str1, str2, len(str1), len(str2))
print("最小编辑距离:", result)
