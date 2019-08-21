object NextPermutation_31 {
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

    if (a.length < 2) {
      a
    }
    else {
      val i = nextSwappablePair()
      i match {
        case None => a.sorted
        case Some(x) => {
          // find index of smallest successor of a(x) to the right of x
          val rest = a.takeRight(a.length - x - 1).filter(y => y > a(x))
          val idx = a.indexWhere(x => x == rest.min)

          val t = a(idx)
          a(idx) = a(x)
          a(x) = t

          val front = a.take(x + 1)
          val back = a.takeRight(a.length - x - 1)

          front ++ back.sorted
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
