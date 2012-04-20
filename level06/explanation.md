level06
=======

`level06` is a basically a password checker. A *really bad one*:

	$ ./level06
	Usage: ./level06 file guess

	Compares the contents of a file with a guess, and
	makes fun of you if you didn't get it right.
	
	$ ./level06 /home/the-flag/.password "This totally isn't the password."	
	Welcome to the password checker!
	................................
	Ha ha, your password is incorrect!

`level06` checks the password character by character, as you can see on line 56. What's more, it calls `taunt()` at the first wrong character, and though that message doesn't print until after every character has been checked (as it's over stdout, whilst the dots are over stderr), that call is going to add a noticeable delay, which we can use to figure out if we're on the right track with our guesses. It's timing attack time.

*(Unless you're clever, then it's force the taunt message to print when `taunt()` is called using rlimits time. But timing attacks are cool.)*

There's not much reason to explain this solution any further. But take a look at `timing.py` for some neat performance tricks and terrible variable naming.
