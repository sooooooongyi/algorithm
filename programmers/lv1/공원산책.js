function solution(park, routes) {
  const maxRow = park.length - 1
  const maxCol = park[0].length - 1

  let curRow = park.findIndex((s) => s.includes("S"))
  let curCol = park[curRow].indexOf("S")

  routes.forEach((route) => {
    let tempRow = curRow
    let tempCol = curCol

    const [direction, distance] = route.split(" ")
    let isPassed = true

    for (let i = 0; i < distance; i++) {
      if (direction === "E") tempCol += 1
      else if (direction === "W") tempCol -= 1
      else if (direction === "N") tempRow -= 1
      else if (direction === "S") tempRow += 1

      if (
        tempRow < 0 ||
        tempRow > maxRow ||
        tempCol < 0 ||
        tempCol > maxCol ||
        park[tempRow][tempCol] === "X"
      ) {
        isPassed = false
        break
      }
    }

    if (isPassed) {
      curRow = tempRow
      curCol = tempCol
    }
  })
  return [curRow, curCol]
}
