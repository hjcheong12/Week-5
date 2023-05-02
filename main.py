main.py

import datetime
import re


def create_membership():
		# 아래 코드는 python에 내장되어 있는 datetime 모듈을 활용하여 오늘 날짜를 입력하는 코드입니다. 
		# stnr_date 코드는 제가 작성했으니, 건드리지 않으셔도 되옵니다 :)
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []
    user = {}
		# user 딕셔너리에 username, password, email을 아래 주어진 제한 조건에 알맞게 입력받는 코드를 작성하세요.
	  # user 딕셔너리 값에는 username, password, email, stnr_date 총 4가지 값이 저장되어야 합니다.
    users.append(user)

    return users

#한국어로 하면 이상하게 깨져서 일단 영어로 했습니당

def get_user_input():
    user = {}

    id_valid = False
    while not id_valid:
        input_id = input("Enter your ID of 2-4 characters of Korean only: ")
        if re.match('^[가-힣]{2,4}$', input_id):
            user['id'] = input_id
            id_valid = True
        else:
            print("Invalid. Please enter 2-4 characters of Korean only.")

    pw_valid = False
    while not pw_valid:
        input_pw = input("Enter your password. Must be 8+ characters with a capital letter and at least one special character !,@,#,$: ")
        if len(input_pw) >= 8 and any(c.isupper() for c in input_pw) and any(c in input_pw for c in "!@#$"):
            user['password'] = input_pw
            pw_valid = True
        else:
            print("Invalid. Please enter a password that is 8+ characters with a capital letter and at least one special character !,@,#,$.")

    email_valid = False
    while not email_valid:
        input_email = input("Enter your email (must end with .com and contain only letters, numbers, and @): ")
        if input_email.endswith(".com") and all(c.isalnum() or c == "@" for c in input_email):
            user['email'] = input_email
            email_valid = True
        else:
            print("Invalid email. Please enter an email that ends with .com and contains only letters, numbers, and @.")

    user['stnr_date'] = stnr_date
    return user

#아래는 그대로
def get_user_list():
    users = []
    while True:
        user = get_user_input()
        users.append(user)
        answer = input("Do you want to add another user? (Y/N) ")
        if answer.lower() != 'y':
            break
    return users


def get_user_list():
    users = []
    while True:
        user = create_membership()[0]
        users.append(user)
        answer = input("Do you want to add another user? (Y/N) ")
        if answer.lower() != 'y':
            break
    return users


def load_to_txt(user_list):
    with open('memberdb.txt', 'w', encoding='UTF-8') as f:
        for user in user_list:
            f.write(f"ID: {user['id']}\n")
            f.write(f"Password: {user['password']}\n")
            f.write(f"Email: {user['email']}\n")
            f.write(f"Start Date: {user['stnr_date']}\n\n")


def run():
    user_list = get_user_list()
    load_to_txt(user_list)
    
run()