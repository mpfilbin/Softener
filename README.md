# Softener

Softener extends the Fabric API with several useful POSIX shell commands. The list of curently implemented shell commands include:


- link (ln): useful for creating literal and symbolic linkages
- unlink (rm):deletes a file, directory, or contents of a directory
- copy (cp): copies a file or a directory
- mkdir: creates a new directory. Supports creating parent directories if they do not exist
- untar: Unpack a tarball archive. Supports decompressing gzipped tarballs also
- restart: Restarts a service registered with the init system (/etc/init or /etc/init.d)


Additionally, softener provides a layer or indirection that allows multiple shells to be supported. Currently, Softener supports both a traditional POSIX shell and a Cygwin shell for Linux and Windows systems respectively.

## Useage:

Softener is intended to be used with Fabric. To leverage Softener in Fabric, simply clone the Fabric repository and add your fabfile.

*At some point, I plan to package this as a standalone module that can be included in your fabfile*
