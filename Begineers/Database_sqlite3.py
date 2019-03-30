import sqlite3

def insert_record():
	get_id = input('\n Enter ID : ')
	get_name = input(' Enter Name : ').lower()
	get_age = int(input(' Enter Age : '))
	get_salary = float(input(' Enter Salary : '))
	conn.execute("insert into student values({}, {}, {}, {})".format(get_id, str(get_name), get_age, get_salary))
	conn.commit()
	print("\n New Record Inserted Sucessfully...")
    
def display_record():
	print('\n*** Displaying Records *** \n')
	view = conn.execute("select * from student")
	for i in view:
		print("Id : "+str(i[0])+"\t Name : "+str(i[1])+"\t Age : "+str(i[2])+"\t Salary : "+str(i[3]))

def update_record():
	get_id = int(input(" Enter Existing ID to update new name in STUDENT Table : "))
	new_name = input(" Enter New Name : ")
	conn.execute("update student set name = '{}' where id = {}".format(new_name, get_id))
	conn.commit()
	print("\n Old Record Updated Sucessfully...")

def delete_record():
	get_id = int(input(" Enter Existing ID to Delete Record in STUDENT Table : "))
	conn.execute("delete from student where id = {}".format(get_id))
	conn.commit()
	print("\n Old Record Deleted Sucessfully...")


if __name__ == '__main__':
	print("\n *** SQlite3 Using Python *** \n")
	# Create New Database called test
	conn = sqlite3.connect("test.db")
	print(" Opened Database Sucessfully..")
	# Create New Table from Database
	conn.execute("create table if not exists student(id int not null, name varchar, age int, salery real)")
	print("\n Student Table Created sucessfully..")

	while True:
		print('\n MainMenu \n 1. Insert New Record \n 2. Delete New Record \n 3. Display All Records \n 4. Update Exsiting Record \n 5. Exit \n')
		choice = int(input(' Enter Your Choice (1-5): '))
		if choice == 1:
			insert_record()
		elif choice == 2:
			delete_record()
		elif choice == 3:
			display_record()
		elif choice == 4:
			update_record()
		elif choice == 5:
			exit(0)
		else:
			print('\n Invalid Choice, Please try again..')
			
	# Close the DB Connection.
	conn.close()





























