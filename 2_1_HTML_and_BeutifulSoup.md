
# 2. HTML 분석

## 2.1. 닭잡는데 소잡는 칼을 쓸 필요는 없습니다.
원하는 콘텐츠가 있고 이 콘텐츠가 있는 웹사이트의 HTML에서 필요한 정보를 가져와야 한다고 가정해보자.
이 콘텐츠는 이름일 수도, 통계 자료일 수도, 텍스트 블록일 수도 있다. 그리고 이 콘텐츠는 20depth나 되고, 단서가 될만한 태그나 속성이 없을 수 있다.
당장 달려들어서 아래 코드를 짰다고 해보자.

~~~python
bsObj.findAll("table")[4].findAll("tr")[2]/find("td").findAll("div")[1].find("a")
~~~

이 경우, 사이트 관리자가 사이트를 조금만 수정하더라도 웹스크레이퍼의 동작이 멈출 수 있을 뿐더러, 그리 보기 좋은 코드도 아니다.

 - HTML코드가 복잡한 구조로 되어있을 경우, 더 나은 HTML구조를 갖춘 모바일 버전 사이트를 찾아보는 것도 방법이 될 수 있다.
 - 자바스크립트 파일에 숨겨진 정보를 찾아보자. 자바스크립트 파일을 불러와서 분석한다.
 - 중요한 정버가 페이지 타이틀에 있는 경우가 많지만, URL에 들어있을 때에도 있다.
 - 원하는 정보가 이 웹사이트에 없을 경우 대안이 될만한 다른 웹사이트를 찾아보자.
 
 데이터가 깊숙히 파묻혀 있거나 정형화되어있지 않을 수록 곧바로 코드부터 짜서는 안된다.
 

## 2.2. 다시 BeutifulSoup
이 섹션에서는 속성을 통해 태그를 검색하는 방법, 태그 목록을 다루는 방법, 트리 내비게이션을 분석하는 방법을 알아보자.

### CSS와 BeutifulSoup의 활용
거의 모든 웹사이트에는 스타일시트가 존재한다. CSS는 HTML요소를 구분해서 서로 다른 스타일을 적용한다.
CSS의 등장은 웹스크레이퍼에도 큰 도움이 되었다고 한다.

***웹스크레이퍼는 클래스를 이용해서 이 태그들을 쉽게 구별할 수 있다.***
예를 들면, 빨간색 텍스트만 전부 수집하고 녹색 텍스트는 수집하지 않을 수 있다. CSS는 이런 속성을 통해 사이트에 스타일을 적용하고, 요즘의 웹사이트 대부분은 이런 클래스(class)와 ID(id)속성이 가득하다.

http://www.pythonscrapping.com/pages/warandpeace.html 페이지를 스크랩하는 예제 웹스크레이퍼를 만들어보자
이 페이지에서 등장인물이 말하는 대사는 빨간색으로 이름은 녹색으로 표시되어있다.
~~~HTML
"<span class="red">Heavens! what a virulent attack!</span>" 
replied <span class="green">the prince</span>, not in the least disconcerted by this reception.
~~~

위의 HTML을 스크래핑하기 위해서 BeutifulSoup로 다음과 같은 프로그램을 구현할 수 있다.
~~~python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscrapping.com/pages/warandpeace.html")
bsObj = BeutifulSoup(html, "html.parser")
~~~

이 BeutifulSoup객체에 findAll함수를 쓰면 
~~~HTML
<span class="green"></span>
~~~
에 들어있는 텍스트만 선택해서 리스트로 추출할 수 있다.
아래 코드는 findAll을 이용해서 등장인물들의 이름들이 등장할 때마다 리스트에 넣어서 이름으로 추출하는 코드이다.
(bsObj.tagName을 사용하면 페이지에서 처음 나타낸 태그를 찾을 수 있다)
(get_text() 태그를 제외하고 콘텐츠만 출력한다)
~~~python
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
~~~

## 2.2.1 find()와 findAll()
find(), findAll()은 BeutifulSoup에서 가장 자주 쓰는 함수이고, HTML 페이지에서 원하는 태그를 속성별로 필터링할 수 있다.

~~~python
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
~~~

실제 이 함수를 쓸 때는 tag, attributes만 쓰는 경우가 많다고 한다. 또, 태그 이름으로 이루어진 리스트를 넘길 수도 있다.
~~~python
.findAll({"h1","h2","h3","h4","h5","h6"})
~~~

***attributes 매개변수***는 속성으로 이루어진 파이썬 딕셔너리를 받고, 그 중에 하나에 일치하는 태그를 찾는다.
예를 들어 다음 함수는 HTML문서에서 녹색과 빨간색 span태그를 모두 반환한다.
~~~python
.findAll("span",{"class":{"green","red"}})
~~~

***recursive 매개변수***는 모두 불리언이고, true이면 매개변수에 일치하는 태그를 재귀적으로 자식을 순회하며 찾게된다.
false이면 최상위 태그만을 찾는다. 기본적으로 findAll은 재귀적으로(recursive = true)로 동작한다. 성능이 중요하지 않다면 그대로 두는 것이 좋다.
예제 페이지에서 'the prin
ce'가 몇번 나타났는지 보자
~~~python
nameList = bsObj.findAll(text="the prince")
print(len(nameList))
~~~

***limit 매개변수***는 물론 findAll에만 쓰인다. find는 findAll을 호출하면서 limit을 1로 호출한 것과 같다.
즉, 페이지의 항목 **처음 몇 개**에만 관심을 있을 때 사용하는 매개변수임.
이 매개변수는 페이지에 나타난 순서대로 찾으며, 그 순서가 원하는 것과 일치하지 않을 수 있다는 점을 주의해야한다.

***keyword 매개변수***는 특정 속성이 포함된 태그를 선택할 때 사용한다.
~~~python
allText = bsObj.findAll(id="text")
print(allText[0].getText())
~~~

 - 태그 목록을 .findAll()에 속성 목록으로 넘기면 or필터처럼 동작한다.(태그1, 태그2, 태그3 등이 들어간 모든 태그 목록을 선택한다)
 - keyword 매개변수는 and 필터처럼 동작한다.


