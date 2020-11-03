const progresses = [93, 30, 55];
const speeds = [1, 30, 5];

function solution(progresses, speeds) {
    let answer = [];
    let temp = [];
    let comp;
    let count = 0;
    
    temp = progresses.map((x, i) => Math.ceil((100 - x) / speeds[i]));
    console.log("계산용 :", temp);

    if(temp.length == 1) {
        answer.push(1);
    }
    else {
        comp = temp[0];
        for(let i = 0; i < temp.length; i++) {
            if(temp[i] <= comp) {
                count++;
            } else {
                answer.push(count);
                count = 1;
                comp = temp[i];
            }
        }
        answer.push(count);
    }
    
    return answer;
}

const answer = solution(progresses, speeds);
console.log("답 :", answer);
