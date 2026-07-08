import streamlit as st
import math

# 1. 원소 데이터
elements_data = {
    "H": {"name": "수소", "val": 1, "type": "nonmetal"}, "Li": {"name": "리튬", "val": 1, "type": "metal"},
    "Be": {"name": "베릴륨", "val": 2, "type": "metal"}, "C": {"name": "탄소", "val": 4, "type": "nonmetal"},
    "N": {"name": "질소", "val": 3, "type": "nonmetal"}, "O": {"name": "산소", "val": 2, "type": "nonmetal"},
    "F": {"name": "플루오린", "val": 1, "type": "nonmetal"}, "Na": {"name": "나트륨", "val": 1, "type": "metal"},
    "Mg": {"name": "마그네슘", "val": 2, "type": "metal"}, "Al": {"name": "알루미늄", "val": 3, "type": "metal"},
    "Cl": {"name": "염소", "val": 1, "type": "nonmetal"}, "K": {"name": "칼륨", "val": 1, "type": "metal"},
    "Ca": {"name": "칼슘", "val": 2, "type": "metal"}
}

st.title("🧪 원소 결합 시뮬레이터")

# 상태 관리
if 'selected' not in st.session_state: st.session_state['selected'] = []

# 주기율표 UI (버튼)
st.write("### 1. 주기율표에서 원소 2개 선택")
cols = st.columns(8)
for i, symbol in enumerate(elements_data.keys()):
    with cols[i % 8]:
        if st.button(symbol):
            if symbol not in st.session_state['selected']:
                st.session_state['selected'].append(symbol)
            if len(st.session_state['selected']) > 2:
                st.session_state['selected'] = [symbol]
            st.rerun()

st.write("---")

# 2. 결과 표시 UI (요청하신 형식)
st.write("### 2. 결과 분석")
sel = st.session_state['selected']

# 빈칸 표시 수식 UI
col_res = st.columns([1, 0.5, 1, 0.5, 1.5, 0.5, 2])
with col_res[0]: st.text_input("원소1", value=sel[0] if len(sel)>0 else "빈칸", disabled=True)
with col_res[1]: st.markdown("### +")
with col_res[2]: st.text_input("원소2", value=sel[1] if len(sel)>1 else "빈칸", disabled=True)
with col_res[3]: st.markdown("### =")

if len(sel) == 2:
    e1, e2 = sel
    v1, v2 = elements_data[e1]["val"], elements_data[e2]["val"]
    lcm = abs(v1 * v2) // math.gcd(v1, v2)
    formula = f"{e1}{lcm//v1 if lcm//v1 > 1 else ''}{e2}{lcm//v2 if lcm//v2 > 1 else ''}"
    
    # 비금속이 뒤로 가게 정렬하여 이름 생성
    d1, d2 = elements_data[e1], elements_data[e2]
    m, nm = (e1, e2) if d1["type"] == "metal" else (e2, e1)
    name = f"{elements_data[nm]['name'].replace('소', '화 ')} {elements_data[m]['name']}"
    
    with col_res[4]: st.text_input("화학식", value=formula, disabled=True)
    with col_res[5]: st.markdown("### =")
    with col_res[6]: st.text_input("생성물 이름", value=name, disabled=True)
else:
    with col_res[4]: st.text_input("화학식", value="?", disabled=True)
    with col_res[6]: st.text_input("생성물 이름", value="?", disabled=True)

if st.button("초기화"):
    st.session_state['selected'] = []
    st.rerun()
