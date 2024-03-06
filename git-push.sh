# pytest - v = pytest verbose -> longer message
# $ gets value of varible in shell script
# use ./git-push.sh to run in the terminal
# ? is value of pytest varible, 0 means they pass
# -eq syntax for equals
# fi ends the if statement (if backwards)
pytest -v
pytest_status = $?
pytest_pass = 0
if [ $pytest_status -eq $pytest_pass ]
then
  git add .
  echo "Enter a commit message: "
  read commitComment
  git commit -m "$commitComment"
  echo "What branch should the commit be pushed to? "
  read branch
  git push origin "$branch"
else
    echo At least one test did not pass - git commit not created
fi
