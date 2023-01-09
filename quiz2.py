print('Welcome to Are you smarter than a 5th grader Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=6
while answer.lower()not in ["a","b","c","d"]:

 
    if answer.lower()=='yes':
        answer=input('Question 1: What is the roman numeral for 100?\nA.) C\nB.) M\nC.) W\nD.) IIIID\n> ')
    while answer.lower() not in ["a","b","c","d"]:
        print('Invalid Input,Try again:(')
        answer=input('Question 1: What is the roman numeral for 100?\nA.) C\nB.) M\nC.) W\nD.) IIIID\n> ')
    if answer.lower()=="a":
        score += 1
        print('correct')

    answer=input('Question 2: Who was the 2nd president of the united states?\nA.)Adam Smith \nB.)John Adams \nC.)Abraham Lincoln \nD.)Jeffery Bezos\n>')
    while answer.lower() not in ["a","b","c","d"]:
        print('Invalid Input,Try again:(')
        answer=input('Question 2: Who was the 2nd president of the united states?\nA.)Adam Smith \nB.)John Adams \nC.)Abraham Lincoln \nD.)Jeffery Bezos\n>')
    if answer.lower()=='b':
        score += 1
        print('correct')
    
 
    answer=input('Question 3: What is the thinnest layer of the earth?\nA.)Inner core\nB.)Mantle\nC.)Outer core \nD.)Crust\n>')
    while answer.lower() not in ["a","b","c","d"]:
        print('Invalid Input,Try again:(')
        answer=input('Question 3: What is the thinnest layer of the earth?\nA.)Inner core\nB.)Mantle\nC.)Outer core \nD.)Crust\n>')
    if answer.lower()=='d':
        score += 1
        print('correct')
  

    answer=input('Question 4: Solve 8/2(2+2)?\nA.)8\nB.)16\nC.)32\nD.)1\n>')
    while answer.lower() not in ["a","b","c","d"]:
        print('Invalid Input,Try again:(')
    answer=input('Question 4: Solve 8/2(2+2)?\nA.)8\nB.)16\nC.)32\nD.)1\n>')
    if answer.lower()=='b':
        score += 1
        print('correct')
    
    answer=input('Question 5: What is longest river in Europe?\nA.)Volga\nB.)Nile\nC.)Elbe\nD.)Danube\n>')
    while answer.lower() not in ["a","b","c","d"]:
        print('Invalid Input,Try again:(')
    answer=input('Question 5: What is longest river in Europe?\nA.)Volga\nB.)Nile\nC.)Elbe\nD.)Danube\n>')
    if answer.lower()=='a':
        score += 1
        print('correct')
    
    

    answer=input('Question 6: What do you call a word that describes a noun?\nA.)Pronoun\nB.)Verb\nC.)Adjective\nD.)Preposition\n>')
    while answer.lower() not in ["a","b","c","d"]:
        print('Invalid Input,Try again:(')
    answer=input('Question 6: What do you call a word that describes a noun?\nA.)Pronoun\nB.)Verb\nC.)Adjective\nD.)Preposition\n>')
    if answer.lower()=='c':
        score += 1
        print('correct')
   
 
print('Thankyou for playing this small quiz game, you answered',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
