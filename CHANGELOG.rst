1.4
===
* Add support for Sphinx 8 (use a more realistic fake environment, deal with ObjectMember changes, etc)
* Change configuration defaults to avoid passing functions and modules, which generates a warning in modern Sphinx due to not being picklable

1.3
===

Change configuration to accept a list of configs, in case you want to handle multiple sub-projects with different 
auto-generated output directories. 

1.2
===

v1.2 is the first public release. It is fully functional, but so far without documentation/samples/testing. 
