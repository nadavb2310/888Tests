hosts="ansible all -i $ENVS_PATH/env.properties --list-hosts"
output=`eval $hosts`
echo $output | cut -d' ' -f3- > hosts