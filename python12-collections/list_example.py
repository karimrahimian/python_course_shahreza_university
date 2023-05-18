names = list()

def addStudent(studentName):
    name_len = len(studentName)
    if (name_len>=3 and name_len <=20):
        names.append(studentName)
        return
    raise Exception("Not valied")
def displayStudent():
    if len(names)==0:
        print("There is no student in the list")
        return
    print("----------Student Names--------------")
    for name in names :
        print(name)
    print("---------End of list ---------------")
def saveStudentInFile():
    with open("students.csv","w") as file:
        for name in names:
            file.write(f"{name}\n")
def loadFromFile():
    with open("students.csv", "r") as file:
        temp_names = file.readlines()
        names.extend([name.replace("\n","") for name in temp_names])
def removeStudent(name):
    names.remove(name)
def main():
    while (True):
        print("1- Add student")
        print("2- Display student")
        print("3- Remove student")
        print("4- Save to file")
        print("5- Load from file")
        print("6- Display unique names")
        user_prompt = int(input("Choose : "))
        if (user_prompt==1):
            name = input("Enter your name :")
            try:
                addStudent(name)
                print("Student added successfully")
            except Exception as err:
                print(err)
        elif (user_prompt == 2):
            displayStudent()
        elif(user_prompt == 4):
            saveStudentInFile()
        elif(user_prompt==5):
            loadFromFile()
        elif(user_prompt == 3):
            name = input("Enter your name :")
            removeStudent(name)
        elif (user_prompt == 6):
            unique_names = set(names)
            print(unique_names)
if __name__ == "__main__":
    main()
