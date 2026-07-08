<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>원소 결합 프로그램</title>
    <style>
        /* CSS는 반드시 여기 style 태그 안에 있어야 합니다 */
        .periodic-table {
            display: grid;
            grid-template-columns: repeat(8, 50px);
            gap: 5px;
            margin: 20px;
        }
        .element {
            width: 50px; height: 50px; border: 1px solid #333;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; background: #f0f0f0;
        }
        .element:hover { background: #ddd; }
        .selected { background: #ffcc00 !important; }
    </style>
</head>
<body>

    <h1>원소 결합 시뮬레이터 (1~20번)</h1>
    <div class="periodic-table" id="table"></div>
    <div id="result">원소 2개를 선택하세요.</div>

    <script>
        const elements = {
            "H": { name: "수소", en: 2.2 }, "He": { name: "헬륨", en: 0 },
            "Li": { name: "리튬", en: 0.98 }, "Be": { name: "베릴륨", en: 1.57 },
            "B": { name: "붕소", en: 2.04 }, "C": { name: "탄소", en: 2.55 },
            "N": { name: "질소", en: 3.04 }, "O": { name: "산소", en: 3.44 },
            "F": { name: "플루오린", en: 3.98 }, "Ne": { name: "네온", en: 0 },
            "Na": { name: "나트륨", en: 0.93 }, "Mg": { name: "마그네슘", en: 1.31 },
            "Al": { name: "알루미늄", en: 1.61 }, "Si": { name: "규소", en: 1.90 },
            "P": { name: "인", en: 2.19 }, "S": { name: "황", en: 2.58 },
            "Cl": { name: "염소", en: 3.16 }, "Ar": { name: "아르곤", en: 0 },
            "K": { name: "칼륨", en: 0.82 }, "Ca": { name: "칼슘", en: 1.00 }
        };

        const table = document.getElementById('table');
        let selected = [];

        Object.keys(elements).forEach(symbol => {
            const div = document.createElement('div');
            div.className = 'element';
            div.innerText = symbol;
            div.onclick = () => {
                if (selected.length < 2 && !selected.includes(symbol)) {
                    selected.push(symbol);
                    div.classList.add('selected');
                }
                if (selected.length === 2) {
                    const [e1, e2] = selected;
                    const diff = Math.abs(elements[e1].en - elements[e2].en);
                    const type = diff > 1.7 ? "이온 결합" : "공유 결합";
                    document.getElementById('result').innerText = `${e1}와 ${e2}는 ${type}을 형성합니다.`;
                }
            };
            table.appendChild(div);
        });
    </script>
</body>
</html>
