order_status = "Complete order"
print(order_status.replace("Complete","Completed on"))

order_df = "1,2,3,4,5,6"
order_newdf = order_df.split(",")
order_newdf.append(9)
order_newdf.insert(1,7)
print(order_newdf)
order_newdf.pop()
print(order_newdf)
for x in order_newdf:
    print(type(x))


numbers = range(1,11)
sum = 0
for x in numbers:
    sum = sum + x
    print(x)
print(sum)
