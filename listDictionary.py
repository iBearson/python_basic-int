def group_by_age():
    #Initialize an empty dictionary
    age_groups = {
        '0-9': [],
        '10-19': [],
        '20-29': [],
        '30-39': [],
        '40-49': [],
        '50-59': [],
        '60-69': [],
        '70-79': [],
        '80-89': [],
        '90-99': []
    }
    
    while True: #loop to keep adding until
        name = input("Enter name (or 'quit' to stop): ")
        if name.lower() == 'quit':
            break
            
        try:
            age = int(input(f"Enter age for {name}: "))
        except ValueError:
            print("Invalid age. Please enter a numeric value.")
            continue
        
        #if-else ages
        if 0 <= age <= 9:
            age_groups['0-9'].append(name) #.append to add
        elif 10 <= age <= 19:
            age_groups['10-19'].append(name)
        elif 20 <= age <= 29:
            age_groups['20-29'].append(name)
        elif 30 <= age <= 39:
            age_groups['30-39'].append(name)
        elif 40 <= age <= 49:
            age_groups['40-49'].append(name)
        elif 50 <= age <= 59:
            age_groups['50-59'].append(name)
        elif 60 <= age <= 69:
            age_groups['60-69'].append(name)
        elif 70 <= age <= 79:
            age_groups['70-79'].append(name)
        elif 80 <= age <= 89:
            age_groups['80-89'].append(name)
        elif 90 <= age <= 99:
            age_groups['90-99'].append(name)

    return age_groups

result = group_by_age()
print(result)
