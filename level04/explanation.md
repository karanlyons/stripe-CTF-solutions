level04
=======

`level04` is a program that copies a string we give it into a buffer:

	$ ./level04 "This is my string."
	Oh no! That didn't work!

If we look at `fun()` on line 5, we see that it doesn't check the length of the string before copying into the `buf`. So what we've got here is a standard buffer overflow attack. Except for that pesky ASLR.

The first thing we've got to do is figure out how long our string has to move outside of `buf` and put our own address onto `eip`, the instruction pointer. Some trial and error with `gdb` and a NOP sled shows 1036 to be the magic number.

Next we've got to find a hardcoded address in `level04` that we can use to call some shellcode. Using `objdump` we find that there's one in `frame_dummy()`, calling eax, which just happens to be where the start of our string is. So if we supply our shellcode, followed by a bunch of NOPs, and then the address of `frame_dummy()`, `level04` end ups running our shellcode, which gives us access to the password.
