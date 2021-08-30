BINDIR=./bin
SRCDIR=./src
DOCDIR=./javadocs

.SUFFIXES: .java .class

${BINDIR}/%.class: ${SRCDIR}/%.java
	javac $< -cp ${BINDIR} -d ${BINDIR}

${BINDIR}/Generate.class: ${BINDIR}/PowerBSTApp.class ${BINDIR}/PowerBSTAppTest.class ${BINDIR}/PowerArrayApp.class ${BINDIR}/PowerArrayAppTest.class ${SRCDIR}/Generate.java

clean:
	rm -f ${BINDIR}/*.class
run: 
	java -cp ./bin Generate

docs:
	javadoc -classpath ${BINDIR} -d ${DOCDIR} ${SRCDIR}/*.java
cleandocs:
	rm -rf ${DOCDIR}/*
