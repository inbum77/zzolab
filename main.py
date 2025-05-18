import streamlit as st

# MBTI 데이터 정의
mbti_info = {
    "INTJ": {
        "성격": "전략적이고 독립적인 사고를 좋아하는 분석가예요 🧠",
        "장점": ["계획적임", "문제 해결에 능함", "자기 주도적임"],
        "단점": ["완벽주의 성향", "감정을 잘 드러내지 않음", "융통성이 부족할 수 있음"],
        "장점_팁": "계획적인 면을 살려 프로젝트를 주도해보세요! 📈",
        "단점_팁": "때때로 감정을 나누고, 유연하게 대처하는 연습을 해보세요 🌿",
        "연예인": ["아이유 🎤", "방시혁 🎹"]
    },
    "ENFP": {
        "성격": "열정적이고 상상력이 풍부한 사람입니다 🌈",
        "장점": ["창의적", "사교적", "긍정적이고 에너지 넘침"],
        "단점": ["산만함", "감정 기복", "계획성이 떨어질 수 있음"],
        "장점_팁": "사람들과의 교류에서 에너지를 얻고, 새로운 아이디어를 현실화해보세요! 🚀",
        "단점_팁": "일정한 루틴을 만들고 목표를 구체화해보세요 📅",
        "연예인": ["유재석 🎤", "박보영 🎬"]
    },
    # 다른 MBTI 유형도 여기에 추가하면 됩니다
}

# Streamlit UI
st.set_page_config(page_title="MBTI 성격 분석기", page_icon="🧬")
st.title("🧬 내 MBTI, 무엇이든 알려줄게!")

mbti_list = list(mbti_info.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", mbti_list)

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
    st.write(", ".join(info["연예인"]))
