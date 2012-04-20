level01
=======

`level01` is a program that prints the date and time:

	$ ./level01
	Current time: Fri Apr 20 06:20:27 PDT 2012

This looks remarkably similar to `date`:

	$ date
	Current time: Fri Apr 20 06:20:28 PDT 2012

And if you've got any doubts, Stripe's left their source code for you to take a look at, where on line 8 you'll see `system("date")`. If we can replace `date` with our own code, we can get `level01` to run what we want instead.

Of course we can't just directly replace `date`, but we *can* tell the system to look somewhere else, simply by rewriting our `PATH`, and directing it to a file called `date` that we control. Then `level01` will run our code instead of the normal `date`, with its own `setuid`.

My solution is far more complex than is actually necessary; you could just create a link from `/bin/sh` to `date` and get the same effect.
