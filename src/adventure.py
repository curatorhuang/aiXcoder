def adventure_game():
    # 游戏的欢迎信息
    print("Welcome to the Adventure Game!")
    print("You are standing at the entrance of a dark forest. Two paths lie before you.")
    
    # 玩家作出选择走左边还是右边
    choice = input("Do you choose to go left or right? (left/right): ")
    if choice.lower() == "left":
        # 左边路径的场景描述和交互
        print("You have chosen the left path and encountered a friendly dwarf who offers you a magical sword.")
        sword = input("Do you take the sword? (yes/no): ")
        
        if sword.lower() == "yes":
            # 拿到剑后的进一步场景描述
            print("Armed with the magical sword, you proceed deeper into the forest.")
            print("Suddenly, a wild troll appears!")
            action = input("Do you fight the troll with your sword, or run away? (fight/run): ")
            
            if action.lower() == "fight":
                # 选择战斗并描述胜利的结果
                print("With a mighty swing of your sword, you defeat the troll and find a treasure chest.")
                print("Congratulations! You've won the game with the treasure!")
            else:
                # 选择逃跑并描述结果
                print("You decided to run away. Unfortunately, you got lost and ended up back at the forest entrance.")
                print("Game over. Try again!")
        else:
            # 选择不拿剑的后果
            print("You decided not to take the sword.")
            print("Without any weapons, you were not prepared when a wild bear attacked.")
            print("Sadly, you did not survive the bear attack. Game over.")
    
    elif choice.lower() == "right":
        # 右边路径的场景描述和交互
        print("You chose the right path and stumbled upon a mysterious cave.")
        enter = input("Do you enter the cave? (yes/no): ")
        
        if enter.lower() == "yes":
            # 进入洞穴的场景描述和选择
            print("Inside the cave, you find a sleeping dragon and a pile of gold coins.")
            stealth = input("Do you try to steal some coins, or sneak out quietly? (steal/sneak): ")
            
            if stealth.lower() == "steal":
                # 偷取金币并描述逃跑的结果
                print("You successfully stole some coins, but the dragon woke up and chased you out of the cave!")
                print("Luckily, you escaped with your life and some gold. You win!")
            else:
                # 安静地离开并描述安全退出的结果
                print("You decided to sneak out quietly without disturbing the dragon.")
                print("Congratulations! You've made a wise choice and safely exited the cave.")
        else:
            # 选择不进入洞穴的后果
            print("Scared of what lies inside, you decide not to enter the cave.")
            print("Sadly, as you turn to leave, you slip and fall. You did not survive the fall. Game over.")
    else:
        # 输入无效时的处理
        print("Invalid choice. You need to choose 'left' or 'right'.")
        adventure_game()  # 如果输入无效，重新开始游戏

# 调用函数开始游戏
# adventure_game()
