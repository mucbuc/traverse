{
	'includes':[
		'lib/traverse/def/base.gypi',
		'plank/def/mac-targets.gypi',
		'plank/def/cpp11-gcc.gypi'
	],#inclues
	'target_defaults': {
		'target_name': 'test-gcc',
		'type': 'executable',
		'sources': [
			'src/main.cpp',
		], #sources
		'include_dirs': [
			'plank/src/',
			'.'
		], #include_dirs		
	}, #target_defaults
}