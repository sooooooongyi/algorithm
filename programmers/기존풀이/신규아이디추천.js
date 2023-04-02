// 정규표현식

function solution(new_id) {
  let answer = new_id
    .toLowerCase()
    .replace(/[^a-z0-9-_.]/g, "")
    .replace(/\.+/g, ".")
    .replace(/^\.|\.$/g, "");

  /*
  1단계: 소문자
  2단계: [] => []안에 포함된 정규표현식과 일치하면 "" 빈문자열로 치환 / ^ => 제외 / a-z0-9-_. => a ~ z, 0 ~ 9, -, _ , , 
  3단계: .이 한개 이상이라면 "."으로 치환
  4단계: [] 밖 ^ => 첫 문자 $ => 끝 문자
  */

  // 5단계  
  if(answer === '') answer += 'a';
  // 6단계
  if(answer.length >= 16) answer = answer.substring(0, 15); 
  answer = answer.replace(/\.$/, '');

  // 7단계
  let length = answer.length;
  while(answer.length <= 2) {
      answer += answer[length-1];
  }
  return answer;
}
