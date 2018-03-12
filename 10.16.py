#bicycles=['trek','cannondale','redline','specialized']
#print(bicycles)
#打印列表
#print(bicycles[0])
#返回第一个元素；
#print(bicycles[1])
#返回列表中的第几个元素,注意索引从0开始；
#print(bicycles[0].title())
#print(bicycles[-1])
#-1是让python返回最后一个列表元素，同理-2就是倒数第二个元素，负数即倒数元素；
#message="My friend was a "+ bicycles[0].title()+"."
#print(message)

#motorcycles=['honda','yamaha','suzuki']
#print(motorcycles)
#motorcycles[0]='ducati'
#修改列表的第一个元素；
#print(motorcycles)
#motorcycles.append('ducati')
#在末尾添加一个元素，.append()是添加命令；
#print(motorcycles)
#motorcycles.insert(0,'ducati')
#在列表开头插入元素；
#print(motorcycles)
#del motorcycles[0];
#删除列表中的元素，使用delete函数
#print(motorcycles)
#delete只是单纯的删除，而pop函数删除的同时，还能够使用它的值
#popped_motorcycle=motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)
#first_owned=motorcycles.pop(0)
#print('The first motorcycle i owned was a '+first_owned.title()+'.')
#说明：pop函数可以删除任何元素，并且给出删除的元素的值；
#motorcycles.remove('yamaha')
#不知道yamaha的位置但是知道我要删除yamaha，则可以直接remove，但remove只删除第一个值并不是所有的，如果有多个只能用循环；
#print(motorcycles)


# 永久排序
#cars=['bmw','audi','toyota','subaru']
#len(cars)
#cars.sort()
#排序，而且是永久性的，无法恢复；
#print(cars)
#cars.sort(reverse=True)
#倒着排序，也是永久性的；

#临时排序
#print("Here is the original list:")
#print(cars)

#print("\nHere is the original list:")
#print(sorted(cars))

#print("\nHere is the original list again:")
#print(cars)
#sorted()函数的排序是临时的

#cars.reverse()
#反转最初列表的排序
#print(cars)


#循环的介绍
#magicians=['alice','david','carolia'];
#for magician in magicians:
    #print(magician.title()+",that was a great trick!")
   # print("i can't wait to see you next trick," + magician.title() + ".")
#print("i can't wait to see you next trick,"+magician.title()+".")
#注意：缩紧则进入循环，没缩紧不进入循环；
#不要进行不必要的缩进；

#range函数的使用；
#for value in range(1,5):
 #   print(value)
#从1开始，输出到5停止并且不包含5
#numbers=list(range(1,6))
#print(numbers)
#打印列表1～5；

#even_numbers=list(range(2,12,2))
#print(even_numbers)
#偶数

#range函数和循环的搭配使用
#squares = []
#for value in range(1, 11):
#    square = value ** 2
#    squares.append(square)

#   print(squares)

#平方数的第二种方法
#squares=[]
#for value in range(1,11):
#    squares.append(value**2)
#   print(squares)

#digits=[1,2,3,4,5,6,7,8,9,10]
#print(min(digits))
#print(sum(digits))


#平方数的第三种方法
#squares=[value**2 for value in range(1,11)]
#print(squares)

#players=['charles','martina','michael','florence','eli']
#切片功能，只提取列表的一部分
#print(players[0:3])
#print(players[:4])
#print(players[:3])


#复制列表
#my_foods.append('cannoli')
#friend_foods.append('ice cream')
#my_foods=['pizza','falafel','carrot cake']
#friend_foods=my_foods[:]
#这一句相当于重复上一句，复制列表
#my_foods.append('cannoli')
#friend_foods.append('ice cream')
#这两句是附加进去的，因此只出现附加作用，未循环；
#print("My favorite foods are: ")
#print(my_foods)

#print("\nMy favorite foods are: ")
#print(friend_foods)

#元组：不同于列表，列表可变化，元组不可以变化
#dimensions=(200,50)
#print(dimensions[0])
#print(dimensions[1])
#注意这里使用圆括号，定义了200和50，这都不能改变的
#for dimension in dimensions:
#    print(dimension)
# dimensions=(400,100)
# print(dimensions[0])
#注：虽然不能更改元组的数据，但是可以通过赋值改变元组的数值

# if语句的学习
#cars=['audi','bmw','subaru','toyota']

#for car in cars:
#    if car == 'bmw':
#       print(car.upper())
#    else:
#        print(car.title())


#检查是否不相等
#requested_topping='anchovies'
#if requested_topping !='anchovies':
#    print("hold the anchovies")

#banned_users=['andrew','carolina','david']
#user='marie'
#if user not in banned_users:
#    print(user.title()+",you can post a response if you wish ")


#if 语句的使用
#age=17
#if age>=18:
#    print(" u are old enough")
#else:
#    print("sorry ,u are young")

#if-elif-else的使用
#age=12
#if age<=4:
#    print("your admission cost is $0")
#elif age<18:
#    print("your admission cost is $5")
#else:
#    print("your admission cost is $10")

#省略else代码块
#age=12

#if age<4:
#    price=0
#elif age<18:
#    price=5
#elif age<65:
#    price=10
#elif age>=65:
#    price=5
#print("Your admission cost is $"+str(price)+".")

#requested_toppongs=['mushromm','extra cheese']

#if 'mushromm' in requested_toppongs:
#    print("a")
#elif 'p' in requested_toppongs:
#    print("b")
#elif 'h' in requested_toppongs:
#    print('c')

#available_topping=['mushroom','olives','green peppers','pepperoni','pineapple','extra cheese']
#requested_topping=['mushroom','french fries','extra cheese']
#for requested_topping in available_topping:
#    if requested_topping:
#        print("adding"+requested_topping+".")
#    else:
#        print("Sorry,we don't have"+requested_topping+".")