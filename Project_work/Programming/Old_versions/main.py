from Project_work.Programming.Old_versions.log_in import *
from Project_work.Programming.Old_versions.admin_menu import *
from main_menu import *


# open log in window
# if admin open admin menu, if not open main menu
def main():
    l = cls_log_in()
    if l.log_in() == 1:
        a = Admin_menu()
    elif l.log_in() == 2:
        m = Main_menu()









main()
