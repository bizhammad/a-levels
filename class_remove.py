def remove_member(membership_number_to_remove, input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            members_list = file.readlines()

        new_members_list = []
        for member in members_list:
            compare=member[1:4]
            if compare != membership_number_to_remove:
                 new_members_list.append(f"{members_list}")

        with open(output_file, 'w') as file:
            file.writelines(new_members_list)

        print("Member removed successfully.")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "EmailDetails.txt"
output_file = "updated_members.txt"

membership_number_to_remove = "1234"

remove_member(membership_number_to_remove, input_file, output_file)



