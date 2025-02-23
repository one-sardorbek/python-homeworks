a=0
while a!=6:
    print("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit")
    a=int(input())
    if a==1:
        with open('employees.txt', 'a') as file:
            if file.tell()==0:
                records=input()
                file.write(records)
            else:
                with open('employees.txt', 'r') as file:
                    file.read()
                with open('employees.txt', 'a') as file:
                    records=input()
                    file.write("\n")
                    file.write(records)
    elif a==2:
        with open('employees.txt', 'r') as file:
            k=file.read()
            if len(k)==0:
                print("No data found")
            else:
                print(k)
            file.seek(0)
    elif a==3:
        with open('employees.txt', 'r') as file:
            id=input()
            lines=file.readlines()
            for line in lines:
                if id in line:
                    print(line)
    elif a==4:
        with open('employees.txt', 'r') as file:
            file_content=file.read()
            file.seek(0)
            id=input("id: ")
            lines=file.readlines()
            for line in lines:
                if id in line:
                    l=[]
                    m=0
                    old_line=line
                    for i in range(len(line)):
                        if line[i]==",":
                            l.append(line[m:i])
                            m=i+1
                    l.append(line[m:])
                    change=int(input("Select what do you want to change:\n1 : Name\n2 : Position\n3 : Salary\n"))
                    if change==1:
                        change_input=input("write the new name: ")
                        l[1]=change_input
                    elif change==2:
                        change_input=input("write the new position: ")
                        l[2]=change_input
                    elif change==3:
                        change_input=input("write the new salary: ")
                        l[3]=change_input
                     
                    new_line=""
                    for item in l:
                        if l[-1]==item:
                            new_line=new_line+item
                        else:
                            new_line=new_line+item+", "
        file_content=file_content.replace(old_line, new_line)
        with open('employees.txt', 'w') as file:
            file.write(file_content)
            file.seek(0)  
    elif a==5:
        with open('employees.txt', 'r') as file:
            file_content=file.read()
            file.seek(0)
            id=input("id: ")
            lines=file.readlines()
            for line in lines:
                if id in line:
                    old_line=line
        file_content=file_content.replace(old_line, "")
        with open('employees.txt', 'w') as file:
            file.write(file_content)
            file.seek(0) 
    elif a>5:
        print("Please select the options only 1-6") 
