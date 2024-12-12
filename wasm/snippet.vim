let g:ycm_language_server += [
  \   {
  \     'name': 'wasm-language-tools',
  \     'cmdline': [ g:ycm_lsp_dir .. '/wasm/root/bin/wat_server' ],
  \     'filetypes': [ 'wat' ],
  \   },
  \ ]
