; RUN: ../llvm-prove.sh %s | FileCheck %s
; CHECK: Result proven

define i1 @test(i32 %a, i32 %b) {
  %add1 = add i32 %a, %b
  %add2 = add i32 %b, %a
  %res = icmp eq i32 %add1, %add2
  ret i1 %res
}
