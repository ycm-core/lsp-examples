let g:ycm_language_server += [
  \   { 'name': 'vala',
  \     'project_root_files': [ 'compile_commands.json', 'meson.build' ],
  \     'filetypes': [ 'vala' ],
  \     'cmdline': [ 'vala-language-server' ],
  \   },
  \ ]
