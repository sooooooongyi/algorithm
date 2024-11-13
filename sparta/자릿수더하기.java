import java.util.*;

public class Solution {

  public int solution(int n) {

    String intToStr = n + "";
    int answer = 0;

    for (String s : intToStr.split("")) {
      answer += Integer.parseInt(s);
    }

    return answer;
  }
}