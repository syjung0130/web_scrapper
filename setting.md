# Ubuntu 14.04
jupyter notebook에서 virtualenv ipython 커널이 필요한 경우가 있다.
검색해보니 ipykernel, jupyter관련 설정을 해주면 된다고 한다.
자세한 내용은 아래 링크를 참조  
https://www.youtube.com/watch?v=J08Nqad_-sI
http://help.pythonanywhere.com/pages/IPythonNotebookVirtualenvs
https://taufiqhabib.wordpress.com/2016/12/18/intalling-jupyter-in-a-virtualenv/

요약하면 아래와 같다.
## 1. pip upgrade 및 ipython 설치
~~~
$ source bin/activate
(crawling_web)$ pip install –upgrade pip
(crawling_web)$ pip install ipython
~~~


## 2. ipykernel설치
~~~
pip install jupyter //python 2.7을 사용하고 있는데 위 링크 명령을 따라하면 ..에러난다.. 버전이 안맞아서 아래 처럼 버전을 명시해주어야한다.
(crawling_web)$pip install tornado==4.5.3
(crawling_web)$pip install ipykernel==4.8.2
~~~


## 3. jupyter notebook에서 사용할 kernel추가
~~~
(crawling_web)$ python -m ipykernel install --user --name=crawling_web
Installed kernelspec crawling_web in /home/sy/.local/share/jupyter/kernels/crawling_web
~~~
(kernel.json 파일 확인)
~~~
(crawling_web)$ls /home/sy/.local/share/jupyter/kernels/crawling_web
(crawling_web)$sudo vim /home/sy/.local/share/jupyter/kernels/crawling_web/kernel.json
~~~
~~~
{
  "display_name": "crawling_web",
  "language": "python",
  "argv": [
   "/home/sy/2_Study/crawling_web/bin/python",
   "-m",
   "ipykernel_launcher",
   "-f",
   "{connection_file}"
  ]
}
~~~

## 4. 필요한 패키지 설치
BeautifoulSoup 패키지 설치
~~~
(crawling_web)$pip install bs4
~~~

python2.7에서는 urllib사용법이 python3과 다르다. 아래 코드처럼 urllib2를 import해서 사용해야한다.
~~~python
from urllib2 import urlopen
~~~

# Mac (알아서..)
