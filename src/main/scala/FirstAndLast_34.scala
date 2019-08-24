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

  def stupid_searchRange(a: Array[Int], target: Int): Array[Int] = {
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

  def find(a: Array[Int], target: Int): Option[Int] = {
    def find_helper(from: Int, to: Int): Option[Int] = {
      if (to < from) None
      else {
        val m = (from + to) / 2
        if (a(m) == target) Some(m)
        else if (target < a(m)) {
          find_helper(from, m - 1)
        }
        else {
          find_helper(m + 1, to)
        }
      }
    }
    // return the index where we found the target, or None
    find_helper(0, a.length - 1)
  }

  def findLeftMost(a: Array[Int], target: Int): Option[Int] = {
    def findLeftMost_helper(from: Int, to: Int): Option[Int] = {
      // we know the target is in the array, but maybe not in this subrange.
      if (to < from) None
      else {
        val m = (from + to) / 2
        if (a(m) == target) {
          // keep looking to the left
          val result = findLeftMost_helper(from, m - 1)
          result match {
            case None => Some(m)
            case Some(_) => result
          }
        }
        else if (a(m) < target) {
          findLeftMost_helper(m + 1, to)
        }
        else {
          // target < a(m) won't happen since we are calling findLeftMost_helper on a range
          // where everything is <= target
          None
        }
      }
    }

    val anyIdx = find(a, target)

    // if we don't find the target at all, give up.
    anyIdx match {
      case None => None
      case Some(idx) => {
        val result = findLeftMost_helper(0, idx - 1)
        result match {
          case None => Some(idx)
          case Some(x) => result
        }
      }
    }
  }

  def findRightMost(a: Array[Int], target: Int): Option[Int] = {
    def findRightMost_helper(from: Int, to: Int): Option[Int] = {
      // we know the target is in the array, but maybe not in this subrange.
      if (to < from) None
      else {
        val m = (from + to) / 2
        if (a(m) == target) {
          // keep looking to the right
          val result = findRightMost_helper(m + 1, to)
          result match {
            case None => Some(m)
            case Some(_) => result
          }
        }
        else if (a(m) > target) {
          findRightMost_helper(from, m - 1)
        }
        else {
          // target > a(m) won't happen since we are calling findRightMost_helper on a range
          // where everything is >= target
          None
        }
      }
    }

    val anyIdx = find(a, target)

    // if we don't find the target at all, give up.
    anyIdx match {
      case None => None
      case Some(idx) => {
        val result = findRightMost_helper(idx + 1, a.length - 1)
        result match {
          case None => Some(idx)
          case Some(x) => result
        }
      }
    }
  }

  def searchRange(a: Array[Int], target: Int): Array[Int] = {
    val left = findLeftMost(a, target)

    left match {
      case None => Array(-1, -1)
      case Some(l) => {
        val right = findRightMost(a, target)

        right match {
          case Some(r) => Array(l, r)
          case None => throw new ArrayIndexOutOfBoundsException("wtf")
        }
      }
    }
  }

  def main(args: Array[String]): Unit = {
  }
}
