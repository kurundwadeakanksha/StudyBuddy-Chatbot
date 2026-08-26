
print("===================================================")
print("              STUDYBUDDY CHATBOT                   ")
print("===================================================")
print("Bot: Hello! I am studyBuddy.")
print("Bot: Type 'bye' to exit.")
while True:   
    message = input("You: ")
    user_message = message.strip().lower()
    if not user_message:
        print("Bot: Please enter a message.")
        continue
    if user_message == "hi":
        print("Hello! How can I help you today?")
    elif user_message == "hello":
        print("Hi there! How can I help you today?")
    elif user_message == "hey":
        print("Hey! What do you need?")
    if "study" in user_message:
        print("Great choice! Let's study together.")
        print("Make a study timetable and study one topic at a time.")
    elif "python" in user_message:
        print("Bot: Practice Python regularly and solve small programs.")
    elif "exam" in user_message:
        print("Bot: Start your preparation early and revise regularly.")
    elif "motivate" in user_message:
        print("Bot: Believe in yourself! Small progress every day.")
    elif "break" in user_message:
        print("Bot: Take a short break and relax your mind.")
    elif user_message in ["bye", "exit"]:
        print("Goodbye!")
        break
else:
     print("Bot: Sorry, I don't understand that question.")
     print("Bot: Try asking about study,python,exams or motivation.")
