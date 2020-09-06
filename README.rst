Sphinx autodocgen extension
===========================

A free extension for Sphinx (the documentation generator) that automatically generates .rst files for 
Python modules. Each module is a page with ``autodoc`` and navigation subheadings for each class, and 
each package has an autosummary with links and description for each of the the modules it contains. 

The project this was originally developed for the PySys test framework. To see what the documentation for a typical 
module looks like, `see here <https://pysys-test.github.io/pysys-test/autodocgen/pysys.writer.html>`_. 

Features include:

	- A strong emphasis on extensibility by writing simple Python callbacks. The extension takes care of walking the 
	  Python hierarchy (the tricky bit), but lets you choose exactly what you want the rst to look like, using the 
	  full power of Python rather than the (sometimes) restrictive templating library approach taken by other plugins. 
	  
	- Nice defaults that give an autosummary table for each package so users know what each of the contained modules 
	  is for, and for each module a single page listing all the classes (and other members) with a navbar-visible 
	  subheading for each class. 
	
	- Skipping of modules (e.g. internal modules) controlled by a regular expression. 
	
	- Ability to customize the autodoc configuration for individual modules. 
	
	- Ability to choose the title of each topic using a Python callback. 
	
	- Automatic generation of .rst files as part of conf.py without the need to separately run a tool like autogen 
	  first. 

Sample
------

To use it, just add a few lines to your ``conf.py``::

	extensions = [
		...
		'sphinx.ext.autodoc',
		'sphinx.ext.autosummary',
		'sphinxcontrib_autodocgen',
	]

	import mymodule # The module you're documenting (assumes you've added the parent dir to sys.path)
	
	autodocgen_config = {
		'modules':[mymodule], 
		'generated_source_dir': DOC_SOURCE_DIR+'/autodocgen-output/',
		
		# if module matches this then it and any of its submodules will be skipped
		'skip_module_regex': '(.*[.]__|myskippedmodule)', 
		
		# produce a text file containing a list of everything documented. you can use this in a test to notice when you've 
		# intentionally added/removed/changed a documented API
		'write_documented_items_output_file': 'autodocgen_documented_items.txt',
		
		# customize autodoc on a per-module basis
		'autodoc_options_decider': { 
			'mymodule.FooBar':    { 'inherited-members':True },
		},
		
		# choose a different title for specific modules, e.g. the toplevel one
		'module_title_decider': lambda modulename: 'API Reference' if modulename=='mymodule' else modulename,
	}

