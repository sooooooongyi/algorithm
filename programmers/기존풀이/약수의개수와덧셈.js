function findDivisor(num) {
    let count = 0
    for (let i = 1; i < num + 1; i ++) {
        if (num%i === 0) {
            count ++
        }
    }
    return count
}

function solution(left, right) {
    var answer = 0;
    for(let i = left; i < right + 1; i ++) {
        console.log(findDivisor(i))
        if (findDivisor(i)%2 === 0) {
            answer += i
        } else {
            answer -= i
        }
    }
    return answer;
}