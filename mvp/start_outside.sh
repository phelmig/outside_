NAME="outside"                                  # Name of the application
OUTSIDEDIR=$(cat /home/mya/outside_dir.txt)
DJANGODIR=$OUTSIDEDIR/mvp/outside             # Django project directory
SOCKFILE=/home/mya/apps/outside/gunicorn.sock  # we will communicte using this unix socket
USER=mya                                        # the user to run as
GROUP=mya                                     # the group to run as
NUM_WORKERS=12                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=outside.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=outside.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=info  \
  --log-file=-
