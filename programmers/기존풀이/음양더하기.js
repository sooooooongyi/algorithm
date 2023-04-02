function solution(absolutes, signs) {
    signs = signs.map(sign => sign? 1 : -1);
    return absolutes.reduce((acc, cur, i) => {
        return acc + cur * signs[i];
    }, 0);
}

// 다른 사람의 풀이
function solution(absolutes, signs) {
    return absolutes.reduce((acc, cur, i) => acc += cur * (sign[i]? 1 : -1), 0);
}