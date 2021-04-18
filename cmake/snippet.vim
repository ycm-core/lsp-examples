let s:pip_os_dir = 'bin'
if has('win32') || has('win64')
    let s:pip_os_dir = 'Scripts'
end

let g:ycm_language_server += [
  \   {
  \     'name': 'cmake',
  \     'cmdline': [ expand( s:lsp . '/cmake/venv/' . s:pip_os_dir . '/cmake-language-server' )],
  \     'filetypes': [ 'cmake' ],
  \   },
  \ ]
