# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


input_username = input('Please enter your username: ')
save_into_db(input_username)
input_dob = int(input('Please enter your birth year: '))
age = 2023 - input_dob
print("You are ",age, " years old.")
