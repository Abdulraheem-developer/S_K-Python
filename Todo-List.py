

tasks = []

userInput = -1;

	
	while(userInput != 5):
	   print(" Select an option") 
 	   print("1. Add a task") 
           print("2. View tasks")  
           print("3. Mark task as complete")
           print("4. Delete a task")
           print("5. Exit")
           
		choice = int(input("Select a task: "))
		
		   match(choice):
			case 1: 
				def add_task():
				  task = input("Enter the task:  ").strip()
				  task.append(task)
				  print("task added")
				  return tasks
			
			case 2:
				def view_tasks():
				 if len(tasks) == 0:
				print("There are no tasks ");
				return		
				   else:
					count = 1
					for item in tasks:
					print(f" Task {count}: {task}")
					count += 1

			case 3: 
				def mark_tasks(tasks):
	

							