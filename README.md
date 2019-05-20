# zamanchu
시종설 심심한사람들 - 자만추

## 다운로드 및 실행
1. 폴더를 만드시고 폴더 안에 download zip 또는 git clone <이 repo의 주소>를 입력해서 다운받기
2. 만든 폴더 경로에서 VSCode에서 가상환경을 만들고($ python -m venv myvenv)
3. 가상환경을 실행합($ source myvenv/Scripts/activate)
4. 가상환경에 장고를 설치하고($ pip install django==2.1.7)
5. 가상환경에 부트스트랩 설치($ pip install django-bootstrap4)
6. 가상환경에 디버깅 패키지 설치($ pip install django-debug-toolbar)
7. 프로젝트 폴더로 이동($ cd jamanchu-master)
8. 서버 실행($ python manage.py runserver)

## 최예은 진행 상황
1. 3/28 django project 업로드
2. 3/29 home, meeting 앱 제작
3. 3/30 meeting 앱 내에 meeting 모델 제작
4. 3/30 meeting 앱 crud중 r 구현(detail.html)
5. 4/7 meeting 앱 c 구현(new.html) ModelForm이나 Form 사용하고 싶었으나 오류남.
6. 4/8 static 폴더 만들고 collectstatic 실행
7. 4/9 부트스트랩 CDN 등록
8. 4/10 accounts 앱 생성, 로그인/로그아웃/회원가입 구현
9. 4/30 profiles 앱 생성, user와 one-to-one 연결 시도중
10. 5/2 meeting 앱 c,r 백엔드 완성
11. 5/2 profiles 앱 c,r 백엔드 완성
12. 5/3 User-Meeting 모델 1:N 연결
13. 5/6 Message 앱 생성, 쪽지 기능 구현, 리스팅 연구중
14. 5/9 수업 시간에 html, css 합침
15. 5/14 search app 완료, message app 완료
16. 5/14 scrap app 만듦, scraplist template 만듦
17. 5/16 message app 리스팅 오류 수정
18. 5/17 message app show.html 서브리스팅 수정, AddMessageForm 적용
19. 5/21 scrap 구현
20. 5/21 scrap scrap.models의 meeting 필드에서 unique=True로 인한 오류 수정