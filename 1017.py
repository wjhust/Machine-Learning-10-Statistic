# 字典的使用
#alien_0={'color':'green','points':5}
#print(alien_0['color'])
#print(alien_0['points'])
#{}花括号表示字典，包含一系列的键值
#key:键 这里是color point等
#value：值 这里是5
#color为键，冒号后的为值；
#new_points=alien_0['points']
#print("You just earned"  + str(new_points) + "points!")
#alien_0['x_position']=0
#alien_0['y_position']=25
#print(alien_0)
#增加字典的键值；
#alien_0={}
#alien_0['color']='green'
#alien_0['points']=5
#print(alien_0)
#也可以先建立一个空的字典，再依次进行增加键值；
#alien_0={'color':'green'}
#print("the alien is" +alien_0['color']+".")
#alien_0={'color':'yellow'}
#print("the alien now is" +alien_0['color']+".")
#对字典进行修改；



##重要例子：跟踪不同移动速度的外星人
#alien_0={'x-position':0,'y-position':25,'speed':'fast'}
#print("Original x-position:"+str(alien_0['x-position']))
#if alien_0['speed']=='slow':
#    x_increment=1
#elif alien_0['speed']=='medium':
#    x_increment=2
#else:
#    x_increment=3
#alien_0['x-position']=alien_0['x-position']+x_increment
#print("new position:"+str(alien_0['x-position']))


#alien_0={'color':'green','points':5}
#print(alien_0)
#del alien_0['points']
#print(alien_0)
#删除字典中的数值，使用del进行删除



#favorite_languages={
#    'jen':'python',
#    'ben':'C',
#    'edward':'ruby',
#    'lily':'python'
#}
#print("jen 's favorite languange is "+favorite_languages['jen'])
#print(favorite_languages['ben'])

#user_0={
#    'username':'efemi',
#    'first':'enrico',
#    'last':'fermi'
#}
#for key,value in user_0.items():
#key和value是定义的用于储存键和值的变量
#.items()包含了字典的键和值
#    print("\nKey:"+ key)
#\n保证每次输出完一组key和value都能空一行
#    print("Value:"+ value)
#两个for循环可以进行遍历
#for name,language in favorite_languages.items():
#    print("\n")
#    print(name.title()+"'s favorite language is"+language.title())
#for name in sorted(favorite_languages.keys()):
#   print(str(name.title)+",3q for taking the poll")
#遍历所有的键；
#sorted是按着顺序进行遍历；
#print("The following languages have been mentioned:")
#for language in set(favorite_languages.values()):
#    print(language.title())
#set()是取不同的列表；



#字典列表
#alien_0={'color':'green','points':5}
#alien_1={'color':'yellow','points':4}
#alien_2={'color':'red','points':3}
#aliens=[alien_0,alien_1,alien_2]
#for alien in aliens:
#    print(alien)

##重要例子创建30个外星人,并且给出前三个带颜色的外星人
#aliens=[]
#创建空列表
#for alien_number in range(30):
#    new_alien={'color':'green','points':5,'speed':'slow'}
#    aliens.append(new_alien)
#循环30次，每次创建一个外星人，加到列表末尾
#for alien in aliens[0:3]:
#    if alien['color']=='green':
#        alien['color']='yellow'
#        alien['speed']='medium'
#        alien['points']=10
#    elif alien['color']=='yellow':
#        alien['color']='red'
#        alien['speed']='fast'
#        alien['points']=15
#for alien in aliens[0:5]:
#    print(alien)

#输出列表中前五个外星人
#print("...")
#print("Total number of aliens:"+str(len(aliens)))
#显示一共创建多少个外星人




#在字典中储存列表
#pizza={
#    'crust':'thick',
#    'toppings':['mushroom','extra cheese'],
#}
#储存列表
#print("you ordered a "+pizza['crust']+"-crust pizza"+"with the following toppings:")
#for topping in pizza['toppings']:
#    print("\t"+topping)

#字典中储存字典
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'

    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    },
}

for username,user_info in users.items():
#在for里可以直接定义username,user_info
    print("\nUsername:"+username)
    full_name=user_info['first']+""+user_info['last']
    location=user_info['location']

    print("\tFull name:"+full_name.title())
    print("\tlocation:"+location.title())











