import datetime 


current_time = datetime.datetime.now()

print(current_time.strftime('%A %d %B %Y'))






people = {
    'John' : {'age': 13,' orientation': 'male'},
    'vika' : {'age': 13,' orientation': 'female'}
    
    
}

print(people.get('vika').get('age'))