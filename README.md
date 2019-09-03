# Voice-Assistant-for-Bank

This system is a prototype of grievance redressal system for bank built in python with libraries such as gTTS, google speech recognition and pyttsx3. This system registers a complaint, tracks the complaint and transfers the call to agent.

We haven't connected database yet but lemme tell you how it is going to work.
We will run the program.
It will ask how it can help.
We can give some random commands like tell me a joke or we can directly ask it that help me with my account.
It will then tell us that verification is important for that. So, it will ask us for account number.
Whatever the customer will say will be stored in a account number variable. Then system will check if the same account number exists in database or not. If not exist it will exit the program otherwise it will ask for the registered name. User will answer and again system will lookup in the database. If the name with same account number is found, it will further ask for date of birth. If that too is found, it will say Verification successful and then it will ask weather we want to register a complaint or track a complaint or need an agent.  It will act accordingly then.

If register a complaint command is given, then system will ask to narrate the issue in detail and it will be stored on the server and a token number will be generated and given to user.

https://youtu.be/3loGnelMAo0
