'''
For the e-learning, various tutorials are provided to the students. One of the 
tutorials shows the highlighter on a number A on the number line. There is a "jump" 
button in the tutorial. On pressing the "jump" button, the highlighter moves by a 
fixed number D towards the right side if D is positive and towards the left side if 
D is negative. The student has to press the button N number of times. The tutorial 
has various sets of exercises. For every exercise, the positions of the highlighter 
before every "jump" button press will be stored in the database.

Write an algorithm to find the position of the highlighter before every 
button press if the button must be pressed N number of times in an exercise.

Input:
**The first line of the input consists of an integer-intialPos, representing 
the initial position of the highlighter (A). 
**The second line consists of an integer -fixedMove, representing the fixed number D.
**The third line consists of an integer-jumps. representing the number of times
the "jump" must be pressed (N).

Output
Print N space-separated integers representing the position of the highlighter 
before every button press if the button must be pressed number of times in an exercise.

Example :
Input:
7
4
3
Output:
7 11 15

Explanation:
Initially, the highlighter is on number 7. After the first jump, the highlighter moves to
7+4=11. So, before the first jump the highlighter was on 7. After the second jump, the 
highlighter moves to 11-4-15. So, before the second jump the highlighter was on 11.
Before the third jump, the highlighter is on 13. So, the output is 7, 11, 15.
'''
Initial_Pos = int(input())
fixed_Num = int(input())
JumpT = int(input())

highlight_Nums = list()
highlight_Nums.append(Initial_Pos)
lightNum = Initial_Pos + fixed_Num
highlight_Nums.append(lightNum) mw
while len(highlight_Nums) < JumpT:
    lightNum = lightNum + fixed_Num
    highlight_Nums.append(lightNum)

print(*highlight_Nums,sep = " ")