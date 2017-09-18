# Парсер ОЛХ 
Парсит сайт https://www.olx.ua/ и вытянутые данные записывает в файл(olx.csv, нормально пока открывается только в LibreOffice), так же будет добалена возможность записи сразу в базу данных(postgresql  или sqlite3) это будет опционально

ссылка(URL) должна быть вида: 
```
"https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/kiev/q-samsung/?page=1"
```
где: 
группа/подгруппа/каталог 
```
/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/
```
локация
```
/kiev/
```
samsung - это бренд/марка и т.д. кароче что нужно искать
```
q-samsung
```
нужно для того что бы с этой страници начинался выбор пагинации, то есть брался последний 
```
?page=1
```
```
pages = soup.find("div", class_="pager rel clr").find_all("span", class_="item fleft")[-1]
```
## Использованые модули
1. requests
2. BeautifulSoup
3. csv
