markdown

접기

자동 줄바꿈

복사
# 💊 Medical_Advice_Bot

## 주요 기능
- **신규 유저 입장 시 비공개 채널 자동 생성**: 서버에 입장한 신규 유저를 위해 본인만 볼 수 있는 비공개 상담 채널을 자동으로 생성합니다.
- **!아파 명령어로 CLOVA 기반 상담 응답**: 사용자가 `!아파 증상`을 입력하면 CLOVA API를 통해 의학적 상담을 제공합니다.
- **하루 최대 100회 상담 제한**: 사용자별로 하루 상담 횟수를 100회로 제한합니다 (현재 미구현, 추가 로직 필요).
- **따뜻하고 공감 어린 의사 말투**: 감정에 기반한 친절하고 위로하는 응답을 제공합니다.
- **관리자 접근 차단**: 생성된 채널은 완전한 개인 상담 공간으로, 관리자도 접근할 수 없습니다.

## 🛠 설치 및 실행 방법

### 1. Python 패키지 설치
bash
pip install discord aiohttp python-dotenv
discord: 디스코드 봇 구현을 위한 패키지.
aiohttp: CLOVA API 비동기 요청 처리.
python-dotenv: 환경 변수 관리.
2. .env 파일 생성 (최상단 디렉토리에 위치)
text

접기

자동 줄바꿈

복사
DISCORD_TOKEN=디스코드_봇_토큰
CLOVA_SECRET=CLOVA_API_키
DISCORD_TOKEN: 디스코드 개발자 포털에서 발급받은 봇 토큰.
CLOVA_SECRET: CLOVA API 인증 키.
3. 디스코드 봇 권한 설정
Discord Developer Portal: https://discord.com/developers/applications
OAuth2 → URL Generator 설정:
Scopes:
bot
applications.commands
Bot Permissions:
Manage Channels
Send Messages
Read Message History
View Channels
생성된 URL로 서버에 봇 초대:
text

접기

자동 줄바꿈

복사
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=274877908992&scope=bot%20applications.commands
✅ 사용 방법
새 유저가 서버에 입장하면?
자동으로 private-닉네임 형식의 비공개 채널이 생성됩니다.
유저가 상담 시작
예: !아파 머리가 아파요
→ 챗봇이 따뜻하고 전문적인 의학 상담으로 응답:
text

접기

자동 줄바꿈

복사
머리가 아프셨다니 정말 힘드셨겠어요. 혹시 스트레스나 수면 부족이 있으셨나요? 이런 증상은 신경과나 내과를 방문해 보시는 게 좋을 것 같아요. 정확한 진단은 병원에서 확인받아 보시고, 빨리 나으시길 바랄게요!
🧠 사용 모델 정보
모델: CLOVA HCX-DASH-001
API 방식: aiohttp를 통한 비동기 요청, CLOVA Studio API 사용.
🧪 테스트 체크리스트
 유저 입장 시 비공개 채널 생성됨
 채널에 유저 외 접근 불가 (관리자 접근 차단 확인)
 !아파 명령어 정상 응답
 하루 100회 제한 작동 (추가 구현 필요)
 CLOVA API 키 정상 연결됨
참고자료
Discord.py 공식 문서
CLOVA Studio API 가이드
Velog: AI 챗봇 제작
Grok 3 (xAI)을 통한 코드 디버깅 및 프롬프트 최적화 (사용 비율 약 70%)
현재 코드 예시
python

접기

자동 줄바꿈

복사
import discord
import aiohttp
from discord.ext import commands

DISCORD_TOKEN = 'YOUR_DISCORD_TOKEN'
CLOVA_URL = 'https://clovastudio.stream.ntruss.com/testapp/v1/chat-completions/HCX-DASH-001'
CLOVA_SECRET = 'YOUR_CLOVA_SECRET'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def call_clova_chatbot(user_input):
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': f'Bearer {CLOVA_SECRET}'
    }
    preset_text = [
        {"role": "system", "content": "친절한 의사처럼 공감하며 상담하고, 전문적인 진료과를 안내하세요."},
        {"role": "user", "content": user_input}
    ]
    payload = {'messages': preset_text, 'maxTokens': 256}
    async with aiohttp.ClientSession() as session:
        async with session.post(CLOVA_URL, headers=headers, json=payload) as response:
            if response.status == 200:
                json_data = await response.json()
                return json_data['result']['message']['content']
            return f'응답 실패: {response.status}'

@bot.event
async def on_member_join(member):
    guild = member.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    channel = await guild.create_text_channel(f"private-{member.name}", overwrites=overwrites)
    await channel.send(f"{member.mention}님, 여기가 당신의 비공개 상담 채널입니다!\n!아파 명령어로 증상을 말씀해 주세요.")

@bot.command()
async def 아파(ctx, *, user_input: str = None):
    if user_input is None:
        await ctx.send("증상이 무엇인지 알려주세요!")
        return
    response = await call_clova_chatbot(user_input)
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user.name} 봇이 로그인했습니다!')

bot.run(DISCORD_TOKEN)
참고: 하루 100회 제한 기능은 추가 구현 필요.
