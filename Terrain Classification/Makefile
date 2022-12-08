BINDIR=./bin
SRCDIR=./src
DOCDIR=./doc

.SUFFIXES: .java .class

${BINDIR}/%.class: ${SRCDIR}/%.java
	javac $< -cp ${BINDIR} -d ${BINDIR}

${BINDIR}/Output.class: ${BINDIR}/BasinCount.class ${BINDIR}/Sequential.class ${SRCDIR}/Output.java

clean:
	rm -f ${BINDIR}/*.class
run: 
	java -cp ./bin Output
docs:
	javadoc -classpath ${BINDIR} -d ${DOCDIR} ${SRCDIR}/*.java
cleandocs:
	rm -rf ${DOCDIR}/*

