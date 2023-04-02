function solution(array, commands) {
    var answer = [];
    for (const [i, j, k] of commands) {
        newArray = array.slice(i - 1, j)
        newArray.sort((a, b) => a - b)
        answer.push(newArray[k - 1])
    }
    
    return answer;
}