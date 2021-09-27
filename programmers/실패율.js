function solution(N, stages) {
  var answer = [];
  let challenge = Array.from({ length: N }, () => 0);
  let failure = Array.from({ length: N }, () => 0);

  for (let stage of stages) {
    if (stage === N + 1) {
      stage = N;
    } else failure[stage - 1] += 1; // stage-1에서 성공못하고 머무르고 있음
    for (let i = 0; i < stage; i++) {
      challenge[i] += 1;
    }
  }
  answer = challenge.map((stage, index) => [failure[index] / stage, index + 1]);
  return answer.sort((a, b) => b[0] - a[0]).map(([_, index]) => index);
}