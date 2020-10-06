function solution(skill, st) {
    let answer = 0;
    let temp = '';

    for(let i = 0; i < st.length; i++) {
        for(let j = 0; j < st[i].length; j++) {
            for(let k = 0; k < skill.length; k++) {
                if(skill[k] == st[i][j]) {
                    temp += st[i][j];
                }
            }
        }
        console.log(temp);
        if(skill.indexOf(temp) === 0 || temp === "") {
            answer++;
        }
        temp = '';
    }

    // [ 'BCD', 'CBD', 'CB', 'BD' ]
    
    return answer;
}

const skill = "CBD";
const st = ["BACDE", "CBADF", "AECB", "BDA", ];
// st 에서 CBD 이외는 다 지운다

// 그이후 CBD와 비교한다. 

console.log(solution(skill, st));