# 💊 Medical_Advice_Bot

## 주요 기능
- **신규 유저 입장 시 비공개 채널 자동 생성**: 서버에 입장한 신규 유저를 위해 본인만 볼 수 있는 비공개 상담 채널을 자동으로 생성합니다.
- **!아파 명령어로 CLOVA 기반 상담 응답**: 사용자가 `!아파 증상 ex) !아파 속이 메스꺼워`을 입력하면 CLOVA API를 통해 의학적 상담을 제공합니다.
- **따뜻하고 공감 어린 의사 말투**: 감정에 기반한 친절하고 위로하는 응답을 제공합니다.
- **관리자 접근 차단**: 생성된 채널은 완전한 개인 상담 공간으로, 관리자도 접근할 수 없습니다.

## 🛠 설치 및 실행 방법

### 1. Python 패키지 설치
필요한 Python 패키지를 설치하려면 터미널에서 다음 명령어를 실행하세요:  
pip install discord aiohttp python-dotenv  
- `discord`: 디스코드 봇 구현을 위한 패키지.  
- `aiohttp`: CLOVA API 비동기 요청 처리.  
- `python-dotenv`: 환경 변수 관리.

### 2. `.env` 파일 생성 (최상단 디렉토리에 위치)
프로젝트 최상단 디렉토리에 `.env` 파일을 만들고 다음 내용을 입력하세요:  
DISCORD_TOKEN=디스코드_봇_토큰  
CLOVA_SECRET=CLOVA_API_키  
- `DISCORD_TOKEN`: 디스코드 개발자 포털에서 발급받은 봇 토큰.  
- `CLOVA_SECRET`: CLOVA API 인증 키.

### 3. 디스코드 봇 권한 설정
- **Discord Developer Portal**: [https://discord.com/developers/applications](https://discord.com/developers/applications)  
- **OAuth2 → URL Generator** 설정:  
  - **Scopes**:  
    - `bot`  
    - `applications.commands`  
  - **Bot Permissions**:  
    - `Manage Channels`  
    - `Send Messages`  
    - `Read Message History`  
    - `View Channels`  
- 생성된 URL로 서버에 봇 초대:  
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=274877908992&scope=bot%20applications.commands

## ✅ 사용 방법
- **새 유저가 서버에 입장하면?**  
  - 자동으로 `private-닉네임` 형식의 비공개 채널이 생성됩니다.  
- **유저가 상담 시작**  
  - 예: `!아파 머리가 아파요`  
  - 응답 예시:  
    머리가 아프셨다니 정말 힘드셨겠어요. 혹시 스트레스나 수면 부족이 있으셨나요? 이런 증상은 신경과나 내과를 방문해 보시는 게 좋을 것 같아요. 정확한 진단은 병원에서 확인받아 보시고, 빨리 나으시길 바랄게요!

## 🧠 사용 모델 정보
- **모델**: CLOVA HCX-DASH-001  
- **API 방식**: `aiohttp`를 통한 비동기 요청, CLOVA Studio API 사용.

## 🧪 테스트 체크리스트
- [x] 유저 입장 시 비공개 채널 생성됨  
- [x] 채널에 유저 외 접근 불가 (관리자 접근 차단 확인)  
- [x] `!아파` 명령어 정상 응답   
- [x] CLOVA API 키 정상 연결됨  

## 참고자료
- [Discord.py 공식 문서](https://discordpy.readthedocs.io/en/stable/)  
- [CLOVA Studio API 가이드](https://www.ncloud.com/product/aiService/clovaStudio)  
- [Velog: AI 챗봇 제작](https://velog.io/@chuu1019/AI-ChatGpt4-Discord-Bot-%EB%A7%8C%EB%93%A4%EA%B8%B0-feat.-python)  
- Grok 3 (xAI)을 통한 코드 디버깅 및 프롬프트 최적화 (사용 비율 약 70%)
