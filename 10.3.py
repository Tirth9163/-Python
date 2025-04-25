def create_vcard():
    name = input("Enter Full Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
END:VCARD
"""

    filename = name.replace(" ", "_") + ".vcf"
    with open(filename, "w") as f:
        f.write(vcard)

    print(f"vCard saved as '{filename}' and ready to import on your phone.")

create_vcard()
