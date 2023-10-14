@echo off

SET TARGET=origin/main

IF /I "%1"==".DEFAULT_GOAL " GOTO .DEFAULT_GOAL 
IF /I "%1"=="help" GOTO help
IF /I "%1"=="lint" GOTO lint
IF /I "%1"=="format" GOTO format
GOTO error

:.DEFAULT_GOAL 
	CALL make.bat =
	CALL make.bat help
	GOTO :EOF

:help
	@grep -E '^[a-zA-Z_-]+:.*?
	GOTO :EOF

:lint
	./git-diff-lint -x "ruff check --exit-zero" -b %TARGET%
	
	darker --revision %TARGET% --diff --check
	GOTO :EOF

:format
	darker --revision %TARGET%
	
	./git-diff-lint -x "ruff --fix --silent --exit-zero" -b %TARGET%
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
