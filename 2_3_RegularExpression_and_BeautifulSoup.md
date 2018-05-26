
# 2.3 정규 표현식, 람다
- 정규표현식이라는 이름은 **정규 문자열**을 식별하는데 쓰이는 데서 유래함.
- 즉, 문자열이 주어진 규칙에 일치하는지, 일치하지 않는지 판단할 수 있다.
- 예를 들어, 긴 문서에서 전화번호나 이메일 주소 같은 문자열을 빠르게 찾아보려 할 때 유용하다
- 정규문자열을 식별하는데 유용하다고 했었는데, 정규문자열이 뭔지 먼저 알아보자.  

# 2.3.1 정규 문자열
아래 규칙을 연달아 적용해서 생성할 수 있는 문자열이 정규문자열이다.
~~~
1. 글자 a를 최소한 한번 쓰시오.
2. 그 뒤에 b를 정확히 다섯개 쓰시오.
3. 그 뒤에 c를 짝수번 쓰시오.
4. 마지막에 d가 있어도 되고 없어도 됩니다.
~~~
 - 예를 들면 aaaabbbbbccccd, aabbbbbcc 이 위 정규문자열의 예가 될 것이다.
 
# 2.3.2 정규 표현식
정규 표현식은 위의 규칙을 짧게 줄여 쓴 것이다.
위의 정규문자열의 4개의 규칙을 정규 표현식으로 표현하면 다음과 같다.

~~~
aa*bbbbb(cc)*(d | )
~~~

이 정규표현식이 뭘 의미하는지 하나씩 뜯어보자

 - aa*  
 먼저 a를 쓰고 그 다음에 a*를 썼다. a*는 a가 몇 개든 상관없고 0개여도 된다는 뜻이다.
 aa*는 a가 최소한 한 번은 있다는 뜻이다.
 
 - bbbbb  
 특별한 건 없고 b를 5번 연이어 쓴다.
 
 - (cc)*  
 c 짝수 개에 관한 규칙을 충족하려면 c 두 개를 괄호 안에 쓰고 그 뒤에 아스테리크를 붙여서,
 c의 쌍이 임의의 숫자만큼 있음을 나타낸다.(0쌍이어도 규칙에는 맞다)

 - (d | )  
 'd 다음에 공백을 쓰거나, 아니면 d 없이 공백만 쓴다'는 뜻. d가 최대 하나만 있고 그 뒤에 공백이 이어지면서 문자열을 끝내게 된다.

## 2.3.3 정규표현식으로 이메일주소를 식별해보자

1. 이메일 주소의 첫번째 부분에는 (대문자, 소문자, 숫자0-9, 마침표(.), 플러스기호(+), 밑줄 기호(_))중 하나가 포함되어야 한다.

    ~~~
    [A-Za-z0-9\._+]+
    ~~~
    이렇게 가능한 경우를 모두 대괄호([])안에 넣으면 '대괄호에 들어있는 것들 중 아무거나 하나'라는 뜻이다.
    마지막의 + 기호는 바로 앞에 있는 것이 최소한 한번은 나타나야하고 최대 몇개인지는 제한하지 않는다는 뜻이다.  

2. 1번의 다음에 @가 와야 한다.

    ~~~
    @
    ~~~
    이메일 주소에는 반드시 @가 있어야 하며, 정확히 한개만 있어야 한다.  

3. 2번의 다음에는 대문자나 소문자가 최소한 하나 있어야 한다.

    ~~~
    [A-Za-z]+
    ~~~
    @다음에 오는 도메인 이름의 첫부분은 영문 대문자 또는 소문자여야 하고 최소한 글자 하나는 있어야 한다.  

4. 3번의 다음에는 마침표가 와야 한다.

    ~~~
    \.
    ~~~
    \는 특수문자(.)를 쓰기 위해 사용하는 이스케이프 문자이다.  
    
    
위의 규칙들을 합치면 이런 정규표현식이 만들어진다.
~~~
[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)
~~~

다른 정규표현식 기호들에 대해서는 인터넷검색을 해보자..(정리하기 귀찮다..)


# 2.3.4 정규표현식 활용(BeutifulSoup)

http://en.wikipedia.org/wiki/Kevin_Bacon 위키 페이지에서 항목링크만을 가져오는 코드를 작성해보자.
항목링크들의 규칙은 아래와 같다.
 - 이 링크들은 id가 bodyContent인 div안에 있다.
 - URL에는 세미콜론이 포함되어 있지 않다.
 - URL은 /wiki/로 시작한다.
 
첫번째 규칙은 BeautifulSoup패키지로 찾을 수 있고, 두번째와 세번째를 정규표현식으로 표현이 가능하다.  
^(/wiki/)((?!:).)*$

코드로 구현해보자


```python
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
```

    /wiki/Kevin_Bacon_(disambiguation)
    /wiki/San_Diego_Comic-Con
    /wiki/Philadelphia
    /wiki/Pennsylvania
    /wiki/Kyra_Sedgwick
    /wiki/Sosie_Bacon
    /wiki/Edmund_Bacon_(architect)
    /wiki/Michael_Bacon_(musician)
    /wiki/Footloose_(1984_film)
    /wiki/JFK_(film)
    /wiki/A_Few_Good_Men
    /wiki/Apollo_13_(film)
    /wiki/Mystic_River_(film)
    /wiki/Sleepers
    /wiki/The_Woodsman_(2004_film)
    /wiki/Fox_Broadcasting_Company
    /wiki/The_Following
    /wiki/HBO
    /wiki/Taking_Chance
    /wiki/Golden_Globe_Award
    /wiki/Screen_Actors_Guild_Award
    /wiki/Primetime_Emmy_Award
    /wiki/The_Guardian
    /wiki/Academy_Award
    /wiki/Hollywood_Walk_of_Fame
    /wiki/Social_networks
    /wiki/Six_Degrees_of_Kevin_Bacon
    /wiki/SixDegrees.org
    /wiki/Philadelphia
    /wiki/Edmund_Bacon_(architect)
    /wiki/Pennsylvania_Governor%27s_School_for_the_Arts
    /wiki/Bucknell_University
    /wiki/Glory_Van_Scott
    /wiki/Circle_in_the_Square
    /wiki/Nancy_Mills
    /wiki/Cosmopolitan_(magazine)
    /wiki/Fraternities_and_sororities
    /wiki/Animal_House
    /wiki/Search_for_Tomorrow
    /wiki/Guiding_Light
    /wiki/Friday_the_13th_(1980_film)
    /wiki/Phoenix_Theater
    /wiki/Flux
    /wiki/Second_Stage_Theatre
    /wiki/Obie_Award
    /wiki/Forty_Deuce
    /wiki/Slab_Boys
    /wiki/Sean_Penn
    /wiki/Val_Kilmer
    /wiki/Barry_Levinson
    /wiki/Diner_(film)
    /wiki/Steve_Guttenberg
    /wiki/Daniel_Stern_(actor)
    /wiki/Mickey_Rourke
    /wiki/Tim_Daly
    /wiki/Ellen_Barkin
    /wiki/Footloose_(1984_film)
    /wiki/James_Dean
    /wiki/Rebel_Without_a_Cause
    /wiki/Mickey_Rooney
    /wiki/Judy_Garland
    /wiki/People_(American_magazine)
    /wiki/Typecasting_(acting)
    /wiki/John_Hughes_(filmmaker)
    /wiki/She%27s_Having_a_Baby
    /wiki/The_Big_Picture_(1989_film)
    /wiki/Tremors_(film)
    /wiki/Joel_Schumacher
    /wiki/Flatliners
    /wiki/Elizabeth_Perkins
    /wiki/He_Said,_She_Said
    /wiki/The_New_York_Times
    /wiki/Oliver_Stone
    /wiki/JFK_(film)
    /wiki/A_Few_Good_Men_(film)
    /wiki/Michael_Greif
    /wiki/Golden_Globe_Award
    /wiki/The_River_Wild
    /wiki/Meryl_Streep
    /wiki/Murder_in_the_First_(film)
    /wiki/Blockbuster_(entertainment)
    /wiki/Apollo_13_(film)
    /wiki/Sleepers_(film)
    /wiki/Picture_Perfect_(1997_film)
    /wiki/Losing_Chase
    /wiki/Digging_to_China
    /wiki/Payola
    /wiki/Telling_Lies_in_America_(film)
    /wiki/Wild_Things_(film)
    /wiki/Stir_of_Echoes
    /wiki/David_Koepp
    /wiki/Taking_Chance
    /wiki/Paul_Verhoeven
    /wiki/Hollow_Man
    /wiki/Colin_Firth
    /wiki/Rachel_Blanchard
    /wiki/M%C3%A9nage_%C3%A0_trois
    /wiki/Where_the_Truth_Lies
    /wiki/Atom_Egoyan
    /wiki/MPAA
    /wiki/MPAA_film_rating_system
    /wiki/Sean_Penn
    /wiki/Tim_Robbins
    /wiki/Clint_Eastwood
    /wiki/Mystic_River_(film)
    /wiki/Pedophile
    /wiki/The_Woodsman_(2004_film)
    /wiki/HBO_Films
    /wiki/Taking_Chance
    /wiki/Michael_Strobl
    /wiki/Desert_Storm
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Matthew_Vaughn
    /wiki/Sebastian_Shaw_(comics)
    /wiki/Dustin_Lance_Black
    /wiki/8_(play)
    /wiki/Perry_v._Brown
    /wiki/Proposition_8
    /wiki/Charles_J._Cooper
    /wiki/Wilshire_Ebell_Theatre
    /wiki/American_Foundation_for_Equal_Rights
    /wiki/The_Following
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/Huffington_Post
    /wiki/Tremors_(film)
    /wiki/EE_(telecommunications_company)
    /wiki/United_Kingdom
    /wiki/Egg_as_food
    /wiki/Kyra_Sedgwick
    /wiki/PBS
    /wiki/Lanford_Wilson
    /wiki/Lemon_Sky
    /wiki/Pyrates
    /wiki/Murder_in_the_First_(film)
    /wiki/The_Woodsman_(2004_film)
    /wiki/Loverboy_(2005_film)
    /wiki/Sosie_Bacon
    /wiki/Upper_West_Side
    /wiki/Manhattan
    /wiki/Tracy_Pollan
    /wiki/The_Times
    /wiki/Will.i.am
    /wiki/It%27s_a_New_Day_(Will.i.am_song)
    /wiki/Barack_Obama
    /wiki/Ponzi_scheme
    /wiki/Bernard_Madoff
    /wiki/Finding_Your_Roots
    /wiki/Henry_Louis_Gates
    /wiki/Six_Degrees_of_Kevin_Bacon
    /wiki/Trivia
    /wiki/Big_screen
    /wiki/Six_degrees_of_separation
    /wiki/Internet_meme
    /wiki/SixDegrees.org
    /wiki/Bacon_number
    /wiki/Internet_Movie_Database
    /wiki/Paul_Erd%C5%91s
    /wiki/Erd%C5%91s_number
    /wiki/Paul_Erd%C5%91s
    /wiki/Bacon_number
    /wiki/Erd%C5%91s_number
    /wiki/Erd%C5%91s%E2%80%93Bacon_number
    /wiki/The_Bacon_Brothers
    /wiki/Michael_Bacon_(musician)
    /wiki/Music_album
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Supporting_Actor_%E2%80%93_Motion_Picture
    /wiki/The_River_Wild
    /wiki/Broadcast_Film_Critics_Association_Awards
    /wiki/Broadcast_Film_Critics_Association_Award_for_Best_Actor
    /wiki/Murder_in_the_First_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Apollo_13_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Supporting_Role
    /wiki/Murder_in_the_First_(film)
    /wiki/MTV_Movie_Awards
    /wiki/MTV_Movie_Award_for_Best_Villain
    /wiki/Hollow_Man
    /wiki/Boston_Society_of_Film_Critics_Awards
    /wiki/Boston_Society_of_Film_Critics_Award_for_Best_Cast
    /wiki/Mystic_River_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Mystic_River_(film)
    /wiki/Satellite_Awards
    /wiki/Satellite_Award_for_Best_Actor_%E2%80%93_Motion_Picture_Drama
    /wiki/The_Woodsman_(2004_film)
    /wiki/Teen_Choice_Awards
    /wiki/Teen_Choice_Awards
    /wiki/Beauty_Shop
    /wiki/Primetime_Emmy_Awards
    /wiki/Primetime_Emmy_Award_for_Outstanding_Lead_Actor_in_a_Miniseries_or_a_Movie
    /wiki/Taking_Chance
    /wiki/Satellite_Awards
    /wiki/Satellite_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Taking_Chance
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Frost/Nixon_(film)
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Taking_Chance
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Taking_Chance
    /wiki/Teen_Choice_Awards
    /wiki/Teen_Choice_Awards
    /wiki/Saturn_Awards
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/The_Following
    /wiki/People%27s_Choice_Awards
    /wiki/People%27s_Choice_Awards
    /wiki/The_Following
    /wiki/Saturn_Awards
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/The_Following
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Television_Series_Musical_or_Comedy
    /wiki/I_Love_Dick_(TV_series)
    /wiki/Kevin_Bacon_filmography
    /wiki/List_of_actors_with_Hollywood_Walk_of_Fame_motion_picture_stars
    /wiki/The_Austin_Chronicle
    /wiki/Access_Hollywood
    /wiki/Reuters
    /wiki/CBS_News
    /wiki/The_Verge
    /wiki/The_Hollywood_Reporter
    /wiki/Indie_Wire
    /wiki/IMDb
    /wiki/Internet_Broadway_Database
    /wiki/Lortel_Archives
    /wiki/AllMovie
    /wiki/Critics%27_Choice_Movie_Award_for_Best_Actor
    /wiki/Geoffrey_Rush
    /wiki/Jack_Nicholson
    /wiki/Ian_McKellen
    /wiki/Russell_Crowe
    /wiki/Russell_Crowe
    /wiki/Russell_Crowe
    /wiki/Daniel_Day-Lewis
    /wiki/Jack_Nicholson
    /wiki/Sean_Penn
    /wiki/Jamie_Foxx
    /wiki/Philip_Seymour_Hoffman
    /wiki/Forest_Whitaker
    /wiki/Daniel_Day-Lewis
    /wiki/Sean_Penn
    /wiki/Jeff_Bridges
    /wiki/Colin_Firth
    /wiki/George_Clooney
    /wiki/Daniel_Day-Lewis
    /wiki/Matthew_McConaughey
    /wiki/Michael_Keaton
    /wiki/Leonardo_DiCaprio
    /wiki/Casey_Affleck
    /wiki/Gary_Oldman
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Mickey_Rooney
    /wiki/Anthony_Andrews
    /wiki/Richard_Chamberlain
    /wiki/Ted_Danson
    /wiki/Dustin_Hoffman
    /wiki/James_Woods
    /wiki/Randy_Quaid
    /wiki/Michael_Caine
    /wiki/Stacy_Keach
    /wiki/Robert_Duvall
    /wiki/James_Garner
    /wiki/Beau_Bridges
    /wiki/Robert_Duvall
    /wiki/James_Garner
    /wiki/Ra%C3%BAl_Juli%C3%A1
    /wiki/Gary_Sinise
    /wiki/Alan_Rickman
    /wiki/Ving_Rhames
    /wiki/Stanley_Tucci
    /wiki/Jack_Lemmon
    /wiki/Brian_Dennehy
    /wiki/James_Franco
    /wiki/Albert_Finney
    /wiki/Al_Pacino
    /wiki/Geoffrey_Rush
    /wiki/Jonathan_Rhys_Meyers
    /wiki/Bill_Nighy
    /wiki/Jim_Broadbent
    /wiki/Paul_Giamatti
    /wiki/Al_Pacino
    /wiki/Idris_Elba
    /wiki/Kevin_Costner
    /wiki/Michael_Douglas
    /wiki/Billy_Bob_Thornton
    /wiki/Oscar_Isaac
    /wiki/Tom_Hiddleston
    /wiki/Ewan_McGregor
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/Kyle_Chandler
    /wiki/Steven_Weber_(actor)
    /wiki/Richard_Dean_Anderson
    /wiki/David_Boreanaz
    /wiki/Robert_Patrick
    /wiki/Ben_Browder
    /wiki/David_Boreanaz
    /wiki/David_Boreanaz
    /wiki/Ben_Browder
    /wiki/Matthew_Fox
    /wiki/Michael_C._Hall
    /wiki/Matthew_Fox
    /wiki/Edward_James_Olmos
    /wiki/Josh_Holloway
    /wiki/Stephen_Moyer
    /wiki/Bryan_Cranston
    /wiki/Bryan_Cranston
    /wiki/Mads_Mikkelsen
    /wiki/Hugh_Dancy
    /wiki/Andrew_Lincoln
    /wiki/Bruce_Campbell
    /wiki/Andrew_Lincoln
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Ra%C3%BAl_Juli%C3%A1
    /wiki/Gary_Sinise
    /wiki/Alan_Rickman
    /wiki/Gary_Sinise
    /wiki/Christopher_Reeve
    /wiki/Jack_Lemmon
    /wiki/Brian_Dennehy
    /wiki/Ben_Kingsley
    /wiki/William_H._Macy
    /wiki/Al_Pacino
    /wiki/Geoffrey_Rush
    /wiki/Paul_Newman
    /wiki/Jeremy_Irons
    /wiki/Kevin_Kline
    /wiki/Paul_Giamatti
    /wiki/Al_Pacino
    /wiki/Paul_Giamatti
    /wiki/Kevin_Costner
    /wiki/Michael_Douglas
    /wiki/Mark_Ruffalo
    /wiki/Idris_Elba
    /wiki/Bryan_Cranston
    /wiki/Alexander_Skarsg%C3%A5rd
    /wiki/Biblioteca_Nacional_de_Espa%C3%B1a
    /wiki/Biblioth%C3%A8que_nationale_de_France
    /wiki/Integrated_Authority_File
    /wiki/International_Standard_Name_Identifier
    /wiki/Library_of_Congress_Control_Number
    /wiki/MusicBrainz
    /wiki/SNAC
    /wiki/Syst%C3%A8me_universitaire_de_documentation
    /wiki/Virtual_International_Authority_File


# 2.3.5 태그의 속성에 접근
웹스크레이핑을 하다보면 특정 태그의 콘텐츠보다는 태그의 속성 값이 필요할 경우가 있다.  
찾으려고 하는 대상이 URL이 href속성에 들어있는 \<a\>태그, 타겟 이미지가 src속성에 들어있는 \<img\>태그일 경우, 속성 값이 필요할 것이다.
태그에 접근했던 방식과 유사하게 속성값에도 접근할 수 있다.

~~~python
myTag.attrs #get attributes from tag
myImgTag.attrs['src'] #get img source from attributes of tag
~~~
