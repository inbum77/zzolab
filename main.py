import streamlit as st

mbti_info = {
    "INTJ": {
        "성격": "전략적이고 독립적인 사고를 좋아하는 분석가예요 🧠",
        "장점": ["계획적임", "문제 해결에 능함", "자기 주도적임"],
        "단점": ["완벽주의 성향", "감정을 잘 드러내지 않음", "융통성이 부족할 수 있음"],
        "장점_팁": "계획적인 면을 살려 프로젝트를 주도해보세요! 📈",
        "단점_팁": "감정을 나누고, 유연하게 대처하는 연습을 해보세요 🌿",
        "연예인": [
            ("엘론 머스크", "https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society_%28crop1%29.jpg"),
            ("아이유", "https://upload.wikimedia.org/wikipedia/commons/5/56/IU_at_Golden_Disc_Awards_2022.jpg")
        ]
    },
    "INTP": {
        "성격": "호기심 많고 분석적인 철학자예요 🤓",
        "장점": ["창의적", "논리적 사고", "독립적"],
        "단점": ["현실 감각 부족", "감정 표현 어려움"],
        "장점_팁": "복잡한 문제 해결 능력을 연구나 기획에 활용해보세요!",
        "단점_팁": "소통을 통해 아이디어를 현실과 연결해보세요.",
        "연예인": [
            ("앨버트 아인슈타인", "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg"),
            ("공유", "https://upload.wikimedia.org/wikipedia/commons/b/bf/Gong_Yoo_from_acrofan.jpg")
        ]
    },
    "ENTJ": {
        "성격": "지도자 스타일로 목표를 향해 나아가는 타입이에요 👑",
        "장점": ["결단력 있음", "조직적", "리더십 뛰어남"],
        "단점": ["지나치게 경쟁적", "감정 공감 부족"],
        "장점_팁": "조직 내에서 프로젝트 리딩 역할을 맡아보세요!",
        "단점_팁": "다른 사람의 감정에도 귀 기울여보세요.",
        "연예인": [
            ("채드윅 보스먼", "https://upload.wikimedia.org/wikipedia/commons/e/e3/Chadwick_Boseman_by_Gage_Skidmore_July_2017.jpg"),
            ("이병헌", "https://upload.wikimedia.org/wikipedia/commons/4/4f/Lee_Byung-hun_%282019%29.jpg")
        ]
    },
    "ENTP": {
        "성격": "아이디어가 넘치는 도전가예요 💡",
        "장점": ["창의적", "말 잘함", "적응력 높음"],
        "단점": ["계획 부족", "지루함을 잘 느낌"],
        "장점_팁": "새로운 프로젝트나 스타트업에 참여해보세요!",
        "단점_팁": "일관성과 루틴을 유지하는 연습이 필요해요.",
        "연예인": [
            ("로빈 윌리엄스", "https://upload.wikimedia.org/wikipedia/commons/7/74/Robin_Williams_2011a_%28cropped%29.jpg"),
            ("장기하", "https://upload.wikimedia.org/wikipedia/commons/3/35/Jang_Ki-ha_in_2017.jpg")
        ]
    },
    "INFJ": {
        "성격": "통찰력 있고 조용한 이상주의자예요 🌌",
        "장점": ["깊이 있는 통찰", "이타적", "강한 가치관"],
        "단점": ["과민함", "혼자 고민 많이 함"],
        "장점_팁": "사람들을 위한 의미 있는 일을 찾아보세요.",
        "단점_팁": "자신을 돌보는 시간도 중요해요.",
        "연예인": [
            ("니콜 키드먼", "https://upload.wikimedia.org/wikipedia/commons/a/a7/Nicole_Kidman_Cannes_2017_2.jpg"),
            ("수지", "https://upload.wikimedia.org/wikipedia/commons/1/19/Suzy_in_2019.png")
        ]
    },
    "INFP": {
        "성격": "감성적이고 상상력이 풍부한 몽상가예요 🌈",
        "장점": ["이해심 많음", "창의력 풍부", "이상주의적"],
        "단점": ["현실 회피", "우울감에 빠지기 쉬움"],
        "장점_팁": "창작 활동에 참여해 감정을 표현해보세요.",
        "단점_팁": "작은 성공 경험을 통해 현실과 연결을 시도해보세요.",
        "연예인": [
            ("팀 버튼", "https://upload.wikimedia.org/wikipedia/commons/5/52/Tim_Burton_Comic-Con_2012.jpg"),
            ("정우성", "https://upload.wikimedia.org/wikipedia/commons/e/e7/Jung_Woo-sung_in_2016.jpg")
        ]
    },
    "ENFJ": {
        "성격": "사람들을 이끄는 따뜻한 리더예요 🤝",
        "장점": ["사교성 좋음", "배려심 깊음", "열정적"],
        "단점": ["타인의 기대에 민감함", "자기 희생"],
        "장점_팁": "팀워크와 리더십을 발휘할 수 있는 활동에 참여해보세요.",
        "단점_팁": "자기 자신도 돌보는 연습을 해보세요.",
        "연예인": [
            ("오프라 윈프리", "https://upload.wikimedia.org/wikipedia/commons/8/82/Oprah_in_2014.jpg"),
            ("박서준", "https://upload.wikimedia.org/wikipedia/commons/b/b3/Park_Seo-jun_2019.png")
        ]
    },
    "ENFP": {
        "성격": "열정적이고 상상력이 풍부한 사람입니다 🌈",
        "장점": ["창의적", "사교적", "긍정적이고 에너지 넘침"],
        "단점": ["산만함", "감정 기복", "계획성이 떨어질 수 있음"],
        "장점_팁": "사람들과 교류하며 아이디어를 현실화해보세요! 🚀",
        "단점_팁": "루틴과 구체적인 목표 설정이 좋아요 📅",
        "연예인": [
            ("로버트 다우니 주니어", "https://upload.wikimedia.org/wikipedia/commons/3/3e/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg"),
            ("임윤아", "https://upload.wikimedia.org/wikipedia/commons/b/b5/Yoona_in_2021.png")
        ]
    }
}

st.set_page_config(page_title="MBTI 성격 분석기", page_icon="🧬")
st.title("🧬 MBTI 성격 분석기")
st.markdown("MBTI를 선택하면 당신의 성격, 장점과 단점, 팁, 그리고 같은 유형의 연예인을 알려드릴게요!")

selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", list(mbti_info.keys()))

if selected_mbti:
    info = mbti_info[selected_mbti]

    st.subheader(f"📌 {selected_mbti}의 성격")
    st.write(info["성격"])

    st.subheader("👍 장점")
    for good in info["장점"]:
        st.write(f"• {good}")
    st.markdown(f"💡 **장점을 살리는 방법**: {info['장점_팁']}")

    st.subheader("👎 단점")
    for bad in info["단점"]:
        st.write(f"• {bad}")
    st.markdown(f"🛠️ **단점을 줄이는 방법**: {info['단점_팁']}")

    st.subheader("🌟 같은 MBTI 연예인")
    for name, img_url in info["연예인"]:
        st.image(img_url, width=150, caption=name)
