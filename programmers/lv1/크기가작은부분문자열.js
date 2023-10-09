function solution(t, p) {
  const tLen = t.length
  const pLen = p.length
  let answer = 0

  for (let i = 0; i < tLen - pLen + 1; i++) {
    if (Number(t.slice(i, i + pLen)) <= Number(p)) {
      answer++
    }
  }

  return answer
}
