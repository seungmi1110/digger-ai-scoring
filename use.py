import streamlit as st
from st_pages import add_page_title

# 현재 페이지 제목 설정
# st.page_title("사용하기", icon="🛠")

# 메인 타이틀
# st.title("📏 수학문제 자동 채점 AI")

# 설명 텍스트
st.write("📤 이미지를 업로드해주세요. AI가 채점하여 엑셀 파일 결과를 반환합니다.")

# 파일 업로드 기능
uploaded_files = st.file_uploader(
    "파일을 선택하세요.",
    type=["png", "jpg", "jpeg", "pdf"],
    accept_multiple_files=True
)

# 파일이 하나 이상 업로드되었을 때만 채점 버튼 활성화
if uploaded_files:
    st.success(f"📂 {len(uploaded_files)}개의 파일이 업로드되었습니다!")
    if st.button("🔍 채점하기"):
        st.toast("📊 AI가 채점을 진행 중입니다... (기능 구현 필요)")
else:
    st.warning("📂 최소 한 개의 파일을 업로드해주세요.")
