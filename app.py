import streamlit as st
import math

# 1. 1~20번 원소 데이터 (이름 추가)
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

st.title("🧪 원소 결합 분석기")

# 상태 초기화
if 'selected' not in st.session_state: st.session_state['selected'] = []

# 주기율표 UI
st.write("### 1. 주기율표에서 원소를 클릭하세요")
cols = st.columns(8)
for i, symbol in enumerate(elements_data.keys()):
    with cols[i % 8]:
        if st.button(symbol, key=f"btn_{symbol}"):
            if symbol not in st.session_state['selected']:
                st.session_state['selected'].append(symbol)
            if len(st.session_state['selected']) > 2:
                st.session_state['selected'] = [symbol]
            st.rerun()

# 2. 결과 표시 UI (요청하신 방식)
st.write("---")
st.write("### 2. 결합 분석")

sel = st.session_state['selected']
# 빈칸 표시
c1, c2, c3, c4 = st.columns([1, 0.5, 1, 1.5])
with c1: st.text_input("첫 번째 원소", value=sel[0] if len(sel)>0 else "", disabled=True)
with c2: st.write("### +")
with c3: st.text_input("두 번째 원소", value=sel[1] if len(sel)>1 else "", disabled=True)

if len(sel) == 2:
    e1, e2 = sel
    v1, v2 = elements_data[e1]["val"], elements_data[e2]["val"]
    
    if v1 == 0 or v2 == 0:
        st.error("비활성 기체는 결합하지 않습니다.")
    else:
        # 화학식 계산
        lcm = abs(v1 * v2) // math.gcd(v1, v2)
        formula = f"{e1}{lcm//v1 if lcm//v1 > 1 else ''}{e2}{lcm//v2 if lcm//v2 > 1 else ''}"
        
        # 결과 출력 (공식 = 결과)
        st.write("#### 결과 출력:")
        st.success(f"화학식: ${formula}$")
        # 간단한 이름 매칭 (예시)
        name = "결합 화합물"
        if formula == "NaCl": name = "염화 나트륨"
        elif formula == "H2O": name = "물"
        elif formula == "CaCl2": name = "염화 칼슘"
        st.write(f"물질 이름: **{name}**")

if st.button("초기화"):
    st.session_state['selected'] = []
    st.rerun()
