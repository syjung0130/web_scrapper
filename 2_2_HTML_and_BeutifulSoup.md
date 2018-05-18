
## 2.2.2 기타 BeutifulSoup 객체

**BeutifulSoup 객체**  
이전 코드 예제에서 bsObj와 같은 형태로 사용함

**Tag 객체**  
리스트 호출 또는 BeautifulSoup 객체에 find와 findAll을 호출, 또는 직접 접근해서 사용함
~~~python
bsObj.div.h1
~~~
**NavigableString 객체**  
태그 자체가 아닌 태그 안에 들어있는 텍스트를 나타냄. 일부 함수는 Navigable Strings를 반환함

**Comment 객체**  
주석 태그 안에 들어있는 아래와 같은 HTML 주석을 찾는데 사용함
~~~HTML
<!-- like this one -->
~~~


## 2.2.3 트리 이동

findAll()함수는 이름과 속성에 따라 태그를 찾는다. 그런데 문서 안에서의 위치를 기준으로 태그를 찾고자할 경우가 있다.
아래와 같은 페이지를 예로 확인해보자
~~~
html
-- body
  -- div.wrapper
     -- h1
     -- div.content
     -- table#giftList
        -- tr
        -- th
        -- th
        -- th
        -- th
     -- tr.gift#gift1
        -- td
        -- td
           -- span.excitingNote
        -- td
           -- img
     -- ... 더 많은 테이블 행 ...
  -- div.footer
~~~

## 자식과 자손
BeutifulSoup라이브러리도 자식과 자손을 구별한다.
자식은 항상 부모보다 한 태그 아래에 있고, 자손은 조상보다 몇 단계든 아래에 있을 수 있다.
위의 예를 보면, tr태그는 table태그의 자식이며 tr과 th, td, img, span은 모두 table 태그의 자손이다.
모든 자식은 자손이지만, 모든 자손이 자식은 아니다.
예를 들어보면
 - bsObj.body.h1은 body의 자손인 첫번째 h1태그를 선택하고 body 바깥에 있는 태그에 대해서는 동작하지 않는다.
 - bsObj.div.findAll("img")는 문서의 첫번째 div태그를 찾고, 그 div태그의 자손인 모든 img태그의 목록을 가져온다.
 - 자식만 찾을 때는 .children을 사용한다.



```python
#이 코드는 giftList테이블에 들어있는 제품 행 목록을 출력한다.
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscrapping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)
```

## 형제
BeautifulSoup의 next_siblings()함수는 테이블에서 데이터를 쉽게 수집할 수 있고, 테이블에 타이틀 행이 있을 때 유용하다.
코드를 예로 확인해보자
 - 이 코드에서 출력하는 내용은 첫번째 타이틀 행을 제외한 모든 제품의 행이다. 자기 자신을 제외한 형제 객체들을 가져온다.
 - 이 함수를 보완하는 previous_siblings함수도 있다. 이 함수를 사용하면 원하는 형제 태그 목록의 마지막에 있는 태그를 쉽게 선택할 수 있다.
 - previous_sibling, next_sibling함수도 있는데 이 함수들은 태그 하나만 반환한다.


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscrapping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
```

## 부모 다루기
 - 웹 페이지를 스크랩하다보면 부모를 알아야 할 때가 있다.
 - 부모 검색 함수로 .parent , .parents 함수가 있다.
 - 이 코드는 img1.jpg가 나타내는 객체의 가격을 출력한다.
 ( img1.jpg에 해당하는 이미지를 선택 -> 부모 태그 선택(< td >태그) -> previous_sibling을 선택함 -> 태그에 들어있는 $15.00을 선택함)


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscrapping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
```
