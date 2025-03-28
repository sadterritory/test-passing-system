#!C:/Users/Ruslan/AppData/Local/Microsoft/WindowsApps/python.exe

import cgi
import os
from datetime import datetime

now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")
count = 0

form = cgi.FieldStorage()
if form.getvalue('q1') == "true":
    count += 1
if form.getvalue('q2') == "true":
    count += 1
if form.getvalue('q31') == "true":
    count += 1
if form.getvalue('q32') == "true":
    count += 1

handler = {}
if 'HTTP_COOKIE' in os.environ:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')
    for cookie in cookies:
        cookie = cookie.split('=')
        if len(cookie) == 2:
            handler[cookie[0]] = cookie[1]

results = []
for k in handler:
    results.append(handler[k])
results[0] = handler["date"]
results[1] = handler["res"]

print('Set-Cookie: date=' + str(dt))
print('Set-Cookie: res=' + str(count))
print("Content-type:text/html\r\n\r\n")
print("<!DOCTYPE html>")
print("<html lang=\"en\">")
print("<head>")
print("<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">")
print("<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>")
print("<link href=\"https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">")
print("<link href=\"/style.css\" rel=\"stylesheet\" type=\"text/css\">")
print("<title>Result CGI-script</title>")
print("</head>")
print("<style>")
print(".inner-wrapper {")
print("    max-width: 1380px;")
print("}")
print("</style>")
print("<body>")
print("<header class=\"inner-wrapper\">")
print("    <div class=\"inner-wrapper\">")
print("        <nav>")
print("            <div class=\"flex_container\">")
print("                <img src=\"/favicon.ico\" width=\"90\" height=\"90\" alt=\"kitty\" class=\"kittyImg\">")
print("                <h1 class=\"labHeader\">Лабораторная работа №3</h1>")
print("            </div>")
print("        </nav>")
print("    </div>")
print("</header>")
print("<main class=\"inner-wrapper\">")
print("    <article>")
print("        <section>")
print("            <div class=\"title_container\">")
print("                <div class=\"title_name\">Результаты:</div>")
print("                <div class=\"title_border\"></div>")
print("            </div>")

print("            <h2>Ваш результат {} из 3</h2>".format(count))
print("            <div>Дата и время прохождения теста: {}</div><br>".format(dt))
if results:
    print("        <h4> Предыдущий результат: ",
          results[1], "из 3, дата и время: ", results[0], "</h4>")
print("<div class=\"flex_button\">")
print("    <a href=\"/secondTest.html\" class=\"button-link\"><button class=\"butt\">Пройти тест еще раз</button></a>")
print("</div>")
print(          "</section>")
print(      "</article>")
print("</main>")
print("<footer class=\"inner-wrapper\">")
print("    <nav>")
print("        <span id=\"message\">Выполнил студент группы АВТ-143 Кувандыков Р.Н.</span>")
print("    </nav>")
print("</footer>")
print("</body>")
print("</html>")
