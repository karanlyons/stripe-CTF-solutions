level05
=======

`level05` is an uppercasing service written in Python, using a work queue.

	$ curl localhost:9020 -d "uppercase"
	{
		"processing_time": 5.0067901651228115e-06,
		"queue_time": 0.41274619102378031,
		"result": "UPPERCASE"
	}

If you look at lines 52–65, you'll see that it's using `pickle` to pass our string around. And it's not sanitizing it. All we need to do supply a string that, when unpickled, gives us access to the password. We can't just drop into a shell, but we *can* use Python's `os.system()` function to copy the password to a file we can read.

I chose to hand pickle my code, because the exploit was fairly simple. You could instead use the `__reduce__()` method in an object, and use `pickle` to do the pickling for you.
