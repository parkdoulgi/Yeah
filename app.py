import streamlit as st
import math

# 1. 원소 데이터 및 명명 규칙 데이터
elements_data = {
    "H": {"name": "수소", "val": 1, "type": "nonmetal", "suffix": "화"},
    "Li": {"name": "리튬", "val": 1, "type": "metal"},
    "Be": {"name": "베릴륨", "val": 2, "type": "metal"},
    "C": {"name": "탄소", "val": 4, "type": "nonmetal", "suffix": "화"},
    "N": {"name": "질소", "val": 3, "type": "nonmetal", "suffix": "화"},
    "O": {"name": "산소", "val": 2, "type": "nonmetal", "suffix": "화"},
    "F": {"name": "플루오린", "val": 1, "type": "nonmetal", "suffix": "화"},
    "Na": {"name": "나트륨", "val": 1, "type": "metal"},
    "Mg": {"name": "마그네슘", "val": 2, "type": "metal"},
    "Al": {"name": "알루미늄", "val": 3, "type": "metal"},
    "Cl": {"name": "염소", "val": 1, "type": "nonmetal", "suffix": "화"},
    "K": {"name": "칼륨", "val": 1, "type": "metal"},
    "Ca": {"name": "칼슘", "val": 2, "type": "metal"}
}

def get_compound_info(e1, e2):
    d1, d2 = elements_data[e1], elements_data[e2]
    v1, v2 = d1["val"], d2["val"]
    
    # 화학식 생성 로직
    lcm = abs(v1 * v2) // math.gcd(v1, v2)
    ratio1 = lcm // v1
    ratio2 = lcm // v2
    
    # 화학식 문자열
    formula = f"{e1}{ratio1 if ratio1 > 1 else ''}{e2}{ratio2 if ratio2 > 1 else ''}"
    
    # 이름 생성 (비금속이 뒤로 가는 순서로 정렬 후 이름 조합)
    # 예: 염소(Cl) + 나트륨(Na) -> 염화 나트륨
    metal, nonmetal = (e1, e2) if d1["type"] == "metal" else (e2, e1)
    name = f"{elements_data[nonmetal]['name'].replace('소', '화 ')} {elements_data[metal]['name']}"
    
    return formula, name

st.title("🧪 주기율표 결합 시뮬레이터")

# 주기율표 및 선택 로직
if 'selected' not in st.session_state: st.session_state['selected'] = []
cols = st.columns(8)
for i, symbol in enumerate(elements_data.keys()):
    with cols[i % 8]:
        if st.button(symbol):
            if symbol not in st.session_state['selected']:
                st.session_state['selected'].append(symbol)
            if len(st.session_state['selected']) > 2:
                st.session_state['selected'] = [symbol]
            st.rerun()

# 결과 UI
st.write("---")
sel = st.session_state['selected']
if len(sel) == 2:
    e1, e2 = sel
    f, name = get_compound_info(e1, e2)
    
    # 결과 레이아웃
    c1, c2, c3, c4, c5 = st.columns([1, 0.3, 1, 0.3, 1.5])
    c1.metric("원소 1", e1)
    c3.metric("원소 2", e2)
    c5.write(f"### ${e1} + {e2} \\rightarrow {f}$")
    
    st.success(f"결합 생성물: **{name}** ($ {f} $)")
    
    # 학습을 위한 시각 자료 트리거
    st.write("화학 결합의 기초 원리를 확인해 보세요.")
