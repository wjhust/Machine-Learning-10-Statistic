#第八章函数
#def greet_user(username):
#定义函数
#    """显示简单的问候语"""
#显示注释，说明函数干嘛
#    print("Hello,"+username.title()+"!")

#调用函数
#greet_user('bob')
#这个函数里形参是是username，实参是bob；

#def describle_pet(pet_name,animal_type='dog'):
#    print("\nI have a "+animal_type+".")
#   print("My "+animal_type+"'s name is "+pet_name.title()+".")

#describle_pet('pig','lily')
#describle_pet('dog','eric')
#这是一般实参；
#describle_pet(animal_type='cat',pet_name='sily')
#describle_pet(pet_name='sily',animal_type='cat')
#这是关键字实参，好处是能够和函数的对应,并且对应起来后和顺序无关；
#describle_pet(pet_name='liming')
#而且还会发现，在给形参赋予默认值时候，默认的要放后边，放前边不行；
#describle_pet(pet_name='ca',animal_type='cat')
#但是如果实参类型和形参的默认值不同，则以实参为主；




#def get_formatted_name(first_name,last_name):
#   full_name=first_name+' '+last_name
#return full_name.title()
#musician=get_formatted_name('bob', 'stephen')
#print(musician)

#def build_person(first_name,last_name,age=''):
#    person={'first':first_name,'last':last_name}
#    if age:
#        person['age']=age

#    return person

#musician=build_person('jimi','hendrix',age=27)
#print(musician)


#函数和while结合使用
#def get_formatted_name(first_name,last_name):
#   full_name=first_name+' '+last_name
#   return full_name.title()
#while True:
#    print("please tell me your name:")
#    print("(enter 'q' at any time to quit)")

#    f_name=input("First name:")
#    if f_name=='q':
#        break

#    l_name=input("Last name:")
#    if l_name=='q':
#        break

#    formatted_name =get_formatted_name(f_name,l_name)
#    print("\nHello,  "+formatted_name+"!")




#函数参数的传递
#def greet_users(names):
#    for name in names:
#        msg="hello, "+name.title()+"!"
#        print(msg)
#usernames=['bob','li','san']
#greet_users(usernames)



#未使用函数时的打印；
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#completed_models = []
#while  unprinted_designs:
#只要unprinted还未空，从末尾减去一个，传递给current，并将current传给completed
#    current_design=unprinted_designs.pop()
#    print("printing model: "+current_design)
#    completed_models.append(current_design)

#print("\nthe following models have been printed; ")
#for completed_model in completed_models:
#    print(completed_model)

#下面使用函数更高效率；

#def print_models(unprinted_designs,completed_models):
#    while unprinted_designs:
#         current_design=unprinted_designs.pop()
#         print("Printing model: "+current_design)
#         completed_models.append(current_design)


#def show_completed_models(completed_models):
#   print("\nThe following models have been printed:")
#   for completed_model in completed_models:
#       print(completed_model)
#unprinted_designs=['iphone case','robot pendant','dodecahedron']
#completed_models=[]
#print_models(unprinted_designs[:],completed_models)
#show_completed_models(completed_models)
#好处在于，更容易扩展和维护：（1）可直接另外附加print
#（2）修改参数时候只需要修改一次；（3）每个函数只负责一项工作，更清晰；




#传递不同数量的实参，使用*
#def make_pizza(*toppings):
#*toppings使得python创建空的元组，可以收到很多实参
#    print("\nMaking a pizza with the following toppings:")
#    for topping in toppings:
#        print("-"+topping)
#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')


#传递不同数量和类型的实参，把接纳任意数量和类型实参所对应的形参放最后
#def make_pizza(size,*toppings):
#*toppings使得python创建空的元组，可以收到很多实参
#    print("\nMaking a  "+str(size)+"-inch pizza with the following toppings:")
#    for topping in toppings:
#        print("-"+topping)
#make_pizza(10,'pepperoni')
#make_pizza(12,'mushrooms','green peppers','extra cheese')






#传递未知信息给函数，此时需要将函数能够接受任意数量的键值，函数的形参使用**来创建字典
#def build_profile(first,last,**user_info):
#    profile={}
#     profile['first_name']=first
#    profile['last_name']=last
#    for key,value in user_info.items():
#        profile[key]=value
#    return profile

# user_profile=build_profile('albert','einstein',location='princeton',field='physics')
# print(user_profile)


#将函数存储到模块中，使用import
#def make_pizza(size,*toppings):
#*toppings使得python创建空的元组，可以收到很多实参
#    print("\nMaking a  "+str(size)+"-inch pizza with the following toppings:")
#    for topping in toppings:
#        print("-"+topping)
#使用模块之前，需要先建立，例如建立pizza模块，则需要把初pizza之外的函数和代码都删除
#import pizza的含义让python打开pizza.py，并将其中的函数复制到这个程序中
#调用函数的语句变为：
#pizza.make_pizza(16,'pep')




#导入特定的函数：from module_name import function_name
#from module_name import function_0,function_1,function_2倒入任意数量的函数
#还可以使用as，给导入的的函数或者模块重新命名；
#使用*，即导入所有函数； from。。。 import *



#编写函数指南



