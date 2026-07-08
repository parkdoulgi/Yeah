import streamlit as st
import math

# 스타일 정의: 원소 카드 및 레이아웃
st.markdown("""
    <style>
        .element-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            cursor: pointer;
            background-color: #f9f9f9;
            transition: 0.3s;
        }
        .element-card:hover { background-color: #e0e0e0; }
        .selected-card { background-color: #ffcc00 !important; border: 2px solid #ff9900; }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 원소 데이터
elements_data = {
    "H": {"name": "수소", "val": 1, "type": "nonmetal"}, "He": {"name": "헬륨", "val": 0, "type": "noble"},
    "Li": {"name": "리튬", "val": 1, "type": "metal"}, "Be": {"name": "베릴륨", "val": 2, "type": "metal"},
    "B": {"name": "붕소", "val": 3, "type": "nonmetal"}, "C": {"name": "탄소", "val": 4, "type": "nonmetal"},
    "N": {"name": "질소", "val": 3, "type": "nonmetal"}, "O": {"name": "산소", "val": 2, "type": "nonmetal"},
    "F": {"name": "플루오린", "val": 1, "type": "nonmetal"}, "Ne": {"name": "네온", "val": 0, "type": "noble"},
    "Na": {"name": "나트륨", "val": 1, "type": "metal"}, "Mg": {"name": "마그네슘", "val": 2, "type": "metal"},
    "Al": {"name": "알루미늄", "val": 3, "type": "metal"}, "Si": {"name": "규소", "val": 4, "type": "nonmetal"},
    "P": {"name": "인", "val": 3, "type": "nonmetal"}, "S": {"name": "황", "val": 2, "type": "nonmetal"},
    "Cl": {"name": "염소", "val": 1, "type": "nonmetal"}, "Ar": {"name": "아르곤", "val": 0, "type": "noble"},
    "K": {"name": "칼륨", "val": 1, "type": "metal"}, "Ca": {"name": "칼슘", "val": 2, "type": "metal"}
}

st.title("🧪 주기율표 결합 시뮬레이터")

# 상태 초기화
if 'selected' not in st.session_state: st.session_state['selected'] = []

# 주기율표 렌더링
st.write("### 원소를 2개 클릭하세요")
grid = st.container()
with grid:
    cols = st.columns(8)
    for i, (symbol, info) in enumerate(elements_data.items()):
        with cols[i % 8]:
            if st.button(symbol, key=f"btn_{symbol}"):
                if symbol not in st.session_state['selected']:
                    st.session_state['selected'].append(symbol)
                if len(st.session_state['selected']) > 2:
                    st.session_state['selected'] = [symbol]
                st.rerun()

# 결과 표시
if len(st.session_state['selected']) == 2:
    e1, e2 = st.session_state['selected']
    st.info(f"선택: {e1} + {e2}")
    
    # 화학식 로직
    v1, v2 = elements_data[e1]["val"], elements_data[e2]["val"]
    if v1 == 0 or v2 == 0:
        st.error("비활성 기체는 결합하지 않습니다.")
    else:
        lcm = abs(v1 * v2) // math.gcd(v1, v2)
        res = f"{e1}{lcm//v1 if lcm//v1 > 1 else ''}{e2}{lcm//v2 if lcm//v2 > 1 else ''}"
        st.success("생성된 화합물:")
        st.latex(res)
        st.write("화학적 분석: 이 결합은 원자가 전자를 공유하거나 교환하여 안정화된 결과입니다.")
        

[Image of ionic and covalent bonding examples]
