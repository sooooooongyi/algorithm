function solution(wallpaper) {
  const rowLen = wallpaper.length
  const colLen = Array.from(wallpaper[0]).length

  const rowArr = []
  const colArr = []

  for (let i = 0; i < rowLen; i++) {
    const splitedArr = Array.from(wallpaper[i])
    for (let j = 0; j < colLen; j++) {
      if (splitedArr[j] === "#") {
        rowArr.push(i)
        rowArr.push(i + 1)
        colArr.push(j)
        colArr.push(j + 1)
      }
    }
  }
  return [
    Math.min(...rowArr),
    Math.min(...colArr),
    Math.max(...rowArr),
    Math.max(...colArr),
  ]
}
