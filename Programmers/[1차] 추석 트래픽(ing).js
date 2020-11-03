// const lines = [
//     "2016-09-15 20:59:57.421 0.351s",
//     "2016-09-15 20:59:58.233 1.181s",
//     "2016-09-15 20:59:58.299 0.8s",
//     "2016-09-15 20:59:58.688 1.041s",
//     "2016-09-15 20:59:59.591 1.412s",
//     "2016-09-15 21:00:00.464 1.466s",
//     "2016-09-15 21:00:00.741 1.581s",
//     "2016-09-15 21:00:00.748 2.31s",
//     "2016-09-15 21:00:00.966 0.381s",
//     "2016-09-15 21:00:02.066 2.62s"
//     ];


// String.prototype.replaceAll = function(org, dest) {
//     return this.split(org).join(dest);
// }

// function getCorrentStartTime(S, T) {
//     let num = S.split(".");
//     let numFront = num[0];
//     let numBack =  "0." + num[1] - 0 - T + 0.001;
//     num = numFront * 1 + numBack * 1;

//     return num;
// }

// function plusTime(time) {
//     let strTime = time + "";

//     time = strTime.split(".");
//     strTime = time[0] + "";

//     const len = strTime[0].length;   
//     let second = strTime.substr(len - 2, 2) - 0;
//     let minute = strTime.substr(len - 4, 2) - 0;
//     let hour;

//     if(len == 6) {
//         hour = strTime.substr(len - 6, 2) - 0;
//     } else if(len == 5){
//         hour = strTime.substr(len - 5, 1) - 0;
//     }
    
//     if(second + 1 == 60) {
//         second = "00";
//         if(minute - 0 + 1 == 60) {
//             minute = "00";
//             hour++;
//         } else if(minute + 1 < 10) {
//             minute = "0" + (minute + 1 + "");
//         } else {
//             minute++;
//         }
//     } else if(second + 1 < 10) {
//         second = "0" + (second + 1 + ""); 
//     } else {
//         second++;
//     }

//     return (hour + "") + (minute + "") + (second + "");
// }

// function getlogNumPerSec(logList, sortList) {
//     const list = [];
//     let answer = 0;
//     const finalTime = logList[logList.length - 1][1];
//     let count = 0;

//     for(let i = 0; i < sortList.length; i++ ) {
//         if(sortList[i] >=  finalTime) {
//             break;
//         } 
//         logList.forEach(function(logTime) {
//             if(sortList[i] <= logTime[0] && logTime < plusTime(sortList[i])) {
//                 count++;
//             } else if(sortList[i] <=logTime[1] && logTime[1] < plusTime(sortList[i])) {
//                 count++;
//             } else if(logTime[0] <= sortList[i] && plusTime(sortList) <= logTime[1]) {
//                 count++;
//             }
//             console.log(sortList[i], logTime[0], logTime[1]);
//         });

//         list.push(count + 1);
//     }
// }

// function solution(lines) {
//     const logList = [];
//     const sortList = [];
//     let logNumList;
//     let answer;

//     let startTime, endTime;
//     for(let num in lines) {
//         lines[num] = lines[num].replaceAll("2016-09-15 ","").replaceAll(":","").split(" ");
//         lines[num][1] = lines[num][1].replace("s","");
//         startTime = getCorrentStartTime(lines[num][0], lines[num][1]);
//         endTime = lines[num][0] * 1;
//         logList.push([startTime, endTime]);
//         sortList.push(startTime, endTime);
//         sortList.sort();
//     }
//     console.log("sort : ", sortList);
//     answer = getlogNumPerSec(logList, sortList);

//     console.log("answer : ", answer);
//     return answer;
// }

// solution(lines);