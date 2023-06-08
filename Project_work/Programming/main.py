from database import *
from log_in import *
from myvalidation import *
from Themesfile import *
from admin_menu import *
from main_menu import *

# open log in window 
# if admin open admin menu, if not open main menu
def main():
    log_in = log_in_ui()
    user = log_in.username_entry.get()
    if log_in.database.is_admin(user) == True:
        admin_men = Admin_menu()
    else:
        main_men = Main_menu()

main()




















