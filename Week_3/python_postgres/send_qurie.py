from manage_connections import connection

class Person:

    def __init__(self, person_id, first_name, last_name):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"person_id = {self.person_id}, first_name = {self.first_name}, last_name = {last_name}

    def create_person_entry(person: Person):
            #create sql entry
            sql = "insert into persons values(default,%s, %s) returning person_id"
            #create cursor object to handle our query
            cursor = connection.cursor()
            #have cursor object send query to database
            cursor.execute(sql, (person.first_name, person.last_name))
            #commit our query
            connection.commit()
            #end our function
            new_id = cursor.fetchone()[0] #come in tuples
            person.person_id = new_id
            return person

            my_person = Person(0, "Samantha", "Wathen")
            create_person_entry(my_person)

    def get_single_person_record(person_id):
        sql = "select * from persons where person_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [person_id])
        person_record = cursor.fetchone()
        person = Person(* person_record)
        person = Person(person_record[0]. person_record[1], person_record[2])
        return person

    print(get_single_person_record(1)

          def get_all_person_recors(self):
        sql ="select * from persons"
        cursor = connections.cursor()
        cursor.execute(sql)
        persons_record = cursor.fetchall()
        person_list = [])
        for record in person_records:
            person = Person(*record)
            person_list.append(person)
        return person_list

    for person in get_all person_records():
        print(person)

    def update_person_record(person):
        sql = "updatepersons set first_name= %s, last_name = %s where person_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (person.first_name, person.last_name, person.person_id))
        connection.commit()
        #return person
        #return True
        return "Person updated successfully"

    update_into = Person(5, "Evil", "Bob")
    print(update_person_record(updated_info))

    def delete_person_record(person_id):
        sql = "delete from persons wher person_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [person_id])
        connection.commit()
        return True

    print(delete_person_record(5))













    def service_create_person(person):
        if type(person.first_name) == str and type(person.last_name == str:
            result = create_person_entry(person)
            return result
        else:
            return "some error message"

    app.rout("/person", methosd=[POST"]"])
def create_person_from_json():
    person_data = (request.args)person = Person(person_data["personId"])
    persont_data



    )

