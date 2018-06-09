
# Using Web API
API(Application Programming Interface)는 다양한 어플리케이션 사이의 인터페이스를 의미하지만, 여기서는 Web에서 쓰이는 API를 살펴보자.
 - API를 통해 요청을 보낼 때는 HTTP를 통해 데이터를 요청하며 API는 이 데이터를 XML이나 JSON형식으로 반환한다.
 - 대부분의 API가 아직 XML을 지원하지만, 최근에는 JSON을 인코딩 프로토콜로 사용하는 API도 늘어나고 있다.

~~~
웹브라우저의 주소창에서 아래 주소로 이동하면 ip주소에 대한 지역에 대한 정보가 json형식으로 반환되는 것을 확인할 수 있다.
http://freegeoip.net/json/50.78.253.58

{"__deprecation_message__":"This API endpoint is deprecated and will stop working on July 1st, 2018. For more information please visit: https://github.com/apilayer/freegeoip#readme","ip":"50.78.253.58","country_code":"US","country_name":"United States","region_code":"MA","region_name":"Massachusetts","city":"Boston","zip_code":"02116","time_zone":"America/New_York","latitude":42.3496,"longitude":-71.0746,"metro_code":506}
~~~

웹스크레이퍼에서 얻은 정보와 API를 이용해 얻은 정보를 이용해서 더 유용한 정보로 가공할 수 있다는 점에서 Web API도 살펴볼 필요가 있다.
최종적으로는 위키백과 편집내역과 IP주소 해석기 API를 결합해서 전세계에서 어떻게 편집되고 있는지를 알아볼 수 있는 예제를 만들어보자


## 1. HTTP
HTTP API는 표준화된 규칙으로 정보를 제공하고 정보를 생성하는 방법도 표준화되어있다.
우선 HTTP API가 어떤 것인지 살펴보자
https://restfulapi.net/http-methods/

## 1.1 HTTP 메서드
HTTP를 통해 웹 서버에 정보를 요청하는 방법은 네가지다
 - GET: 웹서버에 정보를 요청할 때 쓰는 방법(브라우저에서 주소표시줄을 통해 페이지 방문할 때도 GET을 사용한다)
 - POST: 폼을 작성하거나, 서버에 있는 스크립트에 정보를 보낼때 사용한다.(로그인할 때마다 사용자 이름과 비밀번호를 보낼때 등 사용)
 - PUT: 정보를 데이터베이스에 저장 요청(POST와 같다. POST를 더 많이 쓴다고 한다.
 - DELETE: 어떤 객체를 삭제할 때 사용됨.
 
## 1.2 인증
API를 요청할 때 개발자가 부여받은 인증키를 포함해서 요청해서 사용한다.
일종의 토큰 같은 것인데, API를 호출할 때마다 인증키를 통해 토큰이 웹서버에 전송이 된다. 
사용자가 등록할 때 영구적으로 저장되는 인증키값도 있고 자주 바뀌어서 매번 서버에서 받아와야하는 경우도 있다.

## 1.3 JSON 파싱
최근의 Web API들은 요청에 대한 응답으로 JSON, XML로 반환한다.
응답으로 받은 JSON을 파싱하기 위해서는 라이브러리를 사용하면 된다.
파이썬은 json객체는 딕셔너리로, json배열은 리스트로, json문자열은 문자열로 변환하기 때문에 json에 저장된 값에 접근하고 조작하기 편리하다.


```python
# Get Country using ip address
import json
from urllib2 import urlopen
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
def getCountry(ipAddress):
    response = urlopen("https://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")
print(getCountry("50.78.253.58"))
```

## 2. Web API + Crawlling 응용
wiki페이지를 편집한 나라들을 조회하는 코드를 짜보자..
