const arr = [4,4,4,3,3];

function solution(arr) {
    let result = [];
    let len = arr.length;
    let temp;

    for(let i = 0; i < len; i++) {
        if(arr[i] === temp) {
            continue;
        }
        temp = arr[i];
        result.push(temp);
    }
    return result;
}

function betterSolutioon(arr) {
    return arr.filter((value, index) => value != arr[index + 1]);
}

console.log(solution(arr));