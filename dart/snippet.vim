let g:ycm_language_server += [
  \   {
  \     'name': 'dart',
  \     'cmdline': [ 'dart', expand( g:ycm_lsp_dir . '/dart/analysis_server.dart.snapshot' ), '--lsp' ],
  \     'filetypes': [ 'dart' ],
  \   },
  \ ]
