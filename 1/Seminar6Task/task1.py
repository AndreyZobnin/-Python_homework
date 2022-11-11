#используем filter для списка возвращаем индекс в которых 
# суммы целых чисел слева и справа от текущего элемента равны 
nums = [4, 1, 7, 9, 3, 9]
find_central_point = [i for i in filter(lambda x: sum(nums[x+1:])==sum(nums[:x]), range(len(nums)))]
print(find_central_point)
