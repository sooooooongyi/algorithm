function solution(s) {
    let numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    let answer = s;
    
    for(const [i, value] of numbers.entries()) {
        let arr = answer.split(value);
        answer = arr.join(i);
    }
    return Number(answer);

}

// https://leylaoriduck.tistory.com/451