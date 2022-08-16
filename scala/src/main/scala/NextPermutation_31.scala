object NextPermutation_31 {

  def quickSort(a: Array[Int], from: Int, to: Int): Unit = {
    // quicksort in place

    def swap(from: Int, to: Int): Unit = {
      if (from != to) {
        val t = a(from)
        a(from) = a(to)
        a(to) = t
      }
    }

    if (from >= to) return

    val pivot_idx = to
    var left_idx = from
    var right_idx = to

    while (left_idx < right_idx) {
      while (left_idx < to && a(left_idx) <= a(pivot_idx)) {
        left_idx += 1
      }

      while (right_idx > from && a(right_idx) > a(pivot_idx)) {
        right_idx -= 1
      }

      if (left_idx < right_idx) {
        swap(left_idx, right_idx)
      }
    }

    // swap pivot with left_idx
    if (left_idx < pivot_idx) {
      swap(pivot_idx, left_idx)
    }

    quickSort(a, from, left_idx - 1)
    quickSort(a, left_idx + 1, to)
  }
  def nextPermutation(a: Array[Int]): Array[Int] = {
    // algorithm:
    //  - scan RL to first item x that is smaller than
    //    the one to its right
    //  - swap it with the smallest item to the right
    //    of x that is larger than x (y)
    //  - sort the list [x+1:]

    def nextSwappablePair(): Option[Int] = {
      assert(a.length > 1)
      for (i <- (a.length - 2) to 0 by -1) {
        if (a(i) < a(i + 1)) {
          return Some(i)
        }
      }
      None
    }

    def indexOfMinSuccessor(idx: Int): Int = {
      // return the index of the smallest item greater than a(idx) that is to the right of a(idx).
      // given the conditions under which this is called, this will always yield an answer.

      var minmax_idx = idx + 1
      for (i <- (idx + 1) until a.length) {
        if (a(i) > a(idx)) {
          if (a(i) < a(minmax_idx)) {
            minmax_idx = i
          }
        }
      }
      minmax_idx
    }

    if (a.length < 2) {
      a
    }
    else {
      val i = nextSwappablePair()
      i match {
        case None => a.sorted
        case Some(x) => {
          // find index of smallest successor of a(x) to the right of x
          val idx = indexOfMinSuccessor(x)

          val t = a(idx)
          a(idx) = a(x)
          a(x) = t

          quickSort(a, x + 1, a.length - 1)
          a
        }
      }
    }
  }

  def main(args: Array[String]): Unit = {
    var arr = Array(1,2,3,4)

    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))
//
//    println(nextPermutation(Array(4,3,2,1)).mkString(" "))

    arr = Array(1,1,5)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))

    arr = nextPermutation(arr)
    println(arr.mkString(" "))
  }
}
