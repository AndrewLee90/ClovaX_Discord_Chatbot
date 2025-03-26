# 💊 Medical_Advice_Bot: 당신의 건강 비서

## ✨ 이 봇이 특별한 이유
- **입장 즉시 나만의 상담실**: 서버에 들어오자마자 `private-닉네임`이라는 비밀 공간이 생깁니다. 당신만의 건강 상담실이에요!
- **의사처럼 따뜻한 대화**: `!아파 증상` (예: `!아파 목이 따끔거려요`)를 입력하면 CLOVA AI가 공감하며 조언을 건넵니다.
- **철저한 프라이버시**: 이곳은 오직 당신만을 위한 공간. 관리자도 엿볼 수 없어요.
- **친절함 100% 보장**: 차가운 설명 대신, 따뜻한 위로와 함께 실질적인 도움을 드립니다.

## 🚀 시작하는 법

### ⚙️ 준비물 설치
터미널을 열고 다음 명령어로 필요한 도구를 설치하세요:  
pip install discord aiohttp python-dotenv  
- `discord`: 봇과 디스코드를 연결하는 마법 도구.  
- `aiohttp`: CLOVA AI와 빠르게 소통하기 위한 비밀 통로.  
- `python-dotenv`: 중요한 비밀 키를 안전하게 숨기는 보물 상자.

### 🔑 비밀 키 설정
프로젝트 폴더에 `.env`라는 파일을 만들고, 아래 두 가지 비밀 코드를 적어 주세요:  
DISCORD_TOKEN=당신의_디스코드_토큰  
CLOVA_SECRET=당신의_CLOVA_키  
- **어디서 구하나요?**  
  - `DISCORD_TOKEN`: [디스코드 개발자 포털](https://discord.com/developers/applications)에서 발급.  
  - `CLOVA_SECRET`: CLOVA Studio에서 제공받은 키.

### 🌐 봇을 서버에 초대하기
1. [Discord Developer Portal](https://discord.com/developers/applications)에 들어가세요.  
2. **OAuth2 > URL Generator**에서 다음 설정을 체크:  
   - **Scopes**: `bot`, `applications.commands`  
   - **Permissions**: `Manage Channels`, `Send Messages`, `Read Message History`, `View Channels`  
3. 생성된 링크로 봇을 초대:  
   https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=274877908992&scope=bot%20applications.commands

## 💡 어떻게 쓰나요?
- **서버에 첫발을 내딛으면**:  
  - 당신만을 위한 `private-닉네임` 채널이 뿅! 하고 나타납니다.  
- **건강 고민 털어놓기**:  
  - 입력: `!아파 배고프고 어지러워요`  
  - 답변 예시:  
    배고프고 어지럽다니 몸이 많이 놀랐나 봐요. 혹시 오늘 밥을 거프셨나요? 저혈당일 수도 있으니 간단히 간식을 드셔보세요. 그래도 나아지지 않으면 내과에 가보는 걸 추천드릴게요. 괜찮아지시길 응원할게요!

## 🧠 똑똑한 두뇌 정보
- **AI 두뇌**: CLOVA HCX-DASH-001  
- **소통 방식**: `aiohttp`로 빠르고 부드럽게 CLOVA Studio API와 대화.

## ✅ 점검 완료!
- [x] 새 유저 입장 시 나만의 채널 생성  
- [x] 관리자 접근 불가 확인  
- [x] `!아파`로 건강 조언 잘 받기  
- [x] CLOVA API 연결 성공  

## 🔗 더 궁금하다면?
- [Discord.py의 모든 것](https://discordpy.readthedocs.io/en/stable/)  
- [CLOVA Studio 탐험](https://www.ncloud.com/product/aiService/clovaStudio)  
- [AI 챗봇 제작기](https://velog.io/@chuu1019/AI-ChatGpt4-Discord-Bot-%EB%A7%8C%EB%93%A4%EA%B8%B0-feat.-python)  
- Grok 3 (xAI)와 함께한 코드 튜닝 (약 70% 활용)
