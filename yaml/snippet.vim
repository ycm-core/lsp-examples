let g:ycm_language_server += [
  \   {
  \     'name': 'yaml',
  \     'cmdline': [ 'node', expand( g:ycm_lsp_dir . '/yaml/node_modules/.bin/yaml-language-server' ), '--stdio' ],
  \     'filetypes': [ 'yaml' ],
  \     'capabilities': {
  \       'workspace': { 'configuration': v:true },
  \       'textDocument': {
  \         'completion': {
  \           'completionItem': { 'snippetSupport': v:true },
  \         }
  \       }
  \     },
  \   },
  \ ]
