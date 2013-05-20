level03
=======

`level03` is a program that can perform some basic string manipulations:

	$ ./level03 
	Usage: ./level03 INDEX STRING
	Possible indices:
	[0] to_upper	[1] to_lower
	[2] capitalize	[3] length
	
	$ ./level03 0 "uppercase"
	Uppercased string: UPPERCASE

If we take a look at the source, we can see on line 68 that the options are stored in `fns` as an array of pointers to the various string manipulation functions. We can also see `run()` on line 50, which helpfully calls `system()`. If we can get `level03` to call our `run()` with our string, we can get `level03` to run whatever we want, just like in `level01`.

*(An aside: You may then see `strncpy()` on line 60. You will then, I am sure, notice `\0` on line 61. If that's all the thought you paid to those two lines, you're far better at this than I am.)*

We still don't have an avenue for an attack, however. But if we look at line 80 we see that `level03` only checks to see that `index` isn't too high, not too low. So we can move the index outside of the array of pointers to something lower in the stack. Which `buf`, inside of `truncate_and_call()` is (recall that the stack grows towards lower addresses, and `buf` is created after `fns`).

So we need the address of `run()`, since `level03` accesses its string manipulation functions via that array of pointers. We then need an index that'll point somewhere in `buf`, which'll contain our string. The start of `buf` seems a fine place. To find this index we'll need to know the address of the start of `buf` and the address of the start of `fns`.

Firing up `gdb`, we get the three addresses we need. The difference between the start of `buf` and `fns` turns out to be -112. We've got to account for word size here, so we divide by 4 (we're on a 32bit system) to get -28 as our index.

Next we've got to get `truncate_and_call()` to call `run()`. It's expecting to see a pointer at our supplied index, so we just need to give it the pointer for `run()` (remember that the system is little-endian). And now `run()` will take our string and call it with `system()`. So tack on `sh`, and we've got access to the password.
