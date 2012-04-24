level04
=======

`level04` is a program that copies a string we give it into a buffer:

	$ ./level04 "This is my string."
	Oh no! That didn't work!

If we look at `fun()` on line 5, we see that it doesn't check the length of the string before copying into the `buf`. So what we've got here is a standard buffer overflow attack. Except for that pesky ASLR.

The first thing we've got to do is figure out how long our string has to move outside of `buf` and put our own address onto `eip`, the instruction pointer. Some trial and error with `gdb` and a NOP sled shows 1036 to be the magic number.

Next we've got to find a hardcoded address in `level04` that we can use to call some shellcode. Using `objdump` we find that there's one in `frame_dummy()`, calling eax, which just happens to be where the start of our string is. So if we supply our shellcode, followed by a bunch of NOPs, and then the address of `frame_dummy()`, `level04` end ups running our shellcode, which gives us access to the password.

### *—Or—*

There's another magical solution. Really, it's just absurdly lucky, and it really requires a thorough explanation to understand. Which this, clearly, isn't.

*But,* if you take a look at `magical solution.txt`, you'll find a full `gdb` tour through the exploit that you can set up and run yourself, to see how the exploit works. You'll need to run the tour inside the Stripe VM (or, possibly, run this repo's copy of `level04` on any 32bit machine).

It's for this reason that I don't have a plain English explanation here; doing one from memory would just end up misleading you, and quite frankly the explanation that I wrote up at the time of the CTF was rather terrible. But if you run through the tour with a good understanding of assembly, it should be easy to understand.