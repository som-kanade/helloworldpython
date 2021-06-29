#!/bin/bash
GIT_TAG_NAME="rc"
is_flag_needed="yes"
if [[ $GIT_TAG_NAME == "rc" && $is_flag_needed == "yes" ]]; then 
echo "okay done"
else
echo "not done"
fi