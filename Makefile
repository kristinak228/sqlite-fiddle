all: run
run: clean
	/usr/bin/python3 play.py
clean:
	rm -f example.db
