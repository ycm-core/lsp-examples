let g:ycm_language_server += [
  \   {
  \     'name': 'Jails',
  \     'cmdline': [ g:ycm_lsp_dir .. '/jai/Jails/bin/jails' ],
  \     'filetypes': [ 'jai' ],
  \     'project_root_files': [ 'jails.json', 'build.jai', 'first.jai' ],
  \   },
  \ ]
