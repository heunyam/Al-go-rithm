const participant = ["stanko", "mislav", "ana"];
const completion = ["stanko", "ana", "mislav"];

function solution(par, com) {
    let parTemp = '';
    for(let i = 0, count = 0; ; i++) {
        parTemp = par.shift();
        if(parTemp === com[count]) {
            count++;
            if(count === com.length) {
                break;
            }
        } else {
            par.push(parTemp);
        }
    }

    return par;
}

const answer = solution(participant, completion);
console.log(answer);