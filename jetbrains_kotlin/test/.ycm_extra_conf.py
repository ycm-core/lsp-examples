def Settings( **kwargs ):
  return {
    'config_sections': {
      'jetbrains.kotlin': {
        'hints': {
          # Show parameter name hints at call sites
          'parameters': True,
          # Show return type hints in call chains
          'call': { 'chains': True },
        },
      },
    },
  }
