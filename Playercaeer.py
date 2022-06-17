import random
print("Welcome to my Transfer Story")
print("Player Career")
amount = [2,4,20,33,5,7,8,65]
first_move = ['Bilton Wanderers', 'Derby County', 'Fleetwood Town','Nice', 'Strasbourg','Angers']
second_move = ['Lorient','RB Leipzig', 'VfL Wolfsburg','Bayer Leverkusen']
third_move = ['Bordeaux','Dijon','Guingamp','Lille','Marseille','Monaco','Nantes','Paris Saint-Germain','Toulouse']
fourth_move = ['Atlético Madrid','Barcelona','Bayern Munich','Chelsea','Juventus','Liverpool','Manchester United','Real Madrid','Valencia','Villarreal']
last_move = ['Ajax','Athletic Bilbao','Atletico Madrid','Bayer Leverkusen','Borussia Dortmund','Borussia Mönchengladbach','Chelsea','Crystal Palace','FC Bayern München','FC Bayern','FC Schalke 04','FC Zenit St. Petersburg','Fenerbahce','Fortuna Düsseldorf','Galatasaray','Hannover 96','Hoffenheim','Juventus','Liverpool','Manchester City','Manchester United','Olympiacos','PSV','RB Leipzig','SC Freiburg','Schalke 04','Sevilla','Shakhtar Donetsk','Tottenham Hotspur','Valencia','Villarreal','Werder Bremen','Zenit St. Petersburg','Zenit','Zürich']
random.shuffle (first_move)
random.shuffle (second_move)

random.shuffle(amount)
for i in range(1):
    a = input("Press Enter to guess the first club: ")
    if i == 0:
        print(f"First Club Move is:  {first_move.pop()} Worth ${amount.pop()}") # pop() removes the last element from the list and returns it.
    b = input("Press Enter to guess the Second club: ")
    if i == 0:
        print(f"Second Club Move is:  {second_move.pop()} Worth ${amount.pop()}") # pop() removes the last element from the list and returns it.
    c = input("Press Enter to guess the Third club: ")
    if i == 0:
        print(f"Third Club Move is:  {third_move.pop()} Worth ${amount.pop()}")
    d = input("Press Enter to guess the Fourth club: ")
    if i == 0:
        print(f"Fourth Club Move is:  {fourth_move.pop()} Worth ${amount.pop()}")
    e = input("Press Enter to guess the last club: ")
    if i == 0:
        print(f"Last Club Move is:  {last_move.pop()} Worth ${amount.pop()}")
        print("Thank you for playing")
    else:
        break
