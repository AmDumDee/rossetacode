array = []

array.append(1)
array.append(3)

array[0] = 2

print(array[0])



my_array = [0] * size



my_array = [[0] * width] * height



my_array = [[0 for x in range(width)] for y in range(height)]



my_array = list()
for x in range(height):
   my_array.append([0] * width)



item = array[index]

array.pop()  
array.pop(0)

item = array[-1]  



try:

    print(array[len(array)])
except IndexError as e:
    
    print(e)



another_array = my_array[1:3]
