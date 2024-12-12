(module
  (global $global i32)
  (func $boris (result i32) (local $local i32)
    (i32.add
      (i32.const 1)
      (local.get $local))
    (i32.add
      (i32.const 1)
      (global.get $global))
    (i))
  (func $ben (result i32)
    (call $boris))
  (export $ben))
