import streamlit as st

# 1. CSS 스타일 정의 (반드시 따옴표 3개로 감싸야 함)
st.markdown("""
    <style>
        .periodic-table {
            display: grid;
            grid-template-columns: repeat(8, 50px);
            gap: 5px;
            margin-top: 20px;
        }
        .element {
            width: 50px; height: 50px; border: 1px solid #333;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; background: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("원소 결합 시뮬레이터")

# 2. 원소 데이터
elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", 
            "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]

# 3. HTML/JS를 이용한 주기율표 UI 렌더링
# Streamlit은 클릭 이벤트를 직접 처리하기 까다로우므로, 
# 버튼을 사용하여 원소를 선택하게 하는 것이 가장 안정적입니다.

selected = st.multiselect("원소 2개를 선택하세요:", elements, max_selections=2)

if len(selected) == 2:
    st.write(f"선택된 원소: {selected[0]} + {selected[1]}")
    # 여기에 결합 로직 추가 (간단한 예시)
    st.success(f"{selected[0]}와 {selected[1]}은(는) 결합을 형성할 가능성이 있습니다!")
else:
    st.info("원소 2개를 선택해 주세요.")
