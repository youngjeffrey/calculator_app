import easyocr

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext('matrix-example.jpg', detail = 0)

for i in range(len(result)):
    print(result[i])
