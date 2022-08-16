import org.scalatest._

class FirstAndLast_34Test extends FunSuite {

  test("testFind") {
    val a = Array(5,7,7,8,8,8,10,10,10,10,11)

    var answer = FirstAndLast_34.find(a, 8)
    assert(answer.isDefined)

    assert(FirstAndLast_34.find(a, 5).isDefined)
    assert(FirstAndLast_34.find(a, 11).isDefined)
    assert(FirstAndLast_34.find(a, 12).isEmpty)
  }

  test("findLeftMost") {
    val a = Array(5,7,7,8,8,8,10,10,10,10,11)

    var answer = FirstAndLast_34.findLeftMost(a, 8)
    assert(answer.get == 3)

    answer = FirstAndLast_34.findLeftMost(a, 5)
    assert(answer.get == 0)

    answer = FirstAndLast_34.findLeftMost(a, 11)
    assert(answer.get == 10)

    answer = FirstAndLast_34.findLeftMost(a, 14)
    assert(answer.isEmpty)
  }

  test("findRightMost") {
    val a = Array(5,7,7,8,8,8,10,10,10,10,11)

    var answer = FirstAndLast_34.findRightMost(a, 8)
    assert(answer.get == 5)

    answer = FirstAndLast_34.findRightMost(a, 5)
    assert(answer.get == 0)

    answer = FirstAndLast_34.findRightMost(a, 11)
    assert(answer.get == 10)

    answer = FirstAndLast_34.findRightMost(a, 10)
    assert(answer.get == 9)

    answer = FirstAndLast_34.findRightMost(a, 14)
    assert(answer.isEmpty)
  }

  test("searchRange") {
    val a = Array(5,7,7,8,8,8,10,10,10,10,11)

    assert(FirstAndLast_34.searchRange(a, 8) === Array(3, 5))
    assert(FirstAndLast_34.searchRange(a, 5) === Array(0, 0))
    assert(FirstAndLast_34.searchRange(a, 11) === Array(10, 10))
    assert(FirstAndLast_34.searchRange(a, 10) === Array(6, 9))
    assert(FirstAndLast_34.searchRange(a, 88) === Array(-1, -1))

  }
}
