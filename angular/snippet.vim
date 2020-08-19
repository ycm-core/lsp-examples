let g:ycm_language_server += [
  \   {
  \     'name': 'angular',
  \     'cmdline': [ 'node' ,
  \        expand( g:ycm_lsp_dir . '/angular/node_modules/@angular/language-server' ),
  \        '--ngProbeLocations',
  \        expand( g:ycm_lsp_dir . '/angular/node_modules/' ),
  \        '--tsProbeLocations',
  \        expand( g:ycm_lsp_dir . '/angular/node_modules/' ),
  \        '--stdio' ],
  \     'filetypes': [ 'ts','html' ],
  \   },
  \ ]
