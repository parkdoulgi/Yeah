const elements = {
    "H": { name: "수소", val: 1, en: 2.2 }, "He": { name: "헬륨", val: 0, en: 0 },
    "Li": { name: "리튬", val: 1, en: 0.98 }, "Be": { name: "베릴륨", val: 2, en: 1.57 },
    "B": { name: "붕소", val: 3, en: 2.04 }, "C": { name: "탄소", val: 4, en: 2.55 },
    "N": { name: "질소", val: 5, en: 3.04 }, "O": { name: "산소", val: 6, en: 3.44 },
    "F": { name: "플루오린", val: 7, en: 3.98 }, "Ne": { name: "네온", val: 0, en: 0 },
    "Na": { name: "나트륨", val: 1, en: 0.93 }, "Mg": { name: "마그네슘", val: 2, en: 1.31 },
    "Al": { name: "알루미늄", val: 3, en: 1.61 }, "Si": { name: "규소", val: 4, en: 1.90 },
    "P": { name: "인", val: 5, en: 2.19 }, "S": { name: "황", val: 6, en: 2.58 },
    "Cl": { name: "염소", val: 7, en: 3.16 }, "Ar": { name: "아르곤", val: 0, en: 0 },
    "K": { name: "칼륨", val: 1, en: 0.82 }, "Ca": { name: "칼슘", val: 2, en: 1.00 }
};
<style>
    .periodic-table {
        display: grid;
        grid-template-columns: repeat(8, 50px); /* 주기율표 형태 */
        gap: 5px;
    }
</style>

<div class="periodic-table" id="table">
    </div>
    function getBondResult(e1, e2) {
    const el1 = elements[e1];
    const el2 = elements[e2];
    
    // 1. 비활성 기체 예외 처리
    if (el1.val === 0 || el2.val === 0) return "비활성 기체는 결합하지 않습니다.";

    // 2. 전기 음성도 차이로 결합 분류
    const diff = Math.abs(el1.en - el2.en);
    let bondType = diff > 1.7 ? "이온 결합" : "공유 결합";

    // 3. 단순 화학식 생성 (전하 균형 예시)
    // 예: Na(1+) + Cl(1-) -> NaCl
    // 이 부분은 산화수 계산 로직을 고도화하면 완벽해집니다.
    return `${e1}-${e2} 결합: ${bondType}`;
}
