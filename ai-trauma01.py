#
#  Trauma  마음에 상처 극복하기
#
import streamlit as st

# 페이지 설정 (배경색 등 추가 가능)
st.set_page_config(page_title="마음에 상처, 트라우마 극복하기", layout="wide")

# CSS 스타일 적용
st.markdown("""
<style>
    /* 버튼 색상 커스텀 */
    .stButton>button {
        background-color: #4CAF50;  /* 초록색 계열 */
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;  /* 호버 시 색상 변경 */
    }
    
    /* 특정 버튼 별도 색상 지정 */
    #video-btn { background-color: #FF5722 !important; }  /* 주황색 */
    #talk-btn { background-color: #2196F3 !important; }   /* 파란색 */
    #ppt-btn { background-color: #9C27B0 !important; }     /* 보라색 */
    
    /* 강조 텍스트 스타일 */
    .highlight {
        font-weight: bold;
        color: #FF5722;  /* 주황색 */
    }
    .note {
        font-size: 14px;
        color: #666;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀
st.write("### 마음에 상처, 트라우마 극복하기! 👋")

# 설명 텍스트 (bold 및 색상 적용)
st.markdown("""
<span class="highlight">마음에 상처, 트라우마, 고통받고 았나요</span>  
여기 Kevin이 맛깔나게 여러 각도에서 제안 합니다.  
<span class="highlight">아래 3편을 의미 있게 보시길</span>  
""", unsafe_allow_html=True)

# # 대화 링크 버튼
st.link_button("대화 를 통해 듣기", "https://youtu.be/V_bB5ZNdQjk")

# Video 링크 버튼
st.link_button("Video 를 통해 보기", "https://youtu.be/H2sUB83lq_0")

# Video 링크 버튼
st.link_button("K Video 를 통해 보기", "https://youtu.be/8u1qwOHuge8")

# 추가 설명 (작은 글씨 + 색상)
st.markdown("""
<p class="note">※ 화면이 안 나오면 (zzz) 클릭 후 1-2분 정도 기다려주세요</p>
""", unsafe_allow_html=True)


