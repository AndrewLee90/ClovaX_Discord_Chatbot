import discord
import aiohttp
from discord.ext import commands

# private Generated URL
# https://discord.com/oauth2/authorize?client_id=1354358095698202784&permissions=274877978624&integration_type=0&scope=bot

# ===== 설정 =====
DISCORD_TOKEN = ''  # 디스코드 봇 토큰
CLOVA_URL = ''  # CLOVA API URL
CLOVA_SECRET = ''  # CLOVA 인증 키

# 디스코드 봇 초기화
intents = discord.Intents.default()  # 기본 인텐트 설정 가져오기
intents.messages = True  # 메시지 읽기 권한 활성화
intents.message_content = True  # 메시지 내용 접근 권한 활성화
intents.guilds = True  # 서버 관련 이벤트(예: on_guild_join) 사용을 위해 추가

bot = commands.Bot(command_prefix="!", intents=intents)  # 봇 객체 생성: "!" 접두사로 명령어 인식

# CLOVA API 호출 함수 (비동기)
async def call_clova_chatbot(user_input):  # 사용자 입력을 받아 CLOVA API로 응답 생성
    headers = {  # API 요청 헤더
        'Content-Type': 'application/json; charset=UTF-8',
        'X-NCP-CLOVASTUDIO-REQUEST-ID': '',
        'Authorization': f'Bearer {CLOVA_SECRET}'
    }
    
    preset_text = [  # 시스템 지침과 사용자 입력 결합
        {"role": "system", "content": "최초 증상에 의한 스트레스를 이해하고 고생 많았다며 위로한 이후 친절한 의사선생님처럼 이야기하기.\r\n상태와 증상에 대한 질문에 맞는 진료과를 안내합니다.\r\n단, 모든 대답은 전문 의학과 연관되어 있어야 하며, 유사과학, 토속신앙에 의한 답변 금지.\r\n마지막에는 항상 자세한 병명은 병원에 와서 면밀한 진단 이후 알 수 있는 점을 알려주며, 인근에 있는 병원에 방문하여 빠른 조치를 권장하며 마무리."},
        {"role": "user", "content": user_input}
    ]
    
    payload = {  # API 요청 본문
        'messages': preset_text,
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 256,
        'temperature': 0.5,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True,
        'seed': 0
    }

    async with aiohttp.ClientSession() as session:  # 비동기 HTTP 세션 시작
        async with session.post(CLOVA_URL, headers=headers, json=payload) as response:  # API에 POST 요청
            print(response.status)  # 상태 코드 출력: 디버깅용
            text = await response.text()  # 응답 텍스트 가져오기
            print(text)  # 응답 내용 출력: 디버깅용
            if response.status == 200:  # 성공 시
                json_data = await response.json()
                return json_data['result']['message']['content']  # 응답 내용 반환
            return f'CLOVA 응답 실패! 상태 코드: {response.status}'  # 실패 시 오류 메시지 반환

# 서버 초대 시 자동 프라이빗 채널 생성
@bot.event
async def on_guild_join(guild):  # 봇이 서버에 초대될 때 실행
    try:
        owner = guild.owner  # 서버 소유자 정보 가져오기 (초대한 사용자로 간주)
        print(f"{guild.name} 서버에 초대됨. 소유자: {owner.name}")  # 디버깅: 초대 확인
        overwrites = {  # 채널 권한 설정
            guild.default_role: discord.PermissionOverwrite(read_messages=False),  # @everyone 차단
            owner: discord.PermissionOverwrite(read_messages=True, send_messages=True),  # 소유자 허용
            bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)  # 봇 허용
        }
        channel_name = f"private-{owner.name}"  # 고유 채널 이름 생성
        private_channel = await guild.create_text_channel(channel_name, overwrites=overwrites)  # 프라이빗 채널 생성
        await private_channel.send(f"{owner.mention}님, 여기가 당신의 프라이빗 채널입니다!\n이곳에 !아파 명령어 이후 상태와 증상을 자세히 작성해주세요.")  # 가이드 메시지 전송
        print(f"{channel_name} 채널 생성 완료")  # 디버깅: 채널 생성 확인
    except discord.errors.Forbidden:  # 권한 부족 시
        print(f"{guild.name} 서버에서 채널 생성 실패: '채널 관리' 권한 부족")
    except Exception as e:  # 기타 오류
        print(f"{guild.name} 서버에서 오류 발생: {str(e)}")

# 수동 프라이빗 채널 생성 명령어 (옵션으로 유지)
@bot.command()
async def 프라이빗(ctx):  # "!프라이빗"으로 수동 생성 (필요 시 사용)
    try:
        guild = ctx.guild  # 현재 서버 정보
        if not guild:  # DM에서 실행된 경우
            await ctx.send("이 명령어는 서버에서만 사용할 수 있습니다!")
            return
        
        author = ctx.author  # 명령어 입력한 사용자
        overwrites = {  # 채널 권한 설정
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel_name = f"private-{author.name}"  # 고유 채널 이름
        private_channel = await guild.create_text_channel(channel_name, overwrites=overwrites)  # 채널 생성
        await private_channel.send(f"{author.mention}님, 여기가 당신의 프라이빗 채널입니다!\n이곳에 !아파 명령어 이후 상태와 증상을 자세히 작성해주세요.")  # 가이드 메시지
        await ctx.send(f"{author.mention}님, {private_channel.mention} 채널이 생성되었습니다!")  # 원래 채널에 알림
    except discord.errors.Forbidden:  # 권한 부족 오류
        await ctx.send("봇에 '채널 관리' 권한이 없습니다. 서버 관리자에게 문의해 권한을 부여받거나, 봇을 새 초대 링크로 다시 추가하세요!")
    except Exception as e:  # 기타 오류
        await ctx.send(f"오류 발생: {str(e)}")

# 봇 명령어 처리
@bot.command()
async def 아파(ctx, *, user_input: str = None):  # "!아파" 명령어로 증상 처리
    if user_input is None:
        await ctx.send("증상이 무엇인지 알려주세요!")
        return
    
    clova_response = await call_clova_chatbot(user_input)  # CLOVA API 호출
    await ctx.send(clova_response)  # 응답 전송

# 메시지 처리
@bot.event
async def on_message(message):  # 메시지 수신 시 실행
    if message.author == bot.user:  # 봇 자신의 메시지면 무시
        return
    await bot.process_commands(message)  # 명령어 처리

# 봇 준비 완료
@bot.event
async def on_ready():  # 봇 로그인 완료 시 실행
    print(f'{bot.user.name} 봇이 로그인했습니다!')

# 봇 실행
bot.run(DISCORD_TOKEN)  # 봇을 디스코드에 연결