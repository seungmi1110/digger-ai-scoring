import streamlit as st
import zipfile
import io
import os

st.markdown("<h3><b>📤 정보를 입력하고 이미지 압축 폴더를 업로드해주세요.</b></h3>", unsafe_allow_html=True)
st.write("AI가 채점하여 엑셀 파일 결과를 반환합니다.")

# 사용자 입력 필드 추가(교수님 사번, 과목명, 과제 분류, 부분점수 여부)
professor_id = st.text_input("👨‍🏫 **교수님 사번** 입력")
subject_name = st.text_input("📚 **과목명** 입력")
assignment_type = st.text_input("📑 **과제 분류** 입력 (예: 중간고사, 기말고사, 과제1 ...)")
partial_scoring = st.checkbox("✅ **부분 점수 허용** 여부")

# 공백
st.markdown("<br>", unsafe_allow_html=True)

# 압축 폴더 업로드 2개 UI를 가로로 배치
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h4>📄 <b>문제</b> 압축 폴더 업로드</h4>", unsafe_allow_html=True)
    problem_files = st.file_uploader(
        "📥 **문제 파일을 선택하세요.**",
        type=["zip"],
        accept_multiple_files=False
    )
    problem_extracted = []
    if problem_files:
        with zipfile.ZipFile(io.BytesIO(problem_files.read()), 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                if file_name.endswith((".png", ".jpg", ".jpeg", ".pdf")):
                    problem_extracted.append(file_name)
        st.success(f"📄 문제 파일 {len(problem_extracted)}개 압축 해제 완료!")

with col2:
    st.markdown("<h4>📝 <b>학생 풀이</b> 압축 폴더 업로드</h4>", unsafe_allow_html=True)
    solution_files = st.file_uploader(
        "📥 **풀이 파일을 선택하세요.**",
        type=["zip"],
        accept_multiple_files=False
    )
    solution_extracted = []
    if solution_files:
        with zipfile.ZipFile(io.BytesIO(solution_files.read()), 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                if file_name.endswith((".png", ".jpg", ".jpeg", ".pdf")):
                    solution_extracted.append(file_name)
        st.success(f"📝 풀이 파일 {len(solution_extracted)}개 압축 해제 완료!")

# 공백
st.markdown("<br>", unsafe_allow_html=True)

# 확인 버튼 및 입력 내용 확인 
if st.button("✅ 확인"):
    st.markdown(f"""
    <div style='background-color:#f0f0f0; padding:10px; border-radius:10px;'>
        <b>👨‍🏫 교수님 사번:</b> {professor_id}<br>
        <b>📚 과목명:</b> {subject_name}<br>
        <b>📑 과제 분류:</b> {assignment_type}<br>
        <b>✅ 부분 점수 허용 여부:</b> {'예' if partial_scoring else '아니오'}<br>
        <b>📄 문제 파일 개수:</b> {len(problem_extracted)}<br>
        <b>📝 풀이 파일 개수:</b> {len(solution_extracted)}<br>
    </div>
    """, unsafe_allow_html=True)
