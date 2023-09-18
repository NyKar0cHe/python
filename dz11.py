import cv2
from PIL import Image

image_cat = "cat.jpeg"
image = cv2.imread(image_cat)

cat_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")

cat_face = cat_cascade.detectMultiScale(image)
print(cat_face)

cat = Image.open(image_cat)
glasses = Image.open('glasses.png')
crown = Image.open('crown.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
crown = crown.convert("RGBA")

for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h / 3)))
    crown = crown.resize((int(w * 1.5), int(h / 1.2)))
    cat.paste(glasses, (x, int(y + h / 4)), glasses)
    cat.paste(crown, (int(x - 20), int(y - 45)), crown)

cat.save("kit911.png")
kit911 = cv2.imread("kit911.png")
cv2.imshow("Cat", kit911)
cv2.waitKey()
