from getpass import getpass
from mysql.connector import connect, Error

# this spaghettie code was written by Kimberly Mutanga A.K.A Mkaay...

class Views:
    def __init__(self, conn):
        self.connection = conn
        self.cursor = conn.cursor()

        # The queries being executed here are vulnerable to SQL injection attacks.
        # Making use of the bind functions of pyside6 to prevent such attacks but unfortunately i dont have mysql db driver.

        """
            -> The views object is going to store search results for now.
        """

    def update_search_results_tag_id(self, tagId) -> list:
        """
            - Stores the search results when a user searches the animal by breed.
        """
        search_results_sql_1 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE tag_id='{tagId}'"

        self.cursor.execute(search_results_sql_1)
        self.connection.commit()

        # update the table of results in the animal_search_results table

    def update_search_results_breed(self, breed: str):
        """
            - Stores the search results when a user searched the animal by its tag id.
        """
        search_results_sql_2 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE breed='{breed}'"

        self.cursor.execute(search_results_sql_2)
        self.connection.commit()

    def update_search_results_breed_and_animal_sex(self, breed: str, animalSex: str):
        """
            - Updates the search_results view with the animal that has the sex and breed provided in the parameters.
        """
        animal_sex = {"male": 1, "female": 0}
        search_results_sql = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE breed='{breed}' AND sex={animal_sex[animalSex]}"
        self.cursor.execute(search_results_sql)
        self.connection.commit()

    def update_search_results_breed_and_department(self, department: str, breed: str):
        """
            - Updates the search_results view with the animal that has the separtment and breed provided in the parameters.
        """

        search_results_sql = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE department='{department}' AND breed='{breed}'"
        self.cursor.execute(search_results_sql)
        self.connection.commit()

    def update_search_results_breed_sex_department(self, breed: str, sex: bool, department: str):
        search_results = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE department='{department}' AND sex={sex} AND breed='{breed}'"
        self.cursor.execute(search_results)
        self.connection.commit()

    def update_search_results_department(self, department: str):
        """
            - Updates the animal search view with the current department parameters.
        """
        search_results_sql_3 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE department='{department}'"

        self.cursor.execute(search_results_sql_3)
        self.connection.commit()

    def update_search_results_animal_sex(self, animalSex: str):
        """
            - Updates the animal search view with the current animal sex parameters.
        """
        animal_sex = {"male": 1, "female": 0}
        search_results_sql_4 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE sex={animal_sex[animalSex]}"

        self.cursor.execute(search_results_sql_4)
        self.connection.commit()

    def update_search_results_animal_sex_department(self, animalSex: str, department: str):
        """
            - Updates the search_results view with the animal that has the sex and department given.
        """

        animal_sex = {"male": 1, "female": 0}
        print("sex: ", animalSex)
        print("department: ", department)
        search_results_sql_5 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE sex={animal_sex[animalSex]} AND department='{department}'"

        self.cursor.execute(search_results_sql_5)
        self.connection.commit()

    def update_search_results_all(self, searchBarData: str):
        """
            - Updates the animal search view with the current search bar parameters.
        """

        parameters_sql = f"tag_id LIKE '%{searchBarData}%' OR breed LIKE '%{searchBarData}%' OR department LIKE '%{searchBarData}%'"
        search_results_sql_4 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE {parameters_sql}"

        self.cursor.execute(search_results_sql_4)
        self.connection.commit()


class Connection:
    def __init__(self, host='localhost', username='root', password="citrus145"):
        self.host = host
        self.username = username
        self.password = password

        # other variables 
        self.connection_error = ''
        self.failed = True
        # try connecting to the database 
        try:
            self.connection = connect(
                host=self.host,
                user=self.username,
                password=self.password,  # do not hardcode your pass word in the code!
                database='agroiq_smartfarming_suite'
            )
            # create the connection cursor 
            self.cursor = self.connection.cursor()
            # search results table for the animal
            self.search_results = Views(self.connection)

        except Error as e:
            self.connection_error = e
            self.failed = False

    def error(self) -> bool:
        # print the connection error 
        print("[CONN ERROR]: ", self.connection_error)
        return self.failed

    def getConn(self):
        return self.connection

    def logIn(self, logInData: list) -> list:
        # input parameter format: logInData = [farm_id, password]
        # returns [succsesfull_login: bool, farm_id_count: int, password_count: int]

        # selects the number of users with the given farm id and password, using it for validating passwords 
        sql = f" SELECT user_password FROM Users WHERE farm_id='{logInData[0]}'"
        # selects the number of users with the given farm id in the database 
        sql1 = f"SELECT COUNT(*) FROM Users WHERE farm_id='{logInData[0]}';"
        cursor = self.connection.cursor()

        cursor.execute(sql)
        result = cursor.fetchone()

        cursor.execute(sql1)
        result1 = cursor.fetchone()
        # THIS WILL NEEED A REWRITE LATER ON.

        # print(result[0], ": ", result1[0])
        # result1[0] contains the number of existing farm ids in the database that match the one provided by the user.
        # result[0] contains the number of passwords in the database that have the corresponding farm id-
        # and password provided by the user, used to check if the password is correct.

        if result1[0] != 1:
            # print("farm id invalid or is not in our database")
            return [False, result1[0], ""]

        # elif result[0] != 1:
        #     # print("invalid password..!")
        #     return [False, result1[0], result[0]]  
        else:
            return [True, result1[0], result[0]]

    def getUserDetails(self, farmId) -> list:
        # check if the user already exists.
        does_user_exist_sql = f"SELECT COUNT(*) FROM Employees WHERE farm_id='{farmId}';"
        cursor = self.connection.cursor()
        cursor.execute(does_user_exist_sql)
        does_user_exist = cursor.fetchone()
        print(does_user_exist[0])

        if does_user_exist[0] == 1:
            user_details_sql = f"SELECT first_name, last_name FROM Employees WHERE farm_id='{farmId}'"
            cursor = self.connection.cursor()
            cursor.execute(user_details_sql)
            user_details = cursor.fetchone()
            # print(user_details[0], user_details[1])
            return user_details
        else:
            # print("user not in database")
            return [""]

    def register(self, registrationData: list) -> list:
        # add all the provided information to the database  
        # it will return a list of the format: booleans [
        # does_user_exist,
        # user_is_registered,
        # is_admin 
        # ]
        # check if the user already exists.
        does_user_exist_sql = f"SELECT COUNT(*) FROM Employees WHERE farm_id='{registrationData[2]}';"
        cursor = self.connection.cursor()
        cursor.execute(does_user_exist_sql)
        does_user_exist = cursor.fetchone()
        print(does_user_exist[0])

        # check if an Employee is already registered as a suite user
        user_is_registered_sql = f"SELECT COUNT(*) FROM Users WHERE farm_id='{registrationData[2]}'"
        cursor.execute(user_is_registered_sql)
        user_is_registered = cursor.fetchone()
        print(user_is_registered)

        # check if the user has admin privileges.
        is_admin_sql = f"SELECT suite_user FROM Employees WHERE farm_id='{registrationData[2]}'"
        cursor.execute(is_admin_sql)
        is_admin = cursor.fetchone()

        if does_user_exist[0] >= 1:
            # print(f"user with the farm id {registrationData[0]} does not exist")
            return [does_user_exist[0], user_is_registered[0], is_admin[0]]
        else:
            return [does_user_exist[0], user_is_registered[0], 0]

    def add_user_data_to_database(self, user_data: list):
        # before uploading the data i need to hash the passwords first 
        add_data_sql = f"INSERT INTO Users VALUES('{user_data[0]}', '{user_data[1]}')"
        cursor = self.connection.cursor()
        cursor.execute(add_data_sql)
        self.connection.commit()

    def addVaccinationData(self, data: dict):
        sql = f"INSERT INTO vaccination_history VALUES('{data["cattle_id"]}', '{data["vaccine_name"]}', '{data["dosage_mg"]}', '{data["date_vaccinated"]}', '{data["reason"]}', '{data["organization"]}')"
        cursor = self.connection.cursor()
        
        cursor.execute(sql)

        self.connection.commit()

    def addAnimalHealthHistory(self, data: dict):
        # {"tag_id": "C0001", "disease": "Foot-and-Mouth Disease", "disease_description": "Highly contagious viral disease affecting cloven-hoofed animals.", "symptoms": ["fever", "blisters", "lameness"], "date_infected": "2021-02-10T00:00:00"}
        sql = f"INSERT INTO health_history VALUES('{data["tag_id"]}', '{data["disease"]}', '{data["disease_description"]}', '{" ".join(data["symptoms"])}', '{data["date_infected"]}')"
        cursor = self.connection.cursor()

        cursor.execute(sql)
        self.connection.commit()

    # add new animal data 
    def addAnimal(self, data: dict) -> bool:
        # {"id": "C0001", "breed": "Angus", "age_months": 24, "weight_kg": 450.3, "sex": "Female", "unique_characteristics": "Docile temperament, High milk yield", "department": "Milk Production"},
        # THE FORMAT OF THE DATA IN THE data parameter will be 
        # [tag_id, breed, age_in_months, weight_in_kgs, sex, unique_characteristics, department]
        gender = {"Female": 0, "Male": 1}
        add_animal_data_sql = f"INSERT INTO animal VALUES('{data["id"]}', '{data["breed"]}', '{data["age_months"]}', '{data["weight_kg"]}', {gender[data["sex"]]}, '{data["unique_characteristics"]}', '{data["department"]}')"
        check_if_animal_present_sql = f"SELECT COUNT(*) FROM animal WHERE tag_id='{data["id"]}'"

        # first check if animal data has been submitted 
        cursor = self.connection.cursor()
        cursor.execute(check_if_animal_present_sql)
        check_if_animal_present = cursor.fetchone()
        print(check_if_animal_present)
        if check_if_animal_present[0] >= 1:
            return False
        else:
            # add the animal data to the database 
            cursor.execute(add_animal_data_sql)
            # commit the changes 
            self.connection.commit()
            return True

    def updateAnimal(self, sql: str):
        cusor = self.connection.cursor()
        cusor.execute(sql)
        self.connection.commit()

    def searchForDisease(self, filterParameters: list) -> list:

        data_cache_dict = {
            "search bar input": filterParameters[0],
        }

        cursor = self.connection.cursor()

        sql_item_count = (f"SELECT COUNT(*) FROM health_history WHERE "
                          f"tag_id LIKE '%{data_cache_dict["search bar input"]}%' "
                          f"OR "
                          f"disease LIKE '%{data_cache_dict["search bar input"]}%'"
                          )

        cursor.execute(sql_item_count)
        search_result_count = cursor.fetchone()

        sql_data_fetch = (f"SELECT * FROM health_history WHERE "
                          f"tag_id LIKE '%{data_cache_dict["search bar input"]}%' "
                          f"OR "
                          f"disease LIKE '%{data_cache_dict["search bar input"]}%'"
                          )

        cursor.execute(sql_data_fetch)
        search_result_data = cursor.fetchall()

        return [search_result_data, search_result_count[0]]

    def searchForVaccinationHistory(self, filterParameters: list) -> list:

        data_cache_dict = {
            "search bar input": filterParameters[0]
        }

        cursor = self.connection.cursor()

        sql_item_count = (f"SELECT COUNT(*) FROM vaccination_history WHERE "
                          f"tag_id LIKE '%{data_cache_dict["search bar input"]}%' "
                          f"OR "
                          f"vaccine_name LIKE '%{data_cache_dict["search bar input"]}%'"
                          )

        cursor.execute(sql_item_count)
        search_result_count = cursor.fetchone()

        sql_data_fetch = (f"SELECT * FROM vaccination_history WHERE "
                          f"tag_id LIKE '%{data_cache_dict["search bar input"]}%' "
                          f"OR "
                          f"vaccine_name LIKE '%{data_cache_dict["search bar input"]}%'"
                          )

        cursor.execute(sql_data_fetch)
        search_result_data = cursor.fetchall()

        return [search_result_data, search_result_count[0]]

    def selectAllHealthHistory(self) -> list:
        sql = f"SELECT * FROM health_history"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        search_results = cursor.fetchall()
        return search_results

    def selectAllVaccinationHistory(self) -> list:
        sql = f"SELECT * FROM vaccination_history"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        search_results = cursor.fetchall()
        return search_results
    
    def fetchAllAnimalData(self) -> list:
        sql = "SELECT * FROM animal"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        return results
    
    def addVetAppointment(self, data: dict):
        # first insert the data in the notificaions table
        sql_notifications = f"INSERT INTO notifications VALUES('{data["date_set"]}', '{data["date_end"]}', '{data["notification_id"]}')"
        sql_vet_appointments = f"INSERT INTO vet_appointments VALUES('{data["purpose"]}', '{data["notification_id"]}', '{data["organization"]}', '{data["is_queued"]}')"

        cursor = self.connection.cursor()
        cursor.execute(sql_notifications)
        self.connection.commit()

        cursor.execute(sql_vet_appointments)
        self.connection.commit()

    def searchForAnimal(self, filterParameters: list) -> list:
        # select all the animals in the database with the parameters provided.
        data_cache_dict = {
            "animal breed radio": filterParameters[0],
            "Tag Id radio": filterParameters[1],
            "animal sex": filterParameters[2],
            "department": filterParameters[3],
            "animal sex or department checkbox": filterParameters[4],  # bool
            "search bar data": filterParameters[5],
            "sex combo box data": filterParameters[6],
            "department combo box data": filterParameters[7],
            "filters disabled": filterParameters[8]
        }

        # the cursor 
        cursor = self.connection.cursor()
        if not data_cache_dict["filters disabled"]:
            if data_cache_dict["animal breed radio"] and not data_cache_dict[
                "animal sex or department checkbox"] and not data_cache_dict["Tag Id radio"]:

                # if the user wants to search animal by breed only 
                search_query_sql_0 = f"SELECT * FROM animal WHERE breed='{data_cache_dict['search bar data']}'"

                print(data_cache_dict["search bar data"])
                cursor.execute(search_query_sql_0)

                result_0 = cursor.fetchall()

                self.search_results.update_search_results_breed(data_cache_dict["search bar data"])
                if len(result_0) < 1:
                    return result_0
                else:
                    return result_0

            elif data_cache_dict["Tag Id radio"] and not data_cache_dict["animal sex or department checkbox"] and not \
                    data_cache_dict["animal breed radio"]:
                # when the user wants to search by tag id
                search_query_sql_1 = f"SELECT * FROM animal WHERE tag_id='{data_cache_dict['search bar data']}'"
                cursor.execute(search_query_sql_1)

                result_1 = cursor.fetchall()

                # update the search results table 
                self.search_results.update_search_results_tag_id(data_cache_dict['search bar data'])

                if len(result_1) < 1:
                    return result_1
                else:
                    return result_1


            # using animal breed 
            elif data_cache_dict["animal breed radio"] and data_cache_dict["animal sex or department checkbox"] and \
                    data_cache_dict["animal sex"] and not data_cache_dict["department"]:
                # when user searches by animal breed and animal sex
                animal_sex = {"male": 1, "female": 0}
                search_query_sql_2 = f"SELECT * FROM animal WHERE breed='{data_cache_dict['search bar data']}' AND sex={animal_sex[data_cache_dict['sex combo box data']]}"
                cursor.execute(search_query_sql_2)
                result_2 = cursor.fetchall()
                self.search_results.update_search_results_breed_and_animal_sex(data_cache_dict["search bar data"],
                                                                               data_cache_dict["sex combo box data"])

                if len(result_2) < 1:
                    return result_2
                else:
                    return result_2

            elif data_cache_dict["animal breed radio"] and data_cache_dict["animal sex or department checkbox"] and \
                    data_cache_dict["department"] and not data_cache_dict["animal sex"]:
                # when user searches by animal department and animal breed
                search_query_sql_3 = (f"SELECT * FROM animal WHERE breed='{data_cache_dict['search bar data']}' AND "
                                      f"department='{data_cache_dict['department combo box data']}'")
                cursor.execute(search_query_sql_3)

                result_3 = cursor.fetchall()

                self.search_results.update_search_results_breed_and_department(data_cache_dict["department combo box "
                                                                                               "data"],
                                                                               data_cache_dict["search bar data"])
                if len(result_3) < 1:
                    return result_3
                else:
                    return result_3

            elif data_cache_dict["animal breed radio"] and data_cache_dict["animal sex or department checkbox"] and \
                    data_cache_dict["animal sex"] and data_cache_dict["department"]:
                # when user searches by animal breed and sex and department
                animal_sex = {"male": 1, "female": 0}
                search_query_sql_4 = f"SELECT * FROM animal WHERE breed='{data_cache_dict['search bar data']}' AND department='{data_cache_dict['department combo box data']}' AND sex={animal_sex[data_cache_dict['sex combo box data']]}"
                cursor.execute(search_query_sql_4)

                result_4 = cursor.fetchall()

                self.search_results.update_search_results_breed_sex_department(data_cache_dict["search bar data"],
                                                                               animal_sex[data_cache_dict[
                                                                                   'sex combo box data']],
                                                                               data_cache_dict[
                                                                                   "department combo box data"])

                if len(result_4) < 1:
                    return result_4
                else:
                    return result_4

            # for tag id 
            elif data_cache_dict["Tag Id radio"] and data_cache_dict["animal sex or department checkbox"] and \
                    data_cache_dict["animal sex"] and not data_cache_dict["department"]:
                # when user searches by animal tag id and animal sex
                animal_sex = {"male": 1, "female": 0}
                search_query_sql_5 = f"SELECT * FROM animal WHERE tag_id='{data_cache_dict['search bar data']}' AND sex={animal_sex[data_cache_dict['sex combo box data']]}"
                cursor.execute(search_query_sql_5)
                result_5 = cursor.fetchall()

                sql_search_results = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE sex={animal_sex[data_cache_dict['sex combo box data']]} AND tag_id='{data_cache_dict['search bar data']}'"
                cursor.execute(sql_search_results)
                self.connection.commit()

                return result_5

            elif data_cache_dict["Tag Id radio"] and data_cache_dict["animal sex or department checkbox"] and \
                    data_cache_dict["department"] and not data_cache_dict["animal sex"]:
                # when user searches by animal department and animal tag id
                search_query_sql_6 = f"SELECT * FROM animal WHERE tag_id='{data_cache_dict['search bar data']}' AND department='{data_cache_dict['department combo box data']}'"
                cursor.execute(search_query_sql_6)

                result_6 = cursor.fetchall()

                sql_search_results_1 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE department='{data_cache_dict['department combo box data']}' AND tag_id='{data_cache_dict['search bar data']}'"
                cursor.execute(sql_search_results_1)
                self.connection.commit()

                return result_6

            elif data_cache_dict["Tag Id radio"] and data_cache_dict["animal sex or department checkbox"] and \
                    data_cache_dict["animal sex"] and data_cache_dict["department"]:
                # when user searches by animal tag id and sex and department
                animal_sex = {"male": 1, "female": 0}
                search_query_sql_7 = f"SELECT * FROM animal WHERE tag_id='{data_cache_dict['search bar data']}' AND department='{data_cache_dict['department combo box data']}' AND sex={animal_sex[data_cache_dict['sex combo box data']]}"
                cursor.execute(search_query_sql_7)

                result_7 = cursor.fetchall()

                sql_search_results_2 = f"CREATE OR REPLACE VIEW search_results AS SELECT * FROM animal WHERE sex={animal_sex[data_cache_dict['sex combo box data']]} AND tag_id='{data_cache_dict['search bar data']}' AND department='{data_cache_dict['department combo box data']}'"
                cursor.execute(sql_search_results_2)
                self.connection.commit()

                return result_7

        elif data_cache_dict["filters disabled"] and data_cache_dict["animal sex or department checkbox"]:
            # search by department only 
            if data_cache_dict["department"] and not data_cache_dict["animal sex"]:
                print(f"filter by department : sex={data_cache_dict['animal sex']}")
                search_query_sql_8 = f"SELECT * FROM animal WHERE department='{data_cache_dict['department combo box data']}'"
                cursor.execute(search_query_sql_8)
                result_8 = cursor.fetchall()
                self.search_results.update_search_results_department(data_cache_dict["department combo box data"])

                return result_8

            elif data_cache_dict["animal sex"] and not data_cache_dict["department"]:
                print("filter by sex")
                sex_data = {"male": 1, "female": 0}
                search_query_sql = f"SELECT * FROM animal WHERE sex='{sex_data[data_cache_dict["sex combo box data"]]}'" 
                cursor.execute(search_query_sql)
                results = cursor.fetchall()
                print(f"search results sex {results}")
                
                self.search_results.update_search_results_animal_sex(data_cache_dict["sex combo box data"])
                return results
            
            elif data_cache_dict["animal sex"] and data_cache_dict["department"]:
                print("filter by sex and department")
                search_query_sql = f"SELECT * FROM animal WHERE sex='{sex_data[data_cache_dict["sex combo box data"]]}' AND department='{data_cache_dict["department combo box data"]}'"
                cursor.execute(search_query_sql)
                results = cursor.fetchall()
                print(f"search results dep and sex={results}")
                self.search_results.update_search_results_animal_sex_department(data_cache_dict["sex combo box data"],
                                                                                data_cache_dict[
                                                                                    "department combo box data"])
                
                return results


        elif data_cache_dict["filters disabled"] and not data_cache_dict["animal sex or department checkbox"]:

            # if data_cache_dict["search bar data"] == "":
            #     # clear the view 
            #     self.search_results.update_search_results_all("  ")
            #     parameters_sql = f"tag_id LIKE '%{"  "}%' OR breed LIKE '%{"  "}%' OR department LIKE '%{"  "}%'"
            #     search_results_sql_4 = f"SELECT * FROM animal WHERE {parameters_sql}"

            #     cursor.execute(search_results_sql_4)

            #     search_res = cursor.fetchall()
            #     return search_res

            # else:
            # the default filter parameters allows us to fetch all records with the provides parameters.
            self.search_results.update_search_results_all(data_cache_dict["search bar data"])


            searchBarData = data_cache_dict["search bar data"]
            parameters_sql = f"tag_id LIKE '%{searchBarData}%' OR breed LIKE '%{searchBarData}%' OR department LIKE '%{searchBarData}%'"
            search_results_sql_4 = f"SELECT * FROM animal WHERE {parameters_sql}"
            cursor.execute(search_results_sql_4)

            search_results = cursor.fetchall()
            print("animal search view updated..!")
            return search_results

    def getViewData(self) -> list:
        search_query_sql_9 = f"SELECT * FROM search_results"
        cursor = self.connection.cursor()

        cursor.execute(search_query_sql_9)

        result_9 = cursor.fetchall()

        return result_9

cn = Connection()

# # search_res = Views(cn.getConn())
# # search_res.update_search_results_tag_id("1024")

# sex = {"male": True, "female": False}
# cn.searchForAnimal([
#     False, # filter by breed 
#     False, # filter by tag id
#     False, # filter by sex 
#     False,     # filter by department
#     False, # animal or sex department checkbox
#     "d", # search bar data
#     "",
#     'r',
#     True
# ])

# print(cn.getViewData())

# if not cn.addAnimal([
#     "1024", 
#     "Brahman",
#     0.0,
#     0.0,
#     False,
#     "",
#     "breeding"
# ]):
#     print("id is already available.")
# print(cn.logIn(['24680', 'Citrus145']))
# cn.getUserDetails("12345")
# print(cn.register(['24680', 'asfsfsf', '12345', 'sdfsdfsdfs']))


cattle_health_history = [
    {"tag_id": "C0001", "disease": "Foot-and-Mouth Disease", "disease_description": "Highly contagious viral disease affecting cloven-hoofed animals.", "symptoms": ["fever", "blisters", "lameness"], "date_infected": "2021-02-10T00:00:00"},
    {"tag_id": "C0002", "disease": "Bovine Tuberculosis", "disease_description": "Chronic bacterial infection caused by Mycobacterium bovis.", "symptoms": ["weight loss", "cough", "lethargy"], "date_infected": "2022-06-18T00:00:00"},
    {"tag_id": "C0003", "disease": "Mastitis", "disease_description": "Inflammation of the mammary gland due to infection.", "symptoms": ["swollen udder", "pain", "reduced milk"], "date_infected": "2020-09-05T00:00:00"},
    {"tag_id": "C0004", "disease": "Respiratory Disease", "disease_description": "Complex of respiratory infections in cattle.", "symptoms": ["nasal discharge", "fever", "labored breathing"], "date_infected": "2023-01-22T00:00:00"},
    {"tag_id": "C0005", "disease": "Anthrax", "disease_description": "Acute disease caused by Bacillus anthracis.", "symptoms": ["sudden death", "bloody discharge", "high fever"], "date_infected": "2021-07-30T00:00:00"},
    {"tag_id": "C0006", "disease": "Brucellosis", "disease_description": "Bacterial infection causing reproductive issues.", "symptoms": ["abortion", "infertility", "joint pain"], "date_infected": "2022-11-11T00:00:00"},
    {"tag_id": "C0007", "disease": "Lumpy Skin Disease", "disease_description": "Viral disease causing nodules on skin.", "symptoms": ["skin lumps", "fever", "loss of appetite"], "date_infected": "2020-03-14T00:00:00"},
    {"tag_id": "C0008", "disease": "Blackleg", "disease_description": "Bacterial infection causing muscle necrosis.", "symptoms": ["swelling", "lameness", "fever"], "date_infected": "2023-05-02T00:00:00"},
    # {"tag_id": "C0009", "disease": "Johne's Disease", "disease_description": "Chronic intestinal infection.", "symptoms": ["diarrhea", "weight loss", "reduced milk"], "date_infected": "2021-10-19T00:00:00"},
    {"tag_id": "C0010", "disease": "Viral Diarrhea", "disease_description": "Viral disease affecting digestion.", "symptoms": ["diarrhea", "fever", "nasal discharge"], "date_infected": "2022-12-01T00:00:00"},
    {"tag_id": "C0011", "disease": "Pinkeye", "disease_description": "Contagious eye infection.", "symptoms": ["eye redness", "tearing", "swelling"], "date_infected": "2020-06-07T00:00:00"},
    {"tag_id": "C0012", "disease": "Leptospirosis", "disease_description": "Bacterial infection from contaminated water.", "symptoms": ["fever", "abortion", "jaundice"], "date_infected": "2023-03-16T00:00:00"},
    {"tag_id": "C0013", "disease": "Parainfluenza", "disease_description": "Respiratory virus in cattle.", "symptoms": ["coughing", "nasal discharge", "fever"], "date_infected": "2021-11-03T00:00:00"},
    {"tag_id": "C0014", "disease": "Ringworm", "disease_description": "Fungal skin infection.", "symptoms": ["hair loss", "itching", "scaly patches"], "date_infected": "2022-08-27T00:00:00"},
    {"tag_id": "C0015", "disease": "Leukosis", "disease_description": "Viral disease causing tumors.", "symptoms": ["weight loss", "enlarged lymph nodes", "weakness"], "date_infected": "2020-12-12T00:00:00"},
    {"tag_id": "C0016", "disease": "Salmonellosis", "disease_description": "Bacterial infection causing diarrhea.", "symptoms": ["diarrhea", "fever", "dehydration"], "date_infected": "2023-06-20T00:00:00"},
    {"tag_id": "C0017", "disease": "Herpesvirus", "disease_description": "Virus causing respiratory and reproductive issues.", "symptoms": ["nasal discharge", "abortion", "fever"], "date_infected": "2021-01-29T00:00:00"},
    {"tag_id": "C0018", "disease": "Coccidiosis", "disease_description": "Parasitic intestinal infection.", "symptoms": ["bloody diarrhea", "weight loss", "lethargy"], "date_infected": "2022-10-05T00:00:00"},
    {"tag_id": "C0019", "disease": "Anaplasmosis", "disease_description": "Tick-borne disease affecting red blood cells.", "symptoms": ["anemia", "fever", "weakness"], "date_infected": "2020-04-21T00:00:00"},
    {"tag_id": "C0020", "disease": "Actinomycosis", "disease_description": "Chronic bacterial infection causing abscesses.", "symptoms": ["swelling", "pus", "difficulty eating"], "date_infected": "2023-02-14T00:00:00"},
    {"tag_id": "C0021", "disease": "Enterotoxemia", "disease_description": "Toxin-producing bacteria causing sudden death.", "symptoms": ["abdominal pain", "diarrhea", "collapse"], "date_infected": "2021-09-09T00:00:00"},
    {"tag_id": "C0022", "disease": "Septicemia", "disease_description": "Acute bacterial disease with high mortality.", "symptoms": ["fever", "swelling", "respiratory distress"], "date_infected": "2022-07-01T00:00:00"},
    {"tag_id": "C0023", "disease": "Dermatophilosis", "disease_description": "Skin infection caused by Dermatophilus congolensis.", "symptoms": ["scabs", "hair loss", "itching"], "date_infected": "2020-05-18T00:00:00"},
    {"tag_id": "C0024", "disease": "Babesiosis", "disease_description": "Tick-borne protozoal disease.", "symptoms": ["fever", "jaundice", "anemia"], "date_infected": "2023-04-09T00:00:00"},
    {"tag_id": "C0025", "disease": "Pneumonia", "disease_description": "Inflammation of lungs due to infection.", "symptoms": ["coughing", "labored breathing", "fever"], "date_infected": "2021-12-31T00:00:00"},
    {"tag_id": "C0026", "disease": "Bovine Viral Leukemia", "disease_description": "Retrovirus causing lymphosarcoma.", "symptoms": ["tumors", "weight loss", "weakness"], "date_infected": "2022-01-15T00:00:00"},
    {"tag_id": "C0027", "disease": "Trichomoniasis", "disease_description": "Protozoal reproductive disease.", "symptoms": ["infertility", "abortion", "vaginal discharge"], "date_infected": "2023-07-03T00:00:00"},
    {"tag_id": "C0028", "disease": "Theileriosis", "disease_description": "Tick-borne protozoal disease.", "symptoms": ["fever", "anemia", "swollen lymph nodes"], "date_infected": "2020-08-22T00:00:00"},
    {"tag_id": "C0030", "disease": "Ephemeral Fever", "disease_description": "Short-term viral fever in cattle.", "symptoms": ["fever", "lameness", "stiffness"], "date_infected": "2021-03-12T00:00:00"},
    {"tag_id": "C0031", "disease": "Bovine Spongiform Encephalopathy", "disease_description": "Neurodegenerative disease also known as mad cow disease.", "symptoms": ["loss of coordination", "behavioral changes", "weight loss"], "date_infected": "2022-05-08T00:00:00"},
    {"tag_id": "C0032", "disease": "Bovine Ketosis", "disease_description": "Metabolic disorder due to energy imbalance.", "symptoms": ["loss of appetite", "weight loss", "lethargy"], "date_infected": "2023-07-19T00:00:00"},
    {"tag_id": "C0033", "disease": "Bovine Hypocalcemia", "disease_description": "Calcium deficiency often seen post-calving.", "symptoms": ["muscle tremors", "weakness", "collapse"], "date_infected": "2020-11-03T00:00:00"},
    {"tag_id": "C0034", "disease": "Bovine Acidosis", "disease_description": "Digestive disorder caused by excessive grain intake.", "symptoms": ["diarrhea", "dehydration", "reduced appetite"], "date_infected": "2021-08-14T00:00:00"},
    {"tag_id": "C0035", "disease": "Bovine Laminitis", "disease_description": "Inflammation of hoof tissues.", "symptoms": ["lameness", "swollen hooves", "pain"], "date_infected": "2022-09-27T00:00:00"},
    {"tag_id": "C0036", "disease": "Bovine Endometritis", "disease_description": "Uterine infection post-calving.", "symptoms": ["vaginal discharge", "infertility", "fever"], "date_infected": "2023-02-05T00:00:00"},
    {"tag_id": "C0037", "disease": "Bovine Pyometra", "disease_description": "Accumulation of pus in the uterus.", "symptoms": ["abdominal swelling", "infertility", "fever"], "date_infected": "2020-06-29T00:00:00"},
    {"tag_id": "C0038", "disease": "Bovine Metritis", "disease_description": "Inflammation of the uterus after calving.", "symptoms": ["foul discharge", "fever", "depression"], "date_infected": "2021-10-10T00:00:00"},
    {"tag_id": "C0039", "disease": "Bovine Tetanus", "disease_description": "Neurological disease caused by Clostridium tetani.", "symptoms": ["muscle stiffness", "difficulty chewing", "spasms"], "date_infected": "2022-12-21T00:00:00"},
    {"tag_id": "C0040", "disease": "Bovine Botulism", "disease_description": "Paralytic disease caused by botulinum toxin.", "symptoms": ["paralysis", "difficulty swallowing", "respiratory failure"], "date_infected": "2023-04-30T00:00:00"},
    {"tag_id": "C0041", "disease": "Bovine Neosporosis", "disease_description": "Protozoal disease causing abortion.", "symptoms": ["abortion", "neurological signs", "weak calves"], "date_infected": "2020-07-17T00:00:00"},
    {"tag_id": "C0042", "disease": "Bovine Fascioliasis", "disease_description": "Liver fluke infection.", "symptoms": ["weight loss", "anemia", "jaundice"], "date_infected": "2021-05-25T00:00:00"},
    {"tag_id": "C0043", "disease": "Bovine Trypanosomiasis", "disease_description": "Parasitic disease transmitted by tsetse flies.", "symptoms": ["fever", "anemia", "swollen lymph nodes"], "date_infected": "2022-08-03T00:00:00"},
    {"tag_id": "C0044", "disease": "Bovine Cryptosporidiosis", "disease_description": "Protozoal infection causing diarrhea.", "symptoms": ["watery diarrhea", "dehydration", "weight loss"], "date_infected": "2023-01-11T00:00:00"},
    {"tag_id": "C0045", "disease": "Bovine E. coli Infection", "disease_description": "Bacterial infection affecting the digestive tract.", "symptoms": ["diarrhea", "fever", "weakness"], "date_infected": "2020-09-23T00:00:00"},
    {"tag_id": "C0046", "disease": "Bovine Campylobacteriosis", "disease_description": "Bacterial infection causing reproductive failure.", "symptoms": ["infertility", "abortion", "vaginal discharge"], "date_infected": "2021-12-06T00:00:00"},
    {"tag_id": "C0047", "disease": "Bovine Mycoplasmosis", "disease_description": "Respiratory and reproductive disease caused by Mycoplasma.", "symptoms": ["coughing", "mastitis", "infertility"], "date_infected": "2022-03-18T00:00:00"},
    {"tag_id": "C0048", "disease": "Bovine Chlamydiosis", "disease_description": "Bacterial infection affecting eyes and reproductive system.", "symptoms": ["conjunctivitis", "abortion", "nasal discharge"], "date_infected": "2023-06-01T00:00:00"},
    {"tag_id": "C0049", "disease": "Bovine Toxoplasmosis", "disease_description": "Protozoal infection causing abortion and neurological signs.", "symptoms": ["abortion", "fever", "weakness"], "date_infected": "2020-10-13T00:00:00"},
    {"tag_id": "C0050", "disease": "Bovine Rinderpest", "disease_description": "Eradicated viral disease once fatal to cattle.", "symptoms": ["fever", "diarrhea", "mouth ulcers"], "date_infected": "2021-04-04T00:00:00"}
]


diseases = [
    "Anthrax",
    "Blackleg",
    "Brucellosis",
    "Bovine Respiratory Disease",
    "Bovine Tuberculosis",
    "Bovine Viral Diarrhea",
    "Calf Scours",
    "Contagious Bovine Pleuropneumonia",
    "Cowpox",
    "East Coast Fever",
    "Foot and Mouth Disease",
    "Haemorrhagic Septicaemia",
    "Heartwater",
    "Infectious Bovine Rhinotracheitis",
    "Johne’s Disease",
    "Lumpy Skin Disease",
    "Mastitis",
    "Parasitic Infections",
    "Trypanosomiasis",
    "Anaplasmosis",
    "Clostridial Diseases",
    "Diarrhea and Dysentery",
    "Foot and Hoof Problems"
]

# # # print(cattle_data[0]["id"])
# for x, itm in enumerate(cattle_health_history):
#     # print(f"index {x} animal vaccine data = {itm}")
#     # print(" ".join(cattle_health_history[x]["symptoms"]))
#     cn.addAnimalHealthHistory(cattle_health_history[x])
