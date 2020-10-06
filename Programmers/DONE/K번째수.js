const array = [1, 5, 2, 6, 3, 7, 4];
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];

function solution(arr, cmds) {
    let result;
    let answer = [];
    let len = cmds.length;

    for(let i = 0; i < len; i++) {
        result = arr.slice(cmds[i][0] - 1, cmds[i][1]);
        result.sort((a, b) => a - b);   
        answer.push(result[cmds[i][2] - 1]);
    }

    return answer; 
}

// refactorying
function betterSolution(arr, cmds) {
    return cmds.map(([from, to, index]) => {
        return arr.slice(from - 1, to)
                    .sort((a, b) => a - b)[index - 1]; 
    });
}
console.log(betterSolution(array, commands));