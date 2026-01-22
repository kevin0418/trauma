#  Trauma  마음에 상처 극복하기
#
import streamlit as st
from PIL import Image
import io

# 페이지 설정
st.set_page_config(page_title="마음에 상처, 트라우마 극복하기", layout="wide")

# CSS 스타일 적용
st.markdown("""
<style>
    /* 기본 버튼 스타일 */
    .stButton>button {
        color: white;
        font-weight: bold;
        border: none;
        padding: 12px 28px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 8px 4px;
        cursor: pointer;
        border-radius: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* 호버 효과 */
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        opacity: 0.9;
    }
    
    /* 특정 버튼 색상 */
    .stButton>button:nth-child(1) { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;  /* 보라색 그라데이션 */
    }
    
    .stButton>button:nth-child(2) { 
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;  /* 분홍색 그라데이션 */
    }
    
    .stButton>button:nth-child(3) { 
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;  /* 하늘색 그라데이션 */
    }
    
    .stButton>button:nth-child(4) { 
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%) !important;  /* 녹색 그라데이션 */
    }
    
    .stButton>button:nth-child(5) { 
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%) !important;  /* 주황/분홍 그라데이션 */
    }
    
    .stButton>button:nth-child(6) { 
        background: linear-gradient(135deg, #30cfd0 0%, #330867 100%) !important;  /* 청록색 그라데이션 */
    }
    
    /* 이미지 버튼 특별 스타일 */
    .image-btn {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%) !important;
    }
    
    /* 강조 텍스트 스타일 */
    .highlight {
        font-weight: bold;
        background: linear-gradient(90deg, #FF416C, #FF4B2B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.2em;
    }
    
    .note {
        font-size: 14px;
        color: #888;
        font-style: italic;
        padding: 10px;
        background-color: #f9f9f9;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    /* 구분선 */
    .divider {
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        margin: 20px 0;
        border-radius: 3px;
    }
    
    /* 카드 스타일 */
    .card {
        padding: 20px;
        border-radius: 15px;
        background: white;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        margin: 15px 0;
        border-left: 5px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀
st.write("# 마음에 상처, 트라우마 극복하기! 🌈")
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 설명 텍스트
st.markdown("""
<div class="card">
    <span class="highlight">마음에 상처, 트라우마, 고통받고 계신가요?</span><br><br>
    여기 Kevin이 맛깔나게 여러 각도에서 제안합니다.<br>
    <span class="highlight">아래 다양한 자료를 통해 트라우마 극복의 길을 찾아보세요</span>
</div>
""", unsafe_allow_html=True)

# 버튼 섹션
st.markdown("### 🎬 영상 자료 보기")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("대화를 통해 듣기", "https://youtu.be/V_bB5ZNdQjk", 
                   help="트라우마 극복에 대한 대화형 컨텐츠")

with col2:
    st.link_button("Video를 통해 보기", "https://youtu.be/H2sUB83lq_0", 
                   help="트라우마 극복을 위한 시각적 가이드")

with col3:
    st.link_button("K Video를 통해 보기", "https://youtu.be/8u1qwOHuge8", 
                   help="한국어 트라우마 극복 영상")

# 이미지 버튼 섹션
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("### 🖼️ 이미지 자료 보기")

# 이미지 버튼과 표시 영역
col4, col5 = st.columns([1, 2])

with col4:
    # 이미지 버튼들
    if st.button("🧠 트라우마 극복 단계 이미지 보기", key="img1"):
        st.session_state.show_image = "trauma_stages"
    
    if st.button("💖 마음 치유 과정 이미지 보기", key="img2"):
        st.session_state.show_image = "healing_process"
    
    if st.button("🌟 긍정적 마인드셋 이미지 보기", key="img3"):
        st.session_state.show_image = "mindset"

with col5:
    # 이미지 표시 영역
    if 'show_image' in st.session_state:
        st.markdown("**이미지 자료**")
        
        # 샘플 이미지 생성 (실제 사용시에는 실제 이미지 파일로 교체)
        if st.session_state.show_image == "trauma_stages":
            # 트라우마 극복 단계 다이어그램 (가상)
            st.info("트라우마 극복의 5단계")
            st.markdown("""
            1. **인정하기** - 트라우마를 인정하고 받아들이기
            2. **정서적 처리** - 감정을 안전하게 표현하고 처리하기
            3. **재구성하기** - 경험을 새로운 관점에서 바라보기
            4. **통합하기** - 경험을 삶의 일부로 통합하기
            5. **성장하기** - 경험으로부터 의미를 찾고 성장하기
            """)
            
        elif st.session_state.show_image == "healing_process":
            # 치유 과정 이미지 (가상)
            st.success("마음 치유 과정")
            st.markdown("""
            ### 치유의 여정
            - **안전감 확립** → **감정 표현** → **이해와 통합** → **새로운 의미 부여**
            - 각 단계마다 전문가의 도움이 필요할 수 있습니다
            - 개인의 속도에 맞춰 천천히 진행하는 것이 중요합니다
            """)
            
        elif st.session_state.show_image == "mindset":
            # 긍정적 마인드셋 이미지 (가상)
            st.warning("긍정적 마인드셋 개발")
            st.markdown("""
            ### 건강한 마음가짐
            - **자기 연민**: 자신에게 친절하게 대하기
            - **현재에 집중**: 과거에 매몰되지 않기
            - **소망 품기**: 미래에 대한 희망 유지하기
            - **유연성**: 변화에 적응하는 능력 기르기
            """)
        
        # 이미지 다운로드 버튼 (실제 이미지 파일이 있다면)
        st.download_button(
            label="📥 이 내용 다운로드 (텍스트)",
            data=f"이미지 내용: {st.session_state.show_image}",
            file_name=f"{st.session_state.show_image}.txt",
            mime="text/plain"
        )

# 추가 자료 버튼
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("### 📚 추가 자료")

col6, col7 = st.columns(2)

with col6:
    if st.button("📖 자기 도움 가이드북", 
                 help="트라우마 극복을 위한 자기 도움 자료"):
        st.session_state.show_extra = "guidebook"

with col7:
    if st.button("📋 전문가 상담 안내", 
                 help="전문 상담사 연결 정보"):
        st.session_state.show_extra = "counseling"

if 'show_extra' in st.session_state:
    if st.session_state.show_extra == "guidebook":
        st.markdown("""
        <div class="card">
        <h4>📖 자기 도움 가이드북</h4>
        <ul>
        <li>일일 감정 기록하기</li>
        <li>명상과 마음챙김 연습</li>
        <li>자기 돌봄 활동 계획하기</li>
        <li>긍정적 자기 대화 연습</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.show_extra == "counseling":
        st.markdown("""
        <div class="card">
        <h4>📋 전문가 상담 안내</h4>
        <ul>
        <li>정신건강 전문의 상담</li>
        <li>트라우마 전문 심리상담사</li>
        <li>지역 정신건강 복지센터</li>
        <li>위기상담 전화: 1393</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# 추가 설명
st.markdown("""
<div class="note">
💡 **이용 안내**:
- 화면이 안 나오면 새로고침(F5) 후 1-2분 정도 기다려주세요
- 영상은 차분한 환경에서 보는 것을 추천합니다
- 필요시 내용을 메모하거나 저장해 두세요
- 본 자료는 전문적인 치료를 대체하지 않습니다
</div>
""", unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    <p>© 2024 마음 치유 가이드 | 트라우마 극복을 위한 정보 제공</p>
    <p>도움이 필요하시면 전문가의 도움을 받으세요</p>
</div>
""", unsafe_allow_html=True)