function solution(numbers) {
    const TOTAL = 45;
    return TOTAL - numbers.reduce((acc, cur, i) => acc + cur, 0);
}