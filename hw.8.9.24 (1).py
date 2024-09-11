# START

# p_slice: int = int(input("how many pizza slice dani's mom brought?"))
#
# x = p_slice % 4
# y = p_slice // 4
#
# if x == 0 and y == 1:
#     print(f"everyone got {y} slice of pizza!")
# elif x == 0:
#     print(f"everyone got {y} slices of pizza!")
# elif x !=0 and y == 1:
#     print(f"everyone got {y} slice of pizza and {x} left!")
# else:
#     print(f"everyone got {y} slices of pizza and {x} left!")

friends = int(input("how many friend came o dani?"))
p_slice: int = int(input("how many pizza slice dani's mom brought?"))

if friends > 0:
     x = p_slice % friends
     y = p_slice // friends

     if x == 0:
        print(f"everyone got {y} slices of pizza!")
     else:
        print(f"everyone got {y} slices of pizza and {x} left!")
else:
    print("no one got a pizza!!!")


# END