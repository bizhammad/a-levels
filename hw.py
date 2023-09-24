#since we don't habe data about customers i'll make an array to make this program work
customer_id=[]

def new_customer(no_of_customers):
    maxval=no_of_customers
    tempval=800
    while no_of_customers != len(customer_id):
        tempval= (tempval % maxval) * 4
        if tempval in customer_id:
            tempval= tempval+7
        else:
            customer_id.append(tempval)
    print("Customer ID list", customer_id)

new_customer(int(input("Enter the nmnumbers of customer ID's you want: ")))
            

        
