let s:variable = 'test'

function test#stuff#Test()
endfunction

function! s:BadFunction()
endfunction

function! s:TestFunction() abort
  let m = s:variable
  let m = [ 'test' ]
  call filter( m, 'test' )

  call s:BadFunction()
endfunction
