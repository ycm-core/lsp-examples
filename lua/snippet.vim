" Windows: `/path/to/lua-language-server/bin/Windows/lua-language-server.exe`
" Linux: `/path/to/lua-language-server/bin/Linux/lua-language-server`
" macOS: `/path/to/lua-language-server/bin/macOS/lua-language-server`
py3 << EOF
def LuaLSPGetOS():
  import sys
  if sys.platform == 'Windows':
    return "Windows"
  elif sys.platform == 'darwin':
    return 'macOS'
  else:
    return 'Linux'
EOF

let g:ycm_language_server += [
  \   { 'name': 'lua',
  \     'filetypes': [ 'lua' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/lua/lua-language-server/root/extension/server/bin/' . py3eval( 'LuaLSPGetOS()' ) . '/lua-language-server'),
  \                  expand( g:ycm_lsp_dir . '/lua/lua-language-server/root/extension/server/main.lua' ) ]
  \   },
  \ ]
