

current_usr = ['raju','mia','asif','jakir','known',"hossen"]
new_user = ['new1','new2','raju','mia','jakir']

for new_user in new_user:
    if new_user in current_usr:
        print(f"{new_user}--The person will need inter a new username")
    else:
        print(f"{new_user}--That username is not available")