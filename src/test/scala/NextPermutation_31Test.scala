import org.scalatest.FunSuite

class NextPermutation_31Test extends FunSuite {

  test("quicksort") {
    val a = Array(9,8,7,6,5,4,3,2,1)
    NextPermutation_31.quickSort(a, 0, a.length - 1)

    assert(a === Array(1,2,3,4,5,6,7,8,9))
  }

  test("qsort II") {
    val a = Array(4,3,1)

    NextPermutation_31.quickSort(a, 0, a.length - 1)
    assert(a === Array(1,3,4))
  }

  test("nextPermutation") {
    var a = Array(1,2,3,4)

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(1,2,4,3))

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(1,3,2,4))

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(1,3,4,2))

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(1,4,2,3))

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(1,4,3,2))

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(2,1,3,4))

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(2,1,4,3))
  }

  test("nextPermutation_2") {
    var a = Array(1,4,3,2)

    a = NextPermutation_31.nextPermutation(a)
    assert(a === Array(2,1,3,4))
  }
}

