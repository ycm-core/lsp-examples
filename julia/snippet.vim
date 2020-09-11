let s:julia_cmdline = ['julia', '--startup-file=no', '--history-file=no', '-e', '
\       using LanguageServer;
\       using Pkg;
\       import StaticLint;
\       import SymbolServer;
\       env_path = dirname(Pkg.Types.Context().env.project_file);
\       debug = false;
\
\       server = LanguageServer.LanguageServerInstance(stdin, stdout, debug, env_path, "", Dict());
\       server.runlinter = true;
\       run(server);
\   ']

let g:ycm_language_server += [
  \   { 'name': 'julia',
  \     'filetypes': [ 'julia' ],
  \     'project_root_files': [ 'Project.toml' ],
  \     'cmdline': s:julia_cmdline
  \   },
  \ ]
