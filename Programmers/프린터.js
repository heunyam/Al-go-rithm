const priorities = [2, 1, 3, 2];
const location = 2; 
// return 1
// C D A B 

function solution(priorities, location) {
    let answer = 0;
    let max = Math.max.apply(null, priorities);
    let value = 0;

    while(1) {
        value = priorities.shift();
        if(max == value) { 
            answer++; 

            if(location == 0) 
                break;
            else 
                location--; 
                
            max = Math.max.apply(null, priorities);
        } else {
            priorities.push(value);

            if(location == 0) 
                location = priorities.length - 1;
            else 
                location--;
        }
    }
    return answer;
}

console.log(solution(priorities, location));