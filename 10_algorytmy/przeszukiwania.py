# def search_mail():
#    search_mail_list = "abc@wp.pl"
#     search_mail_user = input("Jakiego maila szukasz? ")
#     if search_mail_user == search_mail_list:
#         print("mail znaleziony")
#         return True
#     else:
#         print("nie udało się")
#         return False
#
#
# search_mail()

def is_email_in_list(email, email_list):
    for e in email_list:
        if email == e:
            print("Znaleziono")
            return True
    print("Nie znaleziono maila)"
    return False