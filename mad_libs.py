print("welcome to your story game")

#The first 4 lines are questions to the users.
name = input("What is your name?\n")
animal = input("What is your favourite animal?\n")
place = input("where do you like going?\n")
action = input("give me an action ending with ing\n")

#Here you write your story with the things you put in the first 4 lines
story = f"One day,{name} met a {animal} in the {place}. They started {action} together."
ending = f"It was the funniest day {name} could remember!"

#Here the computer is printing your story!
print("\n ---- your story ---- here")
print(story+"\n"+ending)

#This saves your story to the file
with open("story.txt", "a", encoding="utf-8") as myfile:
    myfile.write("\nmy amazing adventure\n")
    myfile.write(story+"\n"+ending)
print("I saved your story to the file story.txt")