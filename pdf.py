import requests

pdf_url = "https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf"
pdf_path = "D:/user/Downloads/Smyk-tyndyk.pdf"

response = requests.get(pdf_url)
with open(pdf_path, 'wb') as file:
    file.write(response.content)

print("PDF file downloaded successfully.")
