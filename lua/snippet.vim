let g:ycm_language_server += [
  \   { 'name': 'lua',
  \     'filetypes': [ 'lua' ],
  \     'cmdline': [ g:ycm_lsp_dir . '/lua/lua-language-server/root/bin/lua-language-server' ],
  \     'capabilities': { 'textDocument': { 'completion': { 'completionItem': { 'snippetSupport': v:true } } } },
  \     'triggerCharacters': []
  \   },
  \ ]
