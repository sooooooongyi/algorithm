/*
## 코테 n솔하고 싶은 모임 | DAY 1

### SY 풀이법 💡
(여기다가 어떻게 이래이래해서 풀었는지 적어주세요~~!)
1) "여분이 있는데 도난 당했다" -> 빌려줄 수 없다 이기 때문에 우선 lost와 reserve에서 서로 겹치는 학생을 삭제
2) 새로운 newLost 배열의 아이템을 하나씩 +- 1이 reserve에 있는지 확인
3) 이전 사람이 있으면 그냥 입고 다음 사람이 있으면 입고 다음사람은 "삭제" (뒤에 또 영향 줄 수 있음)
[총평] 기본 로직은 쉬운데 조건을 생각해내기가 조금 까다로운 듯!

### JS 피드백 💬
(코드에 대한 피드백 적어주세요~~! ex 간결해서 좋았다. 시간복잡도 n^3은 ___ 이렇게 바꾸는게 좋을 것 같다.)

### Reference
(문제 출처 + 만약에 블로그 보고 풀었으면 그 출처!)
*/

function solution(n, lost, reserve) {  
    const newLost = lost.filter((s) => (reserve.indexOf(s) === -1))
    const newReserve = reserve.filter((s) => (lost.indexOf(s) === -1))
    

    newLost.sort()
    let answer = n-newLost.length
    newLost.forEach(lostStudent => {
      if (newReserve.indexOf(lostStudent - 1) !== -1) answer ++
      else if (newReserve.indexOf(lostStudent + 1) !== -1) {
          answer ++
          let reserveStudent = newReserve.indexOf(lostStudent + 1)
          newReserve.splice(reserveStudent, 1)
      }
    })
    return answer;
  }