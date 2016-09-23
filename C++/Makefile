# Simple Makefile to build PolyCARP library and example application

SRCS   = $(wildcard src/*.cpp)
OBJS   = $(SRCS:.cpp=.o)
INCLUDEFLAGS = -Iinclude 
CXXFLAGS = $(INCLUDEFLAGS) -Wall -O 

all: lib example

lib: $(OBJS)
	@echo 
	@echo "** Building PolyCARP binary library"
	ar -cr lib/PolyCARP.a $(OBJS) && ranlib lib/PolyCARP.a #&& rm *.o
	@echo 

example:
	@echo
	@echo "** Building DaidalusExample application"
	$(CXX) -o PolycarpExample $(CXXFLAGS) PolycarpExample.cpp lib/PolyCARP.a
	@echo 
	@echo "** To run PolycarpExample type:"
	@echo "./PolycarpExample"

clean:
	rm -f PolycarpExample $(OBJS) lib/PolyCARP.a

.PHONY: all lib example
