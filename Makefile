all: run
run: clean
	/usr/bin/python3 play.py
	/usr/bin/python3 read.py
clean:
	rm -f example.db
