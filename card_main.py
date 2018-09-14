import card_tool
while True:
    card_tool.show_menu() 
    user_sel = input("请输入你的选项:")
    print("你输入的选项是%s" % user_sel)
    if user_sel in ["1", "2", "3"]:
        
        if user_sel == "1":
            card_tool.now_card()
        if user_sel == "2":
            card_tool.display_card()
        if user_sel == "3":
            card_tool.search_card()
    elif user_sel == "0":
        pass
        break
    else:
        print("输入错误")
