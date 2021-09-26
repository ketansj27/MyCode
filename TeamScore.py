'''
Best Club presents sports fest 2021 scheduled in the month August. A new team sport 
Kanduk Khek introduced in the current The rules of game are as follows:
each game,2 teams(A&B) play against eachother.

The input is a string consisting of a's and b's'a' means Team A has scored a point 
and 'b' means Team B has scored a point. The number of points(N) to win is decided at 
the beginning of each game. A team wins if the score reaches N..
If both teams score N-1 points, the teams take part in a decider game. The score is reset to 0.

The team to lead the score by 2 points will be the winner.The leading 2 points will be appended at the end
'''
W_score = int(input())
score = input()
Team_a = 0
Team_b = 0
for team in score:
    if team == "a" :
        Team_a = Team_a + 1
        if Team_a == (W_score-1) and Team_b == (W_score-1):
            Team_a = 0
            Team_b = 0
            print("Tie")
    elif team == "b" :
        Team_b = Team_b + 1
        if Team_a == (W_score-1) and Team_b == (W_score-1):
            Team_a = 0
            Team_b = 0
            print("Tie")

if Team_a > Team_b :print("Team a won")
else :print("Team b won")