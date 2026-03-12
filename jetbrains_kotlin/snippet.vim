let g:ycm_language_server += [
  \   {
  \     'name': 'jetbrains-kotlin',
  \     'cmdline': [
  \       expand( g:ycm_lsp_dir ) . '/jetbrains_kotlin/kotlin-lsp/kotlin-lsp.sh',
  \       '--stdio',
  \     ],
  \     'filetypes': [ 'kotlin' ],
  \     'project_root_files': [ 'build.gradle', 'build.gradle.kts', 'pom.xml' ],
  \     'capabilities': { 'workspace': { 'configuration': v:true } },
  \   },
  \ ]

