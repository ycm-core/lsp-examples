let g:ycm_language_server += [
  \   {
  \     'name': 'astro',
  \     'filetypes': [ 'astro' ],
  \     'cmdline': [  expand( g:ycm_lsp_dir . '/astro/node_modules/@astrojs/language-server/bin/nodeServer.js' ), '--stdio' ],
  \   },
  \ ]
