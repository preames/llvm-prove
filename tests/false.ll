; RUN: ../llvm-prove.sh %s | FileCheck %s
; CHECK: Result proven

define i1 @test(i32 %a) {
  %add1 = add i32 %a, 9
  %add2 = add i32 %a, 7
  %res = icmp eq i32 %add1, %add2
  ret i1 %res
}
