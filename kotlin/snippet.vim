let g:ycm_language_server += [
  \   { 'name': 'kotlin',
  \     'filetypes': [ 'kotlin' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/kotlin/KotlinLanguageServer/server/build/install/server/bin/kotlin-language-server' ) ],
  \   },
  \ ]
