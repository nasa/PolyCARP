dry=--dry-run

all:
	@echo "make releasej [-e dry=] | releasecpp [-e dry=]"

releasej: 
	rsync $(dry) -avz --exclude .DS_Store --exclude build_type.txt --exclude *.class --delete tmp/FormalATMj_polycarp/ Java/
	@echo
	@echo "make releasej -e dry="

releasecpp: 
	rsync $(dry) -avz --exclude .DS_Store --exclude build_type.txt --exclude .gitignore --delete tmp/FormalATM++_polycarp/ C++/
	@echo
	@echo "make releasecpp -e dry="

