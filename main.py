# Impoting qrcode
import qrcode

# Importing time
import time

# Making a function to make qrcode


def generateCode(query):
    # Creating a qrcode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Adding user input to qrcode
    qr.add_data(query)

    # Making qrcode fit to screen
    qr.make(fit=True)

    # Generating qrcode
    img = qr.make_image(fill_color="red", back_color="black")

    img.save("QrCode.png")


# Taking text or url input from user
query = input("Enter text/Url\n")

# Checking if the user input is empty or not
if(query == ""):
    print("Plase Enter some text or Url!!\n")
else:
    print("Generating Qr Code!!")
    time.sleep(2)
    generateCode(query)
    print("QrCode Generated Successfully and saved as QrCode.png")
    time.sleep(2)
    exit()
