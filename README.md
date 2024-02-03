# Hello Pick!

## 실제 L사의 사용자의 데이터를 활용한 VOD 추천 웹서비스 

![image](https://github.com/mino1998/VOD-Chucheon-Backend-.new/assets/55076739/42973193-89cd-41a9-8885-1401b6b727b3)
![image](https://github.com/mino1998/VOD-Chucheon-Backend-.new/assets/55076739/b46633c4-6928-41a8-93f3-bf2d4d27bd9a)

## 👨‍💻 내가 참여한 부분 
1. React를 이용한 프론트엔드 초기 구성 작업 및 API 호출 관련 작업
2. Django를 이용한 백엔드 구성
3. 데이터 분석 및 모델링

## 👨‍💻 백엔드 작업
1. Django의 기본 DB가 아닌, AWS RDS에서 MySQL을 이용하여 사용자 정보 저장
2. 로그인 앱에서 사용자 인증 요청시 DB와 비교 후 SimpleJWT를 이용한 Refresh, Access Token 제공
3. 이후 메인 페이지로 넘어갈 때, 화면 구성을 위해 데이터 요청이 들어올 때 마다 각 요청에 맞는 함수를 이용할 수 있도록 재사용 하기 편한 Class형 뷰로 제작

## 👨‍💻 프론트 작업
1. 초기 로그인 화면 및 메인페이지 넘어갈 수 있도록 토큰과 사용자 ID를 쿠키와 세션에 각각 저장
2. 이후 인증된 사용자가 인가된 서비스를 사용하는지 PrivateRoute를 이용하여 계속 확인하도록 설정
3. 화면 구성을 위해 필요한 정보를 Body에 담아 Server로 Request하는 작업 실시

![image](https://github.com/mino1998/VOD-Chucheon-Backend-.new/assets/55076739/d130dd70-8133-4163-879e-ac542076263a)
![image](https://github.com/mino1998/VOD-Chucheon-Backend-.new/assets/55076739/5fe51497-813e-47a0-af47-d0fc47f2f571)
![image](https://github.com/mino1998/VOD-Chucheon-Backend-.new/assets/55076739/a7e270bb-a473-42f7-bcb7-b6ecf310a159)
![image](https://github.com/mino1998/VOD-Chucheon-Backend-.new/assets/55076739/84518c21-aafa-4218-8542-26c75d24f0e8)
![image](https://github.com/mino1998/VOD-Chucheon-Backend-.new/assets/55076739/5edf0ae8-4229-463f-a99c-03bafb2f0522)

## 👨‍💻 데이터 작업
### 데이터 확인
1. 실제 데이터를 확인하였을 때, 단순히 해당 VOD 상세 페이지로 클릭하는 로그 혹은, 시청 로그만이 존재하였다. 즉, 사용자의 평점은 없던 데이터다.
2. 협업 필터링을 이용하여 추천 모델을 만들려고 하였다. 이를 위해 "평점"으로 사용할 수 있는 데이터를 찾아야 했다.
3. 
