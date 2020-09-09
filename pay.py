# f=open("./Tech_staff.xlsx", "w")
# f.write("Tech staff VOEV")
# f.close()

# f=open("./Tech_staff.xlsx", "r")
# content=f.read()
# f.close()
# print(content)

# with open("./test.txt", "w") as f:
#     content=f.write("Sizin qeyidleriniz test.txt fayilina daxil edildi")
#     print(content)


# with open("./Tech_staff.xlsx", "w") as f:
#     content=f.write("Sizin qeyidleriniz test.txt fayilina daxil edildi")
#     print(content)

# with open("./Tech_staff.xlsx", "r") as f:
#     content=f.read()
#     print(content)

with open("./Tech_staff.xlsx","Sheet1", "w") as f:
    content=f.write("Sizin qeyidleriniz test.txt fayilina daxil edildi")
    print(content)

# with open("./Tech_staff.xlsx","Sheet2", "r") as f:
#     content=f.read()
#     print(content)