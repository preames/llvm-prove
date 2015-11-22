; RUN: ./llvm-prove.sh %s | FileCheck %s
; CHECK: Could not prove


define i1 @test(i32 %a, i32 %b) {
  %add1 = add i32 %a, %b
  %add2 = add i32 %b, 0
  %res = icmp eq i32 %add1, %add2
  ret i1 %res
}
