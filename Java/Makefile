# Simple Makefile to build PolyCARP library and example application

SRCS  = $(wildcard src/gov/nasa/larcfm/Util/*.java src/gov/nasa/larcfm/ACCoRD/*.java)
OBJS  = $(SRCS:.java=.class)
JAVAC = javac
JAR   = jar

all: example

lib: $(SRCS)
	@echo 
	@echo "** Building PolyCARP jar library"
	$(JAVAC) -cp src src/gov/nasa/larcfm/Util/*.java src/gov/nasa/larcfm/ACCoRD/*.java
	cd src; $(JAR) cvf ../lib/PolyCARP.jar gov/nasa/larcfm/Util/*.class gov/nasa/larcfm/ACCoRD/*.class

example:
	test -f lib/PolyCARP.jar || make lib
	@echo 
	@echo "** Building PolycarpExample application"
	$(JAVAC) -cp lib/PolyCARP.jar src/PolycarpExample.java
	@echo 
	@echo "** To run PolycarpExample type:"
	@echo "./PolycarpExample"

clean:
	rm -f PolycarpExample.class $(OBJS) lib/PolyCARP.jar

.PHONY: all lib example
