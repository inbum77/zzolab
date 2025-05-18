import streamlit as st

mbti_info = {
    "INTJ": {
        "성격": "전략적이고 독립적인 사고를 좋아하는 분석가예요 🧠📊",
        "장점": ["계획적임 ✅", "문제 해결에 능함 🛠️", "자기 주도적임 🚀"],
        "단점": ["완벽주의 성향 😵", "감정을 잘 드러내지 않음 😐", "융통성이 부족할 수 있음 🔒"],
        "장점_팁": "계획적인 면을 살려 프로젝트를 주도해보세요! 💼✨",
        "단점_팁": "감정을 나누고, 유연하게 대처하는 연습을 해보세요 🌿🗣️",
        "연예인": [
            ("엘론 머스크", "https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society_%28crop1%29.jpg"),
            ("아이유", "https://upload.wikimedia.org/wikipedia/commons/5/56/IU_at_Golden_Disc_Awards_2022.jpg")
        ]
    },
    "INTP": {
        "성격": "호기심 많고 분석적인 철학자예요 🤓🔍",
        "장점": ["창의적 🎨", "논리적 사고 🧠", "독립적 🧍‍♂️"],
        "단점": ["현실 감각 부족 🌫️", "감정 표현 어려움 😶"],
        "장점_팁": "복잡한 문제 해결 능력을 연구나 기획에 활용해보세요! 🧪",
        "단점_팁": "소통을 통해 아이디어를 현실과 연결해보세요. 💬🔗",
        "연예인": [
            ("앨버트 아인슈타인", "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg"),
            ("공유", "https://upload.wikimedia.org/wikipedia/commons/b/bf/Gong_Yoo_from_acrofan.jpg")
        ]
    },
    "INFJ": {
        "성격": "통찰력 있고 이상주의적인 조언자예요 🔮💬",
        "장점": ["깊은 공감 능력 ❤️", "통찰력 👁️", "도움 주기를 좋아함 🤝"],
        "단점": ["내향적 경향 🤐", "감정 기복 📉"],
        "장점_팁": "타인을 이해하고 돕는 능력을 상담이나 교육 분야에 살려보세요 🎓",
        "단점_팁": "스스로의 감정을 관리하며 자기 돌봄을 잊지 마세요 🌸",
        "연예인": [
            ("칼 융", "https://upload.wikimedia.org/wikipedia/commons/0/0b/Carljung2.jpg"),
            ("정해인", "https://upload.wikimedia.org/wikipedia/commons/1/12/Jung_Hae-in_from_ACROFAN.jpg")
        ]
    },
    "INFP": {
        "성격": "이상과 가치를 중시하는 낭만주의자예요 🌈📚",
        "장점": ["창의적 🎭", "이타적 💖", "깊은 내면의 성찰 🤔"],
        "단점": ["현실 도피 경향 🕳️", "결단력 부족 😓"],
        "장점_팁": "예술, 문학, 봉사활동 등 가치 있는 활동으로 표현해보세요 🎨",
        "단점_팁": "작은 결정부터 실천하며 현실감을 키워보세요 🪴",
        "연예인": [
            ("윌리엄 셰익스피어", "https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg"),
            ("태연", "https://upload.wikimedia.org/wikipedia/commons/2/25/Taeyeon_for_Elle_Korea_2023.jpg")
        ]
    },
    "ENTJ": {
        "성격": "리더십 있고 추진력 강한 통솔자예요 👑⚡",
        "장점": ["결단력 💪", "목표 지향적 🎯", "통솔력 👍"],
        "단점": ["지나치게 경쟁적 🔥", "감정에 무관심할 수 있음 😶"],
        "장점_팁": "조직을 이끄는 리더 역할에서 진가를 발휘해보세요 🏢",
        "단점_팁": "주변 사람들의 감정을 살피고 배려하는 연습을 해보세요 🤗",
        "연예인": [
            ("마거릿 대처", "https://upload.wikimedia.org/wikipedia/commons/a/aa/Margaret_Thatcher.png"),
            ("김혜수", "https://upload.wikimedia.org/wikipedia/commons/3/3e/Kim_Hye-soo_from_ACROFAN.jpg")
        ]
    },
    "ENTP": {
        "성격": "호기심 많고 논쟁을 즐기는 혁신가예요 💭🔍",
        "장점": ["창의적 💡", "논리적 🧩", "적응력 있음 🐬"],
        "단점": ["규칙을 싫어함 🚫", "집중력 부족 📢", "논쟁적 🔥"],
        "장점_팁": "창의성과 논리력을 새로운 시스템 개발에 활용해보세요 🚀",
        "단점_팁": "중요한 일에 에너지를 집중하고 타인의 의견도 존중해보세요 🎯",
        "연예인": [
            ("마크 트웨인", "https://upload.wikimedia.org/wikipedia/commons/0/0c/Mark_Twain_by_AF_Bradley.jpg"),
            ("이영자", "https://upload.wikimedia.org/wikipedia/commons/1/15/Lee_Yeong-ja_in_2020.jpg")
        ]
    },
    "ENFP": {
        "성격": "에너지 넘치고 창의적인 열정가예요 🌟🎉",
        "장점": ["사교적 🗣️", "긍정적 🌞", "아이디어 풍부 💡"],
        "단점": ["산만할 수 있음 🌀", "계획 부족 📆❌"],
        "장점_팁": "다양한 사람과의 소통에서 창의력을 발휘해보세요 🎭",
        "단점_팁": "일정을 정리하고 목표를 설정해 집중력을 높여보세요 📋🖊️",
        "연예인": [
            ("로버트 다우니 주니어", "https://upload.wikimedia.org/wikipedia/commons/2/23/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg"),
            ("유재석", "https://upload.wikimedia.org/wikipedia/commons/3/3f/Yoo_Jae-suk_in_2019.jpg")
        ]
    },
    "ENFJ": {
        "성격": "따뜻하고 열정적인 리더예요 🔥🤝",
        "장점": ["카리스마 있음 ✨", "공감 능력 뛰어남 ❤️", "조직적 🗂️"],
        "단점": ["자기 희생적 경향 😓", "완벽주의 📏"],
        "장점_팁": "조직 내 리더로서 팀원과 조화를 이루어보세요 🧑‍🤝‍🧑",
        "단점_팁": "자신을 돌보는 시간을 확보하세요 🧘‍♀️",
        "연예인": [
            ("바락 오바마", "https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg"),
            ("박보영", "https://upload.wikimedia.org/wikipedia/commons/f/ff/Park_Bo-young_from_ACROFAN.jpg")
        ]
    },
    "ESTJ": {
        "성격": "실용적이고 책임감 강한 관리자예요 📋🔧",
        "장점": ["체계적 📊", "현실적 🧱", "리더십 강함 🧭"],
        "단점": ["융통성 부족 🔒", "감정에 둔감할 수 있음 😐"],
        "장점_팁": "업무 관리와 책임 있는 역할에서 강점을 발휘해보세요 🛠️",
        "단점_팁": "다른 의견을 존중하고 융통성을 길러보세요 🌈",
        "연예인": [
            ("저지 주디", "https://upload.wikimedia.org/wikipedia/commons/6/60/Judge_Judy_Sheindlin_2012.jpg"),
            ("이순재", "https://upload.wikimedia.org/wikipedia/commons/e/e2/Lee_Soon-jae_at_BIFF_2017.jpg")
        ]
    },
    "ESTP": {
        "성격": "행동력 있고 모험적인 사업가예요 🏄‍♂️💼",
        "장점": ["실용적 🛠️", "적응력 있음 🦎", "행동력 강함 🚀"],
        "단점": ["인내심 부족 ⏱️", "계획성 부족 📝❌"],
        "장점_팁": "위기 대처능력과 실행력을 살려 도전적인 일에 도전해보세요 🏆",
        "단점_팁": "장기적 목표를 세우고 꾸준히 추진해보세요 🌱",
        "연예인": [
            ("도널드 트럼프", "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg"),
            ("이수근", "https://upload.wikimedia.org/wikipedia/commons/4/40/Lee_Soo-geun_in_2019.jpg")
        ]
    },
    "ESFP": {
        "성격": "자유롭고 즉흥적인 연예인 기질이에요 🎭✨",
        "장점": ["사교적 🥂", "에너지 넘침 ⚡", "긍정적 🌈"],
        "단점": ["충동적 🎯", "계획성 부족 📅❌"],
        "장점_팁": "사람들과 어울리며 예술적 재능을 발휘해보세요 🎨",
        "단점_팁": "중요한 결정 전에 충분히 생각하는 습관을 들여보세요 🤔",
        "연예인": [
            ("마릴린 먼로", "https://upload.wikimedia.org/wikipedia/commons/b/ba/Marilyn_Monroe_1961.jpg"),
            ("이효리", "https://upload.wikimedia.org/wikipedia/commons/3/3b/Lee_Hyori_on_March_29%2C_2013.jpg")
        ]
    },
    "ESFJ": {
        "성격": "인기 많고 세심한 사교가예요 🥰👋",
        "장점": ["협조적 🤝", "조직적 📋", "사람 관계에 능함 👥"],
        "단점": ["비판에 민감함 😢", "지나친 동조 경향 👍"],
        "장점_팁": "사람들을 모으고 돌보는 능력을 살려보세요 💐",
        "단점_팁": "자신의 의견도 소중히 여기고 표현하는 연습을 해보세요 🗣️",
        "연예인": [
            ("테일러 스위프트", "https://upload.wikimedia.org/wikipedia/commons/b/b5/191125_Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.png"),
            ("전현무", "https://upload.wikimedia.org/wikipedia/commons/6/66/Jun_Hyun-moo_in_December_2021.jpg")
        ]
    },
    "ISTJ": {
        "성격": "신중하고 책임감 있는 현실주의자예요 📝🧮",
        "장점": ["믿음직함 🤞", "체계적 📊", "꼼꼼함 🔍"],
        "단점": ["변화를 꺼림 🔄❌", "융통성 부족 🚧"],
        "장점_팁": "세부 사항을 꼼꼼히 살피는 능력을 업무에 활용해보세요 📋",
        "단점_팁": "작은 변화부터 시도하며 적응력을 키워보세요 🌱",
        "연예인": [
            ("퀸 엘리자베스 2세", "https://upload.wikimedia.org/wikipedia/commons/b/b6/Queen_Elizabeth_II_in_March_2015.jpg"),
            ("신동엽", "https://upload.wikimedia.org/wikipedia/commons/9/91/Shin_Dong-yup_in_Jan_2019.jpg")
        ]
    },
    "ISTP": {
        "성격": "조용하고 분석적인 기술자예요 🔧🔍",
        "장점": ["실용적 🛠️", "적응력 강함 🦎", "문제해결 능력 🧩"],
        "단점": ["감정표현 부족 😶", "장기적 계획 어려움 🗓️"],
        "장점_팁": "기술적 문제를 해결하는 능력을 살려보세요 ⚙️",
        "단점_팁": "감정을 표현하고 장기적 목표를 세워보세요 🎯",
        "연예인": [
            ("클린트 이스트우드", "https://upload.wikimedia.org/wikipedia/commons/a/ac/Clint_Eastwood_2010.jpg"),
            ("현빈", "https://upload.wikimedia.org/wikipedia/commons/9/9e/Hyun_Bin_at_Canton_Fair_Complex_for_Tom_Ford_on_March_31%2C_2023_%282%29.jpg")
        ]
    },
    "ISFP": {
        "성격": "감성적이고 예술적인 모험가예요 🎨🦋",
        "장점": ["창의적 🖌️", "감성이 풍부함 💝", "평화로움 🕊️"],
        "단점": ["경쟁을 피함 🏆❌", "계획성 부족 📆"],
        "장점_팁": "예술적 감각을 디자인이나 음악 등에 활용해보세요 🎵",
        "단점_팁": "작은 목표를 세우고 성취감을 맛보세요 ✅",
        "연예인": [
            ("마이클 잭슨", "https://upload.wikimedia.org/wikipedia/commons/4/44/Michael_jackson_1757322_cropped.jpg"),
            ("박서준", "https://upload.wikimedia.org/wikipedia/commons/a/a0/Park_Seo-joon_at_the_Park_Seo-joon_Asia_Tour_%27Guess_Who%3F%27_Fan_Meeting_on_July_2022_01.jpg")
        ]
    },
    "ISFJ": {
        "성격": "따뜻하고 헌신적인 수호자예요 🛡️🧸",
        "장점": ["배려심 깊음 💕", "책임감 있음 📋", "꼼꼼함 🔍"],
        "단점": ["변화를 두려워함 🔄😨", "자기주장 부족 🤐"],
        "장점_팁": "세심함과 배려심을 교육, 의료 등 돌봄 분야에 활용해보세요 🏥",
        "단점_팁": "자신의 의견을 표현하고 새로운 경험을 시도해보세요 🌈",
        "연예인": [
            ("케이트 미들턴", "https://upload.wikimedia.org/wikipedia/commons/5/5e/Duchess_of_Cambridge_at_National_Portrait_Gallery.jpg"),
            ("수지", "https://upload.wikimedia.org/wikipedia/commons/4/40/Suzy_at_Asia_Artists_Awards_on_December_2%2C_2020_04.png")
        ]
    }
}

st.set_page_config(page_title="MBTI 성격 분석기", page_icon="🧬")
st.title("🧬 MBTI 성격 분석기")
st.markdown("MBTI를 선택하면 당신의 성격, 장점과 단점, 팁, 그리고 같은 유형의 연예인을 알려드릴게요! 😄")

selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", list(mbti_info.keys()))

if selected_mbti:
    info = mbti_info[selected_mbti]

    st.subheader(f"📌 {selected_mbti}의 성격")
    st.write(info["성격"])

    st.subheader("👍 장점")
    for good in info["장점"]:
        st.markdown(f"- {good}")
    st.markdown(f"💡 **장점을 살리는 방법**: {info['장점_팁']}")

    st.subheader("👎 단점")
    for bad in info["단점"]:
        st.markdown(f"- {bad}")
    st.markdown(f"🛠️ **단점을 줄이는 방법**: {info['단점_팁']}")

    st.subheader("🌟 같은 MBTI 연예인")
    col1, col2 = st.columns(2)
    
    for i, (name, img_url) in enumerate(info["연예인"]):
        if i % 2 == 0:
            with col1:
                st.image(img_url, width=200, caption=f"🎬 {name}")
        else:
            with col2:
                st.image(img_url, width=200, caption=f"🎬 {name}")
