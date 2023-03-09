let g:ycm_language_server += [
  \   {
  \     'name': 'css',
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/css/node_modules/.bin/vscode-css-language-server' ), '--stdio' ],
  \     'filetypes': [ 'css', 'sass' ],
  \   },
  \ ]
