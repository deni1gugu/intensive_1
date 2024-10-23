from bs4 import BeautifulSoup
import requests
url = "https://www.cian.ru"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml") 

data = soup.find("div", class_="_33974c2b58--info--dNDv8")


name = data.find("span", class_="_33974c2b58--color_black_100--Ephi7 _33974c2b58--lineHeight_7u--jtkAy _33974c2b58--fontWeight_bold--BbhnX _33974c2b58--fontSize_22px--sFuaL _33974c2b58--display_block--KYb25 _33974c2b58--text--e4SBY")
