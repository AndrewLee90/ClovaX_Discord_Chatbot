# Discord 챗봇 with CLOVA API 연동

이 프로젝트는 Python으로 작성된 디스코드 봇으로, CLOVA AI API와 연동하여 챗봇 기능을 제공합니다. 사용자는 이 봇을 통해 증상에 대한 의학적 조언을 받을 수 있으며, 서버에 초대되었을 때 자동으로 개인 채널을 생성할 수 있습니다.

## 기능

- **프라이빗 채널 생성**: 봇이 새로운 서버에 초대되면 서버 소유자를 위해 자동으로 프라이빗 텍스트 채널을 생성합니다.
- **CLOVA API 연동**: 사용자의 입력을 CLOVA AI API에 전달하여 의료 관련 조언을 생성합니다.
- **봇 명령어**:
  - `!아파`: 사용자의 증상을 입력받아 CLOVA API에 전달하고, 응답을 받아 사용자에게 전송합니다.
  - `!프라이빗`: 사용자가 수동으로 서버에 프라이빗 채널을 생성할 수 있습니다.

## 사용된 기술

- **Python**: 봇을 구축하는 데 사용된 주요 프로그래밍 언어.
- **discord.py**: 디스코드 API와 상호작용하는 데 사용된 Python 라이브러리.
- **CLOVA AI**: 사용자 입력을 처리하고 의료 조언을 생성하는 데 사용.
- **aiohttp**: CLOVA API에 비동기 HTTP 요청을 보내는 데 사용된 라이브러리.

## 설치 방법

1. 이 저장소를 클론합니다:

git clone https://github.com/yourusername/discord-chatbot-clova.git cd discord-chatbot-clova

markdown
복사
편집

2. 필요한 라이브러리 설치:

pip install -r requirements.txt

markdown
복사
편집

3. `.env` 파일에 디스코드 봇 토큰과 CLOVA API 정보를 추가합니다:

DISCORD_TOKEN=your_discord_token CLOVA_URL=your_clova_api_url CLOVA_SECRET=your_clova_secret

markdown
복사
편집

4. 봇 실행:

python bot.py

markdown
복사
편집

## 봇 명령어

- **!아파**: 사용자가 증상을 입력하면 CLOVA API로부터 의학적 조언을 받습니다.
- **!프라이빗**: 서버에서 프라이빗 채널을 생성할 수 있습니다.

## 코드 설명

### 1. 봇 초기화 및 설정

디스코드 봇은 `discord.py` 라이브러리를 사용하여 생성되었습니다. 봇은 기본적으로 메시지 권한을 처리하고, `!` 접두사를 통해 명령어를 실행합니다.

```python
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)
2. CLOVA API 연동
call_clova_chatbot 함수는 CLOVA API를 호출하여 사용자가 입력한 증상에 대한 의학적 조언을 받습니다. API 호출은 비동기적으로 처리됩니다.

python
복사
편집
async def call_clova_chatbot(user_input):
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-NCP-CLOVASTUDIO-REQUEST-ID': '',
        'Authorization': f'Bearer {CLOVA_SECRET}'
    }
    ...
3. 프라이빗 채널 생성
서버에 봇이 초대되면 자동으로 서버 소유자에게만 접근 가능한 프라이빗 채널을 생성합니다.

python
복사
편집
@bot.event
async def on_guild_join(guild):
    try:
        owner = guild.owner
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            owner: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        private_channel = await guild.create_text_channel(f"private-{owner.name}", overwrites=overwrites)
        await private_channel.send(f"{owner.mention}님, 여기가 당신의 프라이빗 채널입니다!")
    except discord.errors.Forbidden:
        print("채널 생성 실패: '채널 관리' 권한 부족")
4. 명령어 처리
!아파 명령어는 사용자의 증상에 대한 응답을 CLOVA API로부터 받아 디스코드 채팅에 출력합니다.

python
복사
편집
@bot.command()
async def 아파(ctx, *, user_input: str = None):
    if user_input is None:
        await ctx.send("증상이 무엇인지 알려주세요!")
        return
    clova_response = await call_clova_chatbot(user_input)
    await ctx.send(clova_response)
봇 준비 완료
디스코드 봇이 로그인하면 on_ready 이벤트가 트리거되어 봇이 정상적으로 작동함을 알립니다.

python
복사
편집
@bot.event
async def on_ready():
    print(f'{bot.user.name} 봇이 로그인했습니다!')
결론
이 프로젝트는 CLOVA API를 활용하여 사용자의 증상에 대한 의료적 조언을 제공하는 디스코드 봇을 구현하는 예제입니다. 서버에 초대되면 자동으로 프라이빗 채널을 생성하여 사용자와의 비공개 대화를 제공합니다.
