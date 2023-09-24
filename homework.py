#HOMEWORK - FILLING

with open('EmailDetails.txt', 'r') as details:
    member_details = details.readlines()

membership_detail_list = []

for member in member_details:
    membership_num = "00" + member 
    membership_detail_list.append(membership_num)

with open("NewEmailDetails.txt", 'w') as file:
    file.writelines(membership_detail_list)

