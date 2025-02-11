import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

# 섹션 표시 여부를 토글할 수 있도록 설정
sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

# 네비게이션 로드
nav = get_nav_from_toml(
    "streamlits/pages.toml"
)

# 네비게이션
pg = st.navigation(nav)

# 페이지 타이틀
add_page_title(pg)

# 선택된 페이지 실행하기
pg.run()
