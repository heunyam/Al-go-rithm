const p1 = ")("; // ()(())()

const isPair = (s) => {
    let cnt = 0;
    
    for(let word of s) { 
        if(word === '(') {
            cnt++;
        } else { 
            cnt--;
            if(cnt === -1) 
                return false;
        }
    }
    
    if(cnt === 0) 
        return true;
    else 
        return false;
};

function solution(p) {
    let answer = "error";
    
    if(p === "") // 1
        return ""; 
    else { // 2
        let cnt1 = 0, cnt2 = 0, idx = 0;
        let u, v, temp = '';

        for(let i = 0; i < p.length;i++) {
            if(p[i] === "(") 
                cnt1++;
            else 
                cnt2++;

            idx++;
            if(cnt1 === cnt2)
                break;
        }

        u = p.substr(0, idx);
        v = p.substr(idx, p.length - 1);
    
        if(isPair(u)) {
            return u + solution(v);
        } else {
            temp += '(';
            temp += solution(v);
            temp += ')';
            
            u = u.substr(1, u.length - 2);
            for(let i = 0; i < u.length; i++) {
                if(u[i] === '(') temp += ')';
                else temp += '(';
            }
            return temp;
        }
    }
}

console.log(solution(p1));

