// 프로그래머스_모의고사 문제
// 가장 많이 맞춘 사람 번호를 return 

function solution(answers) {
    
    const per1 = [1,2,3,4,5];
    const per2 = [2,1,2,3,2,4,2,5];
    const per3 = [3,3,1,1,2,2,4,4,5,5];
    let result = [];

    let len = answers.length;
    let cnt1, cnt2, cnt3;
    let max = 0;
    
    cnt1 = compare(per1, len, answers);
    cnt2 = compare(per2, len, answers);   
    cnt3 = compare(per3, len, answers);

    if (max < cnt1) 
       max = cnt1;  
    if (max < cnt2) 
        max = cnt2;
    if (max < cnt3) 
        max = cnt3; // let max = Math.max(cnt1, cnt2, cnt3);  

    if(max === cnt1) result.push(1);
    if(max === cnt2) result.push(2);
    if(max === cnt3) result.push(3);
    
    console.log(result);
    return result;
}

let compare = function (str, len, answers) {
    let i, j = 0;
    let count = 0;
    
    while(len > 0) {
        for(i = 0; i < str.length; i++) {
            if (len == 0) {
                break;
            } else if(str[i] === answers[j]) {
                count++;
            }
            j++;
            len--;
        }
    }
    
    return count;
}

function init () {
    solution([1,2,3,4,5,5,4,3,2,1]);
};

init();

