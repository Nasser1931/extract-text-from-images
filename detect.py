from PIL import Image
import pytesseract

print(pytesseract.get_languages(config=''))
img = Image.open("Machine learning\yo.jpg")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
print(result)
with open("text_result.txt", mode="w", encoding="utf-8") as file:
    file.write(result)
    print("ready!")
