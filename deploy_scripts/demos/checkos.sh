echo "$OSTYPE";

case $OSTYPE in
	linux*)   echo "Your system is LINUX" ;;
	darwin*)  echo "Your system is OSX" ;;
	mysys*)   echo "Your system is WINDOWS" ;;
	bsd*)	  echo "Your system is BSD" ;;
	solaris*) echo "Your system is SOLARIS" ;;
	*)        echo "unknown: $OSTYPE" ;;
esac

