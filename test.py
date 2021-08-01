import sys
from random import randint
name = input('請輸入名字')
roleData={name:100,'怪物':100}
def showHp(roleData):
    for role in roleData:
        print('角色 {:7s} , 血量 {:3d}'.format(role,roleData[role]))
def changeHp(roleData,role,amount):
    if role in roleData:
        roleData[role]+=amount
def setHp(roleData,role,amount):
    if role in roleData:
        roleData[role]=amount
def menu(roleData,role,type):
    if type==1:
        damage = -randint(0,20)
        print(role + '攻擊 , 傷害:'+ str(damage))
        if role ==name:
            changeHp(roleData,'怪物',damage)
        elif role == '怪物':
            changeHp(roleData,name,damage)
        showHp(roleData)
    elif type ==2:
        recover= randint(0,10)
        print(role+'回復術 , 血量回復+ '+str(recover))
        changeHp(roleData,role,recover)
        (roleData)
    elif type ==3:
        print('你成功逃跑了')
        sys.exit(0)
    else:
        print('放棄回合')
def checkWinner(roleData):
    if roleData[name]>roleData['怪物']:
        if roleData['怪物']<=0:
            return name
    elif roleData[name]<roleData['怪物']:
        if roleData[name]<=0:
            return '怪物'
    return 'No'
showHp(roleData)
print('\n功能列表:\n1.攻擊\n2.回血\n3.逃跑')
while True:
    choice=int(input('請輸入所選功能'))
    choice2=randint(1,2)
    menu(roleData,name,choice)
    print()
    menu(roleData,'怪物',choice2)
    winner=checkWinner(roleData)
    if winner != 'No':
        print('勝利者是: '+winner)
        break