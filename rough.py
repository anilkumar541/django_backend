l= ['abc', 'xyz', 'aba', '1221']

count= 0

# for data in l:
#     if len(data) > 2 and data == data[::-1]: 
#         if :
#             print(data)
#             count += 1

print([data if len(data) > 2 and data == data[::-1] else "pass" for data in l])
print(count)