
'''
파이썬의 유니코드 지원

- 파이썬3.0이후부터는 유니코드가 포함된 str타입들은 모두 유니코드로 저장됨
- 소스코드의 첫번째 줄 또는 두번째 줄에 특수 형식의 주석을 추가하여 다른 인코딩 형식을 지정할 수 있다.
- 파이썬3는 식별자에서 유니코드타입을 사용할 수 있다.
즉, 다음이 가능하다
한글 = '한글'
print(한글)

- 편집기에서 특정문자를 입력할 수 없거나 ASCII 코드만으로 소스코드를 유지하려는 경우,
문자열 리터럴에서 이스케이프 시퀀스를 사용할 수 있다.

- 유니코드 <-> 코드포인트 변환 내장함수를 제공한다.
# 유니코드를 코드포인트로 변환한다.(916)
in_s = ord('\u0394')
# 코드포인트를 유니코드문자열 반환한다.
out_s = chr(in_s)
print(in_s)
print(out_s)
---------------
916
Δ
---------------

 - Converting to Unicode string
bytes의 decode()메서드를 사용해서 유니코드 문자열로 만들 수 있다.
before_s = '가나다'
after_s = before_s.encode('utf-8')
print(after_s)
print(after_s.decode('utf-8'))
---------------
b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4'
가나다
---------------

- decoding 옵션들
encoding rule에 따르지 않아 변환되어질 수 없는 string의 경우, 두번째 인자는 그에 대한 반응으로 사용할 수 있다.(에러리턴 or replace)
'strict' argumnet는 UnicodeDecodeError를 리턴한다.
'replace' argumnet를 사용하면 U+FFD를 붙여서 반환해준다.
'backslahreplace'는 '\' 를 붙여서 반환해준다.
'ignore' argumnet를 사용하면 문제가 있는 문자열을 지우고 반환해준다.
-----------------------------------------------
>>> b'\x80abc'.decode("utf-8", "strict")
Traceback (most recent call last):
    ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0:
invalid start byte
>>> b'\x80abc'.decode("utf-8", "replace")
'\ufffdabc'
>>> b'\x80abc'.decode("utf-8", "backslashreplace")
'\\x80abc'
>>> b'\x80abc'.decode("utf-8", "ignore")
'abc'
-----------------------------------------------

- Converting to Bytes
bytes.decode()와 대응하는 str.encode()함수는 unicode 문자열을 bytes로 변환해준다.
위에서 살펴본 bytes메서드와 같이 'strict', 'replace', 'backslahreplace'
위의 bytes와 유사하지만, replace의 경우 변환할 수 없는 문자를 '?'로 바꾼다.
그 외에도 'xmlrefreplace', 'namereplace'가 있는데
xmlrefreplace는 XML character reference를 붙여주고(inserts an XML character reference)
namereplace의 경우는 \N{...}를 붙여준다는데 (inserts a \N{...} escape sequence)
정확히 뭐하는 놈인지는 모르겠다
-----------------------------------------------
>>> u = chr(40960) + 'abcd' + chr(1972)
>>> u.encode('utf-8')
b'\xea\x80\x80abcd\xde\xb4'
>>> u.encode('ascii')
Traceback (most recent call last):
    ...
UnicodeEncodeError: 'ascii' codec can't encode character '\ua000' in
position 0: ordinal not in range(128)
>>> u.encode('ascii', 'ignore')
b'abcd'
>>> u.encode('ascii', 'replace')
b'?abcd?'
>>> u.encode('ascii', 'xmlcharrefreplace')
b'&#40960;abcd&#1972;'
>>> u.encode('ascii', 'backslashreplace')
b'\\ua000abcd\\u07b4'
>>> u.encode('ascii', 'namereplace')
b'\\N{YI SYLLABLE IT}abcd\\u07b4'
-----------------------------------------------

그 외에도 다른 내용들이 더 있지만,,, 오늘은 여기까지만,,

다음의 파이썬 공식문서를 참고함
https://docs.python.org/3/howto/unicode.html
'''

'''
print('---------------')
한글 = '한글'
print(한글)
print('---------------')
# 유니코드를 코드포인트로 변환한다.(916)
in_s = ord('\u0394')
# 코드포인트를 유니코드문자열 반환한다.
out_s = chr(in_s)

print(in_s)
print(out_s)

print('---------------')
before_s = '가나다'
after_s = before_s.encode('utf-8')
print(after_s)
print(after_s.decode('utf-8'))
print('---------------')
'''