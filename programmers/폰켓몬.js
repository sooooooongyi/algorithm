function solution(nums) {
    var answer = [];
    for (const num of nums) {
        if (answer.indexOf(num) === -1) {
            answer.push(num)
        }
        if (answer.length === parseInt(nums.length/2)) break;
    }
    return answer.length;
}