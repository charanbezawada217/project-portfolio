questions=[
    {
        "question":"who is the prime minister of India?",
        "options":["A.Rahul Gandhi","B.Yogi Adithyanadh","C.Narendra Modi","D.Nirmala Sitharraman"],
        "answer":"C" },

    {
        "question":"what is the Capital of India?",
        "options":["A.Mumbai","B.Delhi","C.Chennai","D.Hyderabad"],
        "answer":"B" },


    {
        "question":"who is called as captain cool",
        "options":["A.Sachin Tendulkar","B.Kane williamson","C.Ms Dhoni","D.Rohit Sharma"],
        "answer":"C" },
]
leaderboard=[]

def add_question():

    print("\n ============= ADD QUESTION ========")
    question = input("Enter question: ")
    option_a=input("Enter option A: ")
    option_b=input("Enter option B: ")
    option_c=input("Enter option C: ")
    option_d=input("Enter option D: ")

    answer=input("Enter correct answer(A/B/C/D): ").upper()
    questions.append({
        "question":question,
        "options":["A "+option_a,
                   "B "+option_b,
                   "C "+option_c,
                   "D "+option_d],
        "answer":answer
    })
    print("QUESTION ADDED SUCCESSFULLY")

def view_question():
    print("\n ============VIEW QUESTIONS===============")
    count=1
    for q in questions:
        print("\n Question: ",count)
        print(q["question"])
    
        for option in q["options"]:
            print(option)
    
        print("correct Answer: ",q["answer"])
        count+=1

def  show_Leaderboard():
    if len(leaderboard)==0:
        print("\n No Quiz Attempt")
        return
    sorted_board=sorted(leaderboard,key=lambda x:x["score"],reverse=True)
    print("\n ==========LEADERBOARD==============")
    rank = 1
    for student in sorted_board:
        print(rank,student["name"],"-score:",student["score"],"-percentage",round(student["percentage"],2))
        rank+=1

def calculate_percentage(score,total_questions):
    percentage=(score/total_questions)*100
    return percentage

def calculate_grade(percentage):
    if percentage >=90:
        return "A+"
    elif percentage >=75:
        return "A"
    elif percentage >=60:
        return "B"
    elif percentage >=45:
        return "c"
    else:
        return "fail"


def show_result(student_name,score,total_questions):
    percentage=calculate_percentage(score,total_questions)
    grade=calculate_grade(percentage)

    print("\n ==============  RESULT  =================")
    print("name:",student_name)
    print("Score:",score)
    print("Total Marks:",questions)
    print("percentage:",round(percentage,2),"%")
    print("Grade:",grade)

    leaderboard.append({
        "name":student_name,
        "score":score,
        "percentage":percentage
    })




def show_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)
    choice=input("Enter your answer (A/B/C/D): ").upper()
    return choice

def check_answer(user_choice,correct_answer):
    if user_choice==correct_answer:
        print("correct answer")
        return 1
    else:
        print("Wrong Answer")
        return 0
    
def admin_menu():
    while True:
        print("\n Welcome to admin menu")
        print("1.Add Question")
        print("2.view questions")
        print("3.Back to main menu")
        choice=input("enter your choice: ")
        if choice=="1":
            add_question()
        elif choice=="2":
            view_question()
        elif choice=="3":
            break
        else:
            print("Invalid choice")

def start_quiz():
    if len(questions)==0:
        print("NO Questions Avilable")
        return
    name=input("\n ENTER YOUR GOOD NAME: " )
    score=0
    for q in questions:
        user_choice=show_question(q)
        marks=check_answer(user_choice,q["answer"])
        score=score + marks
    show_result(name,score,len(questions))



def main_menu():
    while True:
        print("\n ==============QUIZ MANAGEMENT SYSTEM==================")
        print("1.Admin Panel")
        print("2.Start Quiz")
        print("3.Leaderboard")
        print("4.exit")

        choice=input("enter your choice:")
        if choice=="1":
            password = input("Enter Admin Password: ")
            if password == "admin123":
                admin_menu()
            else:
                print("Access Denied")
 
        elif choice=="2":
            start_quiz()
        elif choice=="3":
            show_Leaderboard()
        elif choice=="4":
            print("\n Thank you for using quiz system")
            break
        else:
            print("INVALID CHOICE!!")


main_menu()