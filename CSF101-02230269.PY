################################
# 1Mechanical 
# Pema Wangdi
# 02230269
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:50267
# 9
################################
# Read the input.txt file
def read_input():
    f = open('CSF101CAP/input_9_cap1.txt', 'r')
    print(f.read())
    f.close()

def calculate_score():
    f=open('CSF101CAP/input_9_cap1.txt','r')
    score=0
    scoreboard= {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}   
    for a in f:
        i=a.strip()
        if i in scoreboard:
            score+= scoreboard[i]
    print("total value: ",score)
        
      
calculate_score()

