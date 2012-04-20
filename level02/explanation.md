level02
=======

`level02.php` is a PHP script that stores and retrieves some information from the cookie `user_details`:

	$ curl http://ctf.stri.pe/level02.php | sed -n 's/      <p>\(.*\)/\1/p'
	Looks like a first time user. Hello, there!
	
	$ curl http://ctf.stri.pe/level02.php | sed -n 's/      <p>\(.*\)/\1/p'
	173.255.249.22 using curl/7.19.7 (i686-pc-linux-gnu) libcurl/7.19.7 OpenSSL/0.9.8k zlib/1.2.3.3 libidn/1.15

If we look at the source, we can see that on lines 14 and 15, the script creates a randomly named text file, writes some information to it, and then stores this filename in our cookie. When we visit the script again, it'll recall the filename from the cookie, and print whatever was in the file.

The problem is that on line 23 we can see that the filename stored in our cookie isn't sanitized at all, but merely tacked on to `'/tmp/level02'`. So we just need to create a path that points to the password, and put that in our cookie instead.
