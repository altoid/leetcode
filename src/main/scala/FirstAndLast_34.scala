object FirstAndLast_34 {

  def elementCounts(a: Array[Int]): Array[Int] = {
    a match {
      case Array() => Array[Int]()
      case Array(x, _*) => {
        val (first, rest) = a.span(p => p == x)
        first.length +: elementCounts(rest)
      }
    }
  }

  def uniques(a: Array[Int]): Array[Int] = {
    a match {
      case Array() => Array[Int]()
      case Array(x, _*) => {
        val (_, rest) = a.span(p => p == x)
        x +: uniques(rest)
      }
    }
  }

  def searchRange(a: Array[Int], target: Int): Array[Int] = {
    val nums = uniques(a)

    println(nums.mkString(" "))

    val counts = elementCounts(a)

    println(counts.mkString(" "))

    val firstIndices = counts.foldLeft(Array(0))((b, a) => (b(0) + a) +: b).tail.reverse

    println(firstIndices.mkString(" "))

    val numsToIndices = (nums zip firstIndices).toMap
    println(numsToIndices.mkString(" "))

    val numsToCounts = (nums zip counts).toMap
    println(numsToCounts.mkString(" "))
    if (numsToIndices.contains(target)) {
      Array(numsToIndices(target), numsToIndices(target) + numsToCounts(target) - 1)
    }
    else {
      Array(-1, -1)
    }
  }

  def main(args: Array[String]): Unit = {
    val a = Array(5,7,7,8,8,8,10,10,10,10,11)

    println(a.mkString(" "))

    var answer = searchRange(a, 14)
    println(answer.mkString(" "))

    answer = searchRange(a, 8)
    println(answer.mkString(" "))
  }
}
