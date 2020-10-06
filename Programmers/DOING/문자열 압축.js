const s = "abcabcdede";

function solution (s) 
{
    let flagCount = 0;
    let temp = 0;
    let answer = s.length;
    let cur;
    let arr = [];

    for(let counter = 1; counter <= (s.length / 2); counter++) {
        for(let i = 0; i < s.length; i += counter) {
            arr.push(s.substr(i, counter)); 
        } // 문자열 단위로 잘라서 배열에 보관
        
        // arr = [abc abc ded e]

        cur = arr[0]; // cur = abc
        temp += cur.length; // temp = 3
        flagCount = 1; 

        for(let j = 1; j < arr.length; j++) {
            if(cur === arr[j]) { // false
                flagCount++; 
            } else {
                if(flagCount !== 1)
                    temp += (flagCount + '').length; // 

                temp += arr[j].length; 
                cur = arr[j];
                flagCount = 1; 
            }
        }
        if(flagCount !== 1) 
            temp += (flagCount + '').length;
        answer = (temp < answer) ? temp : answer;
        arr = [];
        temp = 0;
    }
    return answer;
}

let answer = solution(s);
console.log(answer); // 8
