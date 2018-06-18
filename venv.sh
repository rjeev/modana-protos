#!/usr/bin/env bash
#!/usr/bin/env bash
DIRECTORY=virtualenvs/.auth-service
deactivate 2> /dev/null
if [ -d "${DIRECTORY}" ]; then
    source ${DIRECTORY}/bin/activate
else
    virtualenv -p `which python3` ${DIRECTORY}
    source ${DIRECTORY}/bin/activate
fi

export SERVICE_NAME="auth-service"
export PORT="5000"
