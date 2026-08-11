var1 = "Make a lot of money"
var2 = "buy now"
var3= "subscribe this"
var4= "click this"

message = input("Enter your message: ")
if var1 in message or var2 in message or var3 in message or var4 in message:
    print("This is a spam message")
else:
    print("This is not a spam message")