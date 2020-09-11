let g:ycm_language_server += [
  \   {
  \     'name': 'groovy',
  \     'cmdline': [ 'java', '-jar', expand( g:ycm_lsp_dir . '/groovy/groovy-language-server/build/libs/groovy-language-server-all.jar' ) ],
  \     'filetypes': [ 'groovy' ]
  \   },
  \ ]
