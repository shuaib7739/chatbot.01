import os
class chatbot1:
    def __init__(self,database_file="database.txt"):
        self.database_file = database_file
        if not os.path.exists(self.database_file):
            with open(self.database_file,"w") as f:
                pass
    def learn(self,topic,info):
        topic = topic.strip().lower()
        info = info.strip()
        with open (self.database_file,"a") as f:
            f.write(f"{topic}: {info}\n")
        print(f"thanks! for teaching me about '{topic}'.")
    def recall(self,topic):
        topic = topic.strip().lower()
        if not os.path.exists(self.database_file):
            return"Oops I don't know that yet, can you teach me please"
        with open (self.database_file,"r") as f:
            lines = f.readlines()
        database_dict = {}
        for line in lines:
            line = line.strip()
            if ": " in line:
                stored_topic,stored_info = line.split(": ",1)
                database_dict[stored_topic.lower()]=stored_info
        return database_dict.get(topic,"Oops I don't know that yet, can you teach me please")
    def chat(self):
        print("hey! ask me what I know or teach me something new")
        print("type bye to exit\n")
        while True:
            user_input = input("You: ")
            if user_input in ["bye","exit","quit"]:
              print("byeeeee!")
              break
            elif user_input.startswith("you say"):
                topic = user_input.replace("you say","").strip()
                if topic:
                    info = input(f"what should I know about '{topic}'?")
                    self.learn(topic,info)
                else:
                    print("please specify the topic ")
            else:
                print(f"{self.recall(user_input)}")

bot = chatbot1()
bot.chat()

            