const numbers = [9,34,5,30,3];

function solution(numbers) {
    var answer = '';

    answer = numbers.map(v => v + ''); // 배열 안의 요소를 문자로 바꾼다.
    console.log(answer);
    answer = answer.sort((a, b) =>
        (b + a) * 1 - (a + b) * 1 
    );
    // a = 9, b = 34 
    // (b + a) * 1 = 349,  (a + b) * 1 = 934 (349 - 934)
    // 음수이므로 그대로 
    // 양수면 자리를 바꿈
    console.log(answer);
    answer = answer.join(''); 
    // 배열을 합친다.
    console.log(answer);

    return answer[0]=== '0' ? '0' : answer;
}
console.log(solution(numbers));


