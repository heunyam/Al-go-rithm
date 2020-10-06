let s = 'abcde';

function solution(s) {
    let len = s.length;
    let result = '';

    if(len % 2 != 0) { 
        result += s[len/2 - 0.5];
        return result;
    } else {
        result += s[len/2 - 1];
        result += s[len/2];
        return result;
    }
}

function betterSolution(s) {
    return s.substr(Math.ceil(s.length / 2) - 1, s.length % 2 === 0 ? 2 : 1);
}
// substr() 는 문자열의 일부를 추출하는 함수이다.
// 예: s.substr(1, 3) s 문자열의 s[1] ~ s[3] 
// Math.ceil() 올림. 

console.log(betterSolution(s));