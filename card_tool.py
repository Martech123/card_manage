card_list = []

def show_menu():

    print("名片管理")
    print("*" * 50)
    print("1.添加名片")
    print("2.显示名片")
    print("3.查询名片")

    print("0.退出")
    print("*" * 50)
 

def now_card():
    print("-" * 50)
    print("新增名片")
    name = input("请输入你的名字:") 
    phone = input("请输入你的电话:") 
    qq = input("请输入你的qq:") 
    email = input("请输入你的email:")


    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    card_list.append(card_dict)

    print("名片添加成功")
    
def display_card():
    print("-" * 50)
    print("显示名片")
    if len(card_list) == 0:
        print("名片库无纪录")
    for name in ["name", "phone", "qq", "email"]:
        print(name, end="\t\t")
    print(" ")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" %(card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["qq"],
                                           card_dict["email"]))
def search_card():
    print("-" * 50)
    
    print("查询名片")
