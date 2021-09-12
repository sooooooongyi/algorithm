/*
1) 최고순위 = 이미 맞은 개수 + 0의 개수
2) 최저순위 = 이미 맞은 개수
3) 이미 맞은 개수
*/

const NUMBER = 7;
const STANDARD = 6;

function solution(lottos, win_nums) {
    let matchCnt = 0;
    let zeroCnt = 0;
    for (const lotto of lottos) {
        if (win_nums.includes(lotto)) {
            matchCnt ++;
        }
        if (lotto === 0) zeroCnt++;
    }
    return [NUMBER-(matchCnt+zeroCnt) > STANDARD ? STANDARD : NUMBER-(matchCnt+zeroCnt), NUMBER - matchCnt > STANDARD ? STANDARD : NUMBER-matchCnt];
}