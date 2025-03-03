from datetime import datetime
todo={}
while True:
    print(" To do list ".center(30, '-'))
    op = int(input("1.Add 2.View  3.Exit: "))
    if op==1:
        num =int(input("Enter task count : "))
        j=1
        for i in range(num):
            task=input(f" Enter Task : ")
            user_input = input("Enter the time (HH:MM): ")
            scheduled_time = datetime.strptime(user_input, "%H:%M")
            if task not in todo:
                todo.setdefault(task, scheduled_time)
            else:
                todo[task] = scheduled_time
            j=j+1
    if op==2:
        print()
        print(" Task List ".center(30, '◙'))
        if len(todo)==0:
            print("No task found")
        else:
            now = datetime.now()

            count=1
            for k, entered_time in todo.items():
                 # Combine the entered time with today's date
                entered_time_today = now.replace(hour=entered_time.hour, minute=entered_time.minute, second=0, microsecond=0)
                # Calculate the difference
                time_difference = now - entered_time_today if now >= entered_time_today else entered_time_today - now
                index = str(time_difference).find(":", 4)
                print(f"{count}. {k} {str(time_difference)[0:index]} hours is remain to Complete task")
                count=count+1
        print()

    if op==3:
        print("Thank you!")
        break