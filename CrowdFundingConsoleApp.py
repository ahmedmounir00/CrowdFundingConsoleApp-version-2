from datetime import *
import datetime
import json
class SignUp:
    def __init__(self):
        self.email_list = []
        self.pass_list = []

    def main(self):
        print("*" * 50)
        print("""[1]Registration""")
        print("""[2]Login""")
        print("""[3]Exit""")
        print("*" * 50)

        num = input("Please choose from the list =>")
        if num == "1" or num == "R":
            x = self.reg()
            if bool(x):
                self.Login()
        elif num == "2" or num == "L":
            self.Login()
        elif num == "3" or num == "E":
            print("you select Exit , see you ♥")
            exit(0)
        else:

            print("You enter a wrong option")


    def home_page(self):
        print("*" * 50)
        print("""[1]Create a prject : """)
        print("""[2]Veiw All project : """)
        print("""[3]Edit own project : """)
        print("""[4]Search for a Project : """)
        print("""[5]Delete a project : """)
        print("""press x to Exit : """)
        print("*" * 50)
        no = input("Please choose from the list =>")
        if no == "1":
            self.execute.create_a_project()
        elif no == "2":
            self.execute.view_all_projects()
        elif no == "3":
            self.execute.edit_a_project()
        elif no == "4":
            self.execute.search_for_a_project()
        elif no == "5":
            self.execute.delete_his_own_projects()
        elif no == "x":
            print("you choose Exit")
            exit(0)

    def Login(self):
        log_email = input("write your account : ")
        log_password = input("write your Password : ")
        if log_email in self.email_list and log_password in self.pass_list:
            self.home_page()

    def reg(self):
        fname = input("Please type your first Name => ")
        lname = input("Please type your Last Name => ")
        email = input("Please type your Email ex: am@gmail.com => ")
        password = input("Please type your Password => ")
        con_password = input("Please type your Password again => ")
        mobile_phone = input("Please type your Phone ex: 01010693543 => ")

        def email_validation():
            if "@" in email and "." in email[-1:-5:-1]:
                self.email_list.append(email)
            else:
                raise Exception("error from email")

        def pass_validation():
            if password == con_password:
                self.pass_list.append(password)
            else:
                raise Exception("error from pass")

        def phone_validation():
            if (
                    len(mobile_phone) == 11
                    and mobile_phone.startswith("01")
                    and mobile_phone.isdigit()
            ):
                print("")

            else:
                raise Exception("error from phone")

        try:
            pass_validation()
            phone_validation()
            email_validation()
            print("before login")
            return True
        except ValueError:
            print(ValueError)
            return False


class Execute(SignUp):

    def __init__(self , sign_up_instance):
        super().__init__()
        self.execute = sign_up_instance


    def create_a_project(self):
        title = input("Enter your proj title => ")
        Details = input("Enter your proj details => ")
        total_target = int(input("Enter your total target , should be an integer num => "))
        start_date = input("""Enter Start date , should be "dd-mm-yyyy" => """)
        end_date = input("""Enter End date , should be "dd-mm-yyyy" => """)
        mydict = {
            "title": title,
            "details": Details,
            "total target": total_target,
            "Start date": start_date,
            "End date": end_date,
        }
        file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"

        def file_store():
            file = open(file_path, "a")
            file.write(
                json.dumps(mydict)
            )  # use dumps() to get a JSON string from an object
            file.write("\n")
            file = open(file_path, "r")
            for line in file:
                print(line)

        try:
            valid1 = datetime.datetime.strptime(start_date, "%d-%m-%Y")
            valid1 = datetime.datetime.strptime(end_date, "%d-%m-%Y")
            file_store()
            self.execute.home_page()
        except ValueError:
            print("you entered incorrect date format")
            print(mydict)

    def search_for_a_project(self):
        search_list = []
        file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
        # file = open(file_path, "r")
        with open(file_path, "r") as file:
            for line in file:
                search_reader = json.loads(line)
                search_list.append(search_reader)

        user_date = input("Enter the date to search : ")

        def catch_date():
            found = False
            for search_dict in search_list:
                if (
                        search_dict["Start date"] == user_date
                        or search_dict["End date"] == user_date
                ):
                    print(search_list)
                    found = True
                    self.execute.home_page()

                if not found:
                    print("*" * 60)
                    print("press x to Exit")
                    print("press t to try again")
                    print("*" * 60)
                    user_choice = input("Enter your Choise : ")
                    if user_choice == "t":
                        print(
                            "This date does not represent a project , please try again by press t or press x to Exit "
                        )
                        self.search_for_a_project()
                    elif user_choice == "x":
                        break

        try:
            datetime.datetime.strptime(user_date, "%d-%m-%Y")
            catch_date()
        except ValueError:
            print("This is invalid date format , please try again")
            print("*" * 60)
            print("press x to Exit")
            print("press t to try again")
            print("*" * 60)
            user_choice  = input("Enter your Choise : ")
            if user_choice  == "t":
                print(
                    "This date does not represent a project , please try again by press t or press x to Exit "
                )
                self.search_for_a_project()
            elif user_choice  == "x":
                print("you choose to exit ♥")

    def view_all_projects(self):
        view_list = []
        file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
        file = open(file_path, "r")
        for line in file:
            view_dict = json.loads(line)  # create a Python object from a string
            view_list.append(view_dict)

        print(view_list)

        self.execute.home_page()

    def edit_a_project(self):
        edit_list = []
        file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
        file = open(file_path, "r")
        for line in file:
            reader = json.loads(line)  # create a Python object from a string
            edit_list.append(reader)
        user_title = input("Enter your project's title : ")
        for word in edit_list:
            if word["title"] == user_title:
                print("** your project info is : **")
                print(word)

                key_name = input("Enter the field whose value you want to change : ")
                for key in word:
                    if key == key_name:
                        key_value = input("Enter the new value : ")
                        word[key] = key_value

                        file = open(file_path, "w")
                        for add_dict in edit_list:
                            # wirte an obect in a JSON format to  file
                            json.dump(add_dict, file)
                            file.write("\n")
                        file.close()

                        print("***updated successfully ***")

                        self.execute.home_page()
                else:
                    print("*" * 60)
                    print("press x to Exit")
                    print("press t to try again")
                    print("*" * 60)
                    num = input("Enter your Choise : ")
                    if num == "t":

                        print("key name is not valid  , try again ")
                        self.edit_a_project()
                    elif num == "x":
                        break
            else:
                continue
        else:
            print("*" * 60)
            print("press x to Exit")
            print("press t to try again")
            print("*" * 60)
            num = input("Enter your Choise : ")
            if num == "t":
                print("this project is not in the store , try again ")
                self.edit_a_project()
            elif num == "x":
                print("Exit choise")

    def delete_his_own_projects(self):
        delete_list = []
        file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
        # show the projects from the file
        file = open(file_path, "r")
        for line in file:
            reader_del = json.loads(line)
            delete_list.append(reader_del)

        # search for the project
        user_proj_name = input("please enter your title : ")
        for dict_in_list in delete_list:
            # if title of the proj in our list it will be remove this dict
            if dict_in_list["title"] == user_proj_name:
                delete_list.remove(dict_in_list)

                # update in the JSON file
                file = open(file_path, "w")
                # it will be loop on the deleted list contant
                for add in delete_list:
                    # and add python obect in a JSON format to a file
                    json.dump(add, file)
                    file.write("\n")
                print("***project deleted successfully***")
                file.close()

                self.execute.home_page()
            else:
                continue
        else:
            print("*" * 60)
            print("press x to Exit")
            print("press t to try again")
            print("*" * 60)
            num = input("Enter your Choise : ")
            if num == "t":
                print("this project is not in the store , try again ")
                self.delete_his_own_projects()
            elif num == "x":
                print("Exit choise")


# Initialize SignUp and Execute
sign_up = SignUp()
execute = Execute(sign_up)

# Set the Execute instance in SignUp

sign_up.execute = execute

# Run the main method
sign_up.main()
