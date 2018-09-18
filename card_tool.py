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
        return
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
    name = input("请输入需要搜索的姓名:")
    for card in card_list:
        if card["name"] == name:

            for name in ["name", "phone", "qq", "email"]:
                print(name, end="\t\t")
            print(" ")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" %(card["name"],
                                               card["phone"],
                                               card["qq"],
                                               card["email"]))
            edit_card(card) 
            break
    else:
        print("没有找到")


def edit_card(card):
    print("针对搜索到的名片,你想执行的操作是:1.修改 2.删除 0.退出")
    act_sel = input("请输入")

    if act_sel == "1":
        print("修改名片") 
        card["name"] = input("请输入修改的名字:") 
        card["phone"] = input("请输入修改的电话:") 
        card["qq"] = input("请输入修改的qq:") 
        card["email"] = input("请输入修改的email:") 
    if act_sel == "2":
        print("删除名片")
        card_list.remove(card)
    return
