import streamlit as st
# 1. o st.Page() ÿ¿¯
# ÿst.Page() ¯×~ .py þ
# Emoji Wÿhttps://tw.piliapp.com/emoji/list/
pages = [
st.Page("page_home.py", title="專案首頁", icon="👻"),
st.Page("page_map.py", title="互動地圖瀏覽", icon="🫤"),
st.Page("page_about.py", title="關於我們", icon="🫵")
]
# 2. o st.navigation() ½ (Ït)
with st.sidebar:
    st.title("App導覽")
    # st.navigation() Þóö¿¯
    selected_page = st.navigation(pages)
# 3. ¯ö¿¯
selected_page.run()