# The dockerfile begins with defining an image FROM which the build process starts.
# Since our module is based on python 3.0, we use python:3 as our base image.
# You can find trusted docker contains at https://store.docker.com/.
FROM python:3.6

# WORKDIR changes the active directory of the container to a specific location.
# In case you need to run commands from or in a particular location.
WORKDIR /usr/src/app

# Herje we copy the requirements.txt file and install all the required external libraries
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Here we are copying all our files to the root directory of the container
COPY ./apeer_main.py .
COPY ./plot_2Dtrack.py .
COPY ./module_specification.json .

# mount volumes
VOLUME [ "/input", "/output" ]

# In this example, we would like to run our python command when the container starts.
ENTRYPOINT [ "python", "./apeer_main.py" ]
