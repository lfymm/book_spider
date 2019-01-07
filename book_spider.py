import re
from urllib import request
class Book():       
    
    # 书名
    book_name_pattern = '<h2>([\s\S]*?)</h2>'
    # 作者
    author_pattern = '<a href="/author/[\s\S]*?">([\s\S]*?)</a>'
    # 语言
    language_pattern = '<span class="label label-default">语言:([\s\S]*?)</span>'
    # 出版社
    press_pattern = '<span>出版社:([\s\S]*?)</span>'
    # 出版日期
    data_pattern = '<p>出版日期:([\s\S]*?)</p>'
    # 简介
    content_pattern = '<p class="description">([\s\S]*?)</p>'
    
    def __fetch_content(self,number):
        r = request.urlopen('http://d81fb43e-d.parkone.cn' + number)
        html = r.read()
        html = str(html,encoding='utf-8')   
        return html 
    
    def __analysis(self,html):
        anchors = []
        book_name = re.findall(Book.book_name_pattern,html)
        author = re.findall(Book.author_pattern,html)
        language = re.findall(Book.language_pattern,html)
        press = re.findall(Book.press_pattern,html)
        data = re.findall(Book.data_pattern,html)
        content = re.findall(Book.content_pattern,html)
        anchor = {'书名 ':book_name,'作者 ':author,'语言 ':language,'出版社 ':press,'出版日期 ':data,'简介 ':content}
        anchors.append(anchor)
        return anchors

    def go(self,book_number):
        html = self.__fetch_content(book_number)  
        anchors = self.__analysis(html)
        print(anchors) 

class Test:
    book = Book()
    i = 1
    while True:
        page_url = 'http://d81fb43e-d.parkone.cn/page/{}'.format(i)
        resp = request.urlopen(page_url)           # 打开page_url页面
        htmls = resp.read()
        htmls = str(htmls,encoding='utf-8')
        book_url = '<div class="cover">[\s\S]*?<a href="(/book/[\s\S]*?)"[\s\S]*?>[\s\S]*?</a>[\s\S]*?</div>'
        book_number = re.findall(book_url,htmls)
        if book_number == []:  
            print('shu')                 # 没有书                     
            break
        else: 
            for number in  book_number:                       # 有书
                book.go(number)                 # 爬书
            i += 1
    
    